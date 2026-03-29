from sqlalchemy import Column, BIGINT, Integer, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

from datetime import datetime


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id: Mapped[int] = mapped_column(
        BIGINT, primary_key=True, autoincrement=True, comment="购物车ID")
    user_id: Mapped[int] = mapped_column(
        BIGINT, nullable=False, comment="用户ID")
    product_id: Mapped[int] = mapped_column(BIGINT, ForeignKey(
        "product_main.id"), nullable=False, comment="商品ID")
    quantity: Mapped[int] = mapped_column(
        Integer, default=1, nullable=False, comment="购买数量")
    selected: Mapped[int] = mapped_column(
        Integer, default=1, nullable=False, comment="是否选中 1=是 0=否")

    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), comment='更新时间'
    )
    update_time: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), comment='更新时间'
    )
    is_rent: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="是否租赁 0=购买 1=租赁"
    )
    deposit: Mapped[float] = mapped_column(
        DECIMAL(10, 2), default=0.00, nullable=True, comment="租赁押金"
    )
    rent_date: Mapped[int] = mapped_column(
        Integer, nullable=True, comment="租赁天数"
    )
    is_deleted: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, comment="是否删除 0=正常 1=删除")

    # 关联商品（和你项目完全一致）
    product: Mapped["ProductMain"] = relationship(
        "ProductMain", backref="cart_items")
