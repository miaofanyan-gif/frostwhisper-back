from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class UserAddress(Base):
    __tablename__ = "user_addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    consignee = Column(String(64), nullable=False)  # 收货人
    country_code = Column(String(10), default="US")  # 国家代码
    state = Column(String(64))  # 省/州
    city = Column(String(64))  # 城市
    address = Column(String(255), nullable=False)  # 详细地址
    zip_code = Column(String(20))  # 邮编
    is_default = Column(Boolean, default=False)  # 是否为默认地址

    # 关联用户模型
    user = relationship("UserMain", back_populates="addresses")
