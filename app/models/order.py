from datetime import datetime
from typing import Optional, Dict, Any
from sqlalchemy import String, DECIMAL, DateTime, Enum, JSON, BigInteger, Text, SmallInteger, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

import enum
from app.core.database import Base

# 定义枚举类映射


class OrderType(str, enum.Enum):
    PURCHASE = "Purchase"
    RENTAL = "Rental"
    CUSTOM = "Custom"


class OrderMain(Base):
    __tablename__ = "order_main"

    # 主键 ID (bigint unsigned, auto increment)
    id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True)

    # 订单号 (varchar(64))
    order_sn: Mapped[str] = mapped_column(
        String(64), unique=True, index=True, nullable=False)

    # 用户 ID (bigint unsigned)
    user_id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), index=True, nullable=False)

    # 订单类型 (enum)
    order_type: Mapped[str] = mapped_column(
        String(10), nullable=False)

    # 订单状态 (tinyint, 默认 0: 待支付)
    # 业务逻辑：用户提交后脚本自动改为 1(已支付), 2(已发货) 等
    order_status: Mapped[int] = mapped_column(
        TINYINT, server_default="0", nullable=False)

    # 金额与币种 (decimal(12,2) & char(3))
    total_amount: Mapped[float] = mapped_column(DECIMAL(12, 2), nullable=False)
    currency: Mapped[str] = mapped_column(
        String(3), server_default="USD", nullable=False)
    deposit: Mapped[Optional[float]] = mapped_column(DECIMAL(12, 2))

    # 支付渠道 (varchar(20))
    pay_channel: Mapped[Optional[str]] = mapped_column(String(20))
    payment_id: Mapped[Optional[str]] = mapped_column(String(64), unique=True)

    # 收货地址 (text)
    shipping_address: Mapped[Optional[str]] = mapped_column(Text)
    tracking_no: Mapped[Optional[str]] = mapped_column(String(64), unique=True)

    # 审计字段
    create_time: Mapped[datetime] = mapped_column(
        DateTime, server_default="CURRENT_TIMESTAMP")
    update_time: Mapped[datetime] = mapped_column(
        DateTime, server_default="CURRENT_TIMESTAMP", onupdate=datetime.now)

    create_by: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), server_default="0")
    update_by: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), server_default="0")

    # 逻辑删除 (tinyint(1))
    is_deleted: Mapped[int] = mapped_column(TINYINT(1), server_default="0")
    order_items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem", back_populates="order_main"  # 这里保持不变，指向 OrderItem.order_main
    )

    def __repr__(self) -> str:
        return f"<Order(order_sn={self.order_sn}, type={self.order_type}, status={self.order_status})>"


class OrderItem(Base):
    __tablename__ = "order_item"  # 对应你截图的表
    id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), ForeignKey("order_main.id"), nullable=False)
    order_sn: Mapped[str] = mapped_column(String(64), nullable=False)
    product_id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), ForeignKey("product_main.id"), nullable=False)
    combo_id: Mapped[Optional[int]] = mapped_column(BIGINT(unsigned=True))
    product_name: Mapped[str] = mapped_column(String(255), nullable=False)

    price: Mapped[Optional[float]] = mapped_column(DECIMAL(12, 2))
    quantity: Mapped[Optional[int]] = mapped_column(SmallInteger)
    total_amount: Mapped[float] = mapped_column(DECIMAL(12, 2), nullable=False)
    currency: Mapped[str] = mapped_column(
        String(3), default="USD", nullable=False  # 修正为 String(3)
    )
    create_time: Mapped[datetime] = mapped_column(
        DateTime, server_default="CURRENT_TIMESTAMP")

    # 关联到 OrderMain，属性名是 order_main
    order_main: Mapped["OrderMain"] = relationship(
        "OrderMain", back_populates="order_items"  # 指向 OrderMain.order_items
    )
    # 关联到 ProductMain，属性名是 product
    product: Mapped["ProductMain"] = relationship(
        "ProductMain", back_populates="order_items"  # 指向 ProductMain.order_items
    )
