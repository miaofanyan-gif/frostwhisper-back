from sqlalchemy import Column, BIGINT, String, Integer, DECIMAL, Boolean, DateTime, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum


class UserTagEnum(str, enum.Enum):
    ENTHUSIAST = "Enthusiast"  # 核心爱好者
    NEWBIE = "Newbie"          # 新手
    SCENE = "Scene_User"       # 场景用户 (婚礼/摄影)
    GIFT = "Gift_User"         # 礼品用户


class MemberLevel(str, enum.Enum):
    REGULAR = "Regular"
    SILVER = "Silver"
    GOLD = "Gold"
    DIAMOND = "Diamond"


class UserMain(Base):
    __tablename__ = "user_main"
    id = Column(BIGINT, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(128))
    email = Column(String(100), unique=True, index=True)

    # 企划书核心分层
    user_tag = Column(Integer)

    # 会员体系
    member_level = Column(Integer)
    growth_value = Column(Integer, default=0)  # 成长值（决定等级）
    points = Column(Integer, default=0)       # 积分（用于抵扣）

    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime)
    # 新增 to_dict 方法

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,

            # 把你需要的字段都加进来
        }


class UserAddress(Base):
    __tablename__ = "user_addresses"
    id = Column(BIGINT, primary_key=True)
    user_id = Column(BIGINT, ForeignKey("user_main.id"))
    consignee = Column(String(100))
    country_code = Column(String(10))  # ISO 国家代码
    state = Column(String(100))        # 州/省
    address = Column(String(255))  # 详细地址（加密存储）
    city = Column(String(100))
    zip_code = Column(String(20))
    is_default = Column(Boolean, default=False)
