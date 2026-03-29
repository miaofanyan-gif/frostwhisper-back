from cryptography.fernet import Fernet
from app.config.config import settings
from sqlalchemy.future import select

from app.schemas.users import UserRegister, UserLogin
from app.core.security import verify_password
from app.core.security import get_password_hash
from app.models.user import UserMain, MemberLevel, UserAddress
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import update


# 初始化加密器 (KEY 存于 .env)
fernet = Fernet(settings.SECRET_KEY)


class UserService:
    @staticmethod
    def encrypt_data(data: str) -> str:
        return fernet.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt_data(token: str) -> str:
        return fernet.decrypt(token.encode()).decode()

    @staticmethod
    def register_user(db: Session, user_in: UserRegister):
        """用户注册逻辑"""
        # 先查询用户名是否已被占用
        existing_user = db.query(UserMain).filter(
            UserMain.username == user_in.username).first()
        if existing_user:
            # 抛出自定义异常，FastAPI 会捕获并返回 400
            raise HTTPException(
                status_code=400, detail="usernaem already exists")
        db_user = UserMain(
            username=user_in.username,
            email=user_in.email,
            password_hash=get_password_hash(user_in.password),
            member_level=1,

            user_tag=user_in.user_tag.value if user_in.user_tag else 0,  # 存储枚举值
        )
        db.add(db_user)
        db.commit()

        db.refresh(db_user)

        return db_user

    @staticmethod
    def calculate_member_level(growth: int) -> MemberLevel:
        """根据成长值自动计算等级"""
        if growth >= 10000:
            return MemberLevel.DIAMOND
        if growth >= 5000:
            return MemberLevel.GOLD
        if growth >= 1000:
            return MemberLevel.SILVER
        return MemberLevel.REGULAR

    @staticmethod
    def add_growth(db: Session, user_id: int, amount: int):
        """增加成长值并触发升级"""
        user = db.get(UserMain, user_id)
        user.growth_value += amount
        user.member_level = UserService.calculate_member_level(
            user.growth_value)
        db.commit()

    @staticmethod
    def authenticate(db: Session, login_data: UserLogin) -> UserMain | None:
        """验证用户登录"""
        # 1. 根据用户名查找用户
        result = db.execute(
            select(UserMain).filter(UserMain.username == login_data.username)
        )
        user = result.scalars().first()

        if not user:
            return None

        # 2. 校验密码：将明文与数据库中的 password_hash 进行比对
        if not verify_password(login_data.password, user.password_hash):
            return None

        return user

    @staticmethod
    def add_address(db: Session, user_id: int, address_in: UserAddress):
        """添加新地址"""
        # 1. 如果新地址设为默认，需先将旧的默认地址取消
        if address_in.is_default:
            UserService.reset_default_address(db, user_id)

        # 2. 创建地址实例
        db_address = UserAddress(
            user_id=user_id,
            consignee=address_in.consignee,
            country_code=address_in.country_code,
            state=address_in.state,
            city=address_in.city,
            address=address_in.address,
            zip_code=address_in.zip_code,
            is_default=address_in.is_default
        )

        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        return db_address

    @staticmethod
    def reset_default_address(db: Session, user_id: int):
        """防范性逻辑：将该用户所有地址设为非默认"""
        db.execute(
            update(UserAddress)
            .where(UserAddress.user_id == user_id)
            .values(is_default=False)
        )
        # 注意：这里不需要单独 commit，调用者会在添加新地址时统一 commit

    @staticmethod
    def get_user_addresses(db: Session, user_id: int):
        """获取用户所有地址（防范：只能查自己的）"""
        result = db.execute(
            select(UserAddress)
            .filter(UserAddress.user_id == user_id)
            .order_by(UserAddress.id.desc())  # 按 ID 倒序
        )
        return result.scalars().all()

    @staticmethod
    def delete_address(db: Session, user_id: int, id: int):
        """删除地址（核心防范：校验所属权）"""
        result = db.execute(
            select(UserAddress).filter(
                UserAddress.id == id,
                UserAddress.user_id == user_id  # 必须校验 ID 和 UserID
            )
        )
        address = result.scalars().first()
        if not address:
            return False

        db.delete(address)
        db.commit()
        return True

    @staticmethod
    def set_default_address(db: Session, id: int, user_id: int):
        """防范性逻辑：将该用户所有地址设为非默认"""
        UserService.reset_default_address(db, user_id)

        db.execute(
            update(UserAddress)
            .where(UserAddress.id == id)
            .where(UserAddress.user_id == user_id)
            .values(is_default=True)
        )
        db.commit()

        return True
