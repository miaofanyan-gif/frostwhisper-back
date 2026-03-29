from datetime import datetime
from typing import Optional, Dict, Any
from sqlalchemy import String, DECIMAL, DateTime, Enum, JSON, BigInteger, Text, SmallInteger, BigInteger, Integer, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, TINYINT
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
import enum
from sqlalchemy.sql import func
import enum
from app.core.database import Base

# 定义枚举类映射


class OrderMain(Base):
    __tablename__ = "order_main"

    id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True, comment='订单ID'
    )
    order_no: Mapped[str] = mapped_column(
        String(64), unique=True, index=True, nullable=False, comment='订单编号'
    )
    user_id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), nullable=False, comment='用户ID'
    )
    total_amount: Mapped[float] = mapped_column(
        DECIMAL(12, 2), nullable=False, comment='订单总金额'
    )
    pay_amount: Mapped[float] = mapped_column(
        DECIMAL(12, 2), nullable=False, comment='实付金额'
    )
    freight_amount: Mapped[Optional[float]] = mapped_column(
        DECIMAL(12, 2), default=0.00, comment='运费'
    )
    discount_amount: Mapped[Optional[float]] = mapped_column(
        DECIMAL(12, 2), default=0.00, comment='优惠金额'
    )

    consignee: Mapped[str | None] = mapped_column(
        String(64), nullable=True, comment="收件人姓名"
    )
    is_commented: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment="是否已评论 0未评论 1已评论"
    )
    address: Mapped[str | None] = mapped_column(
        String(255), nullable=True, comment="详细地址"
    )
    country_code: Mapped[str | None] = mapped_column(
        String(20), nullable=True, comment="国家代码"
    )
    state: Mapped[str | None] = mapped_column(
        String(64), nullable=True, comment="州/省"
    )
    city: Mapped[str | None] = mapped_column(
        String(64), nullable=True, comment="城市"
    )
    zip_code: Mapped[str | None] = mapped_column(
        String(20), nullable=True, comment="邮编"
    )
    order_status: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment='订单状态 0待付款 1待发货 2待收货 3已完成 4已关闭'
    )
    pay_status: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment='支付状态 0未支付 1已支付'
    )
    pay_type: Mapped[Optional[int]] = mapped_column(
        SmallInteger, comment='支付方式 1微信 2支付宝'
    )
    currency: Mapped[str] = mapped_column(
        String(3), default="USD", nullable=False, comment='货币类型'
    )

    pay_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, comment='支付时间')
    delivery_time: Mapped[Optional[datetime]
                          ] = mapped_column(DateTime, comment='发货时间')
    receive_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime, comment='确认收货时间')
    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), comment='创建时间')
    update_time: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), comment='更新时间'
    )
    is_deleted: Mapped[int] = mapped_column(
        SmallInteger, default=0, comment='是否删除')
    deposit: Mapped[float] = mapped_column(
        DECIMAL(10, 2), default=0.00, nullable=True, comment="租赁押金"
    )
    is_rent: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="是否租赁 0=购买 1=租赁"
    )
    # 关联订单项
    items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_item"

    id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True, comment='订单项ID'
    )
    order_id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), ForeignKey("order_main.id"), nullable=False, comment='订单ID'
    )
    order_no: Mapped[str] = mapped_column(
        String(64), nullable=False, comment='订单编号'
    )
    product_id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), ForeignKey("product_main.id"), nullable=False, comment='商品ID'
    )

    product_name: Mapped[str] = mapped_column(
        String(255), nullable=False, comment='商品名称（快照）'
    )
    price: Mapped[Optional[float]] = mapped_column(
        DECIMAL(12, 2), comment='下单时单价'
    )
    quantity: Mapped[Optional[int]] = mapped_column(
        SmallInteger, comment='购买数量'
    )
    total_price: Mapped[float] = mapped_column(
        DECIMAL(12, 2), nullable=False, comment='商品小计金额'
    )
    product_image: Mapped[Optional[str]] = mapped_column(
        String(255), comment='商品图片（快照）'
    )

    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), comment='创建时间'
    )
    deposit: Mapped[float] = mapped_column(
        DECIMAL(10, 2), default=0.00, nullable=True, comment="租赁押金"
    )
    rent_date: Mapped[int] = mapped_column(
        Integer, nullable=True, comment="租赁天数"
    )
    is_rent: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="是否租赁 0=购买 1=租赁"
    )
    # 关联订单主表
    order: Mapped["OrderMain"] = relationship(
        "OrderMain", back_populates="items")
