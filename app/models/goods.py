from sqlalchemy import Column, BIGINT, String, Integer, DECIMAL, Boolean, DateTime, ForeignKey, Index, Enum, Text
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
from datetime import datetime
from .constants import DynastyEnum, RegionType
from app.core.database import Base
from typing import List


class ProductMain(Base):
    __tablename__ = "product_main"  # [cite: 401, 482]

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    category_id = Column(Integer, nullable=False,
                         comment='品类ID')  # [cite: 484]
    product_sn = Column(String(64), unique=True, nullable=False)  # [cite: 483]
    name = Column(String(200), nullable=False)  # [cite: 486]
    brand = Column(String(100))  # [cite: 485]
    scene_id = Column(BIGINT, nullable=False)  # [cite: 485]
    name_cn = Column(String(200), nullable=False)  # [cite: 486]
    name_en = Column(String(200), nullable=False)  # [cite: 487]
    dynasty_style = Column(String(50))  # [cite: 488]
    fabric_info = Column(String(100))  # [cite: 489]
    craft_info = Column(String(100))  # [cite: 490]
    base_price = Column(DECIMAL(12, 2), nullable=False)  # [cite: 491]
    market_price = Column(DECIMAL(12, 2), nullable=False)  # [cite: 491]
    price = Column(DECIMAL(12, 2), nullable=False)  # [cite: 491]
    is_rental_available = Column(Boolean, default=False)  # [cite: 492]
    is_customizable = Column(Boolean, default=False)  # [cite: 493]
    create_time = Column(DateTime, default=datetime.now)  # [cite: 494]
    is_deleted = Column(Boolean, default=False)  # [cite: 498]
    status = Column(Integer, default=1)  # [cite: 495]
    update_time = Column(DateTime, default=datetime.now,
                         onupdate=datetime.now)  #
    # 新增：反向关联到 OrderItem
    order_items: Mapped[list["OrderItem"]] = relationship(
        "OrderItem", back_populates="product"  # 指向 OrderItem.product
    )
    images: Mapped[List["ProductImage"]] = relationship(
        'ProductImage', back_populates="product")
    skus: Mapped[List["ProductSku"]] = relationship(
        'ProductSku', back_populates="product")
    comments: Mapped[List["ProductComment"]] = relationship(
        'ProductComment', back_populates="product")


class ProductComment(Base):
    __tablename__ = "product_comment"
    id: Mapped[BIGINT] = mapped_column(
        BIGINT, primary_key=True, autoincrement=True)
    product_id: Mapped[BIGINT] = mapped_column(
        BIGINT, ForeignKey("product_main.id"))
    user_id: Mapped[BIGINT] = mapped_column(BIGINT)
    content: Mapped[str] = mapped_column(Text)
    score: Mapped[int] = mapped_column(Integer, default=5)  # 评分，默认5分
    username: Mapped[str] = mapped_column(String(64))  # 评论用户名
    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)

    product: Mapped["ProductMain"] = relationship(
        "ProductMain", back_populates="comments")


def to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns if not isinstance(getattr(self, c.name), datetime)}


class Category(Base):
    __tablename__ = "category"
    id: Mapped[BIGINT] = mapped_column(
        BIGINT, primary_key=True, autoincrement=True)
    name: Mapped[BIGINT] = mapped_column(String(64), nullable=False)
    parent_id: Mapped[BIGINT] = mapped_column(
        BIGINT, ForeignKey("product_main.id"), default=0)
    status: Mapped[BIGINT] = mapped_column(BIGINT, default=1)
    sort: Mapped[BIGINT] = mapped_column(BIGINT, default=0)
    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    update_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now)


class ProductSku(Base):
    __tablename__ = "product_sku"
    id: Mapped[BIGINT] = mapped_column(
        BIGINT, primary_key=True, autoincrement=True)
    product_id: Mapped[BIGINT] = mapped_column(
        BIGINT, ForeignKey("product_main.id"))
    sku_sn: Mapped[str] = mapped_column(String(64), unique=True)
    color: Mapped[str] = mapped_column(String(32))
    size: Mapped[str] = mapped_column(String(32))
    barcode: Mapped[str] = mapped_column(String(64), nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(12, 2))
    stock: Mapped[BIGINT] = mapped_column(BIGINT, default=0)
    lock_stock: Mapped[BIGINT] = mapped_column(BIGINT, default=0)
    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    update_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now)
    product: Mapped["ProductMain"] = relationship(
        "ProductMain", back_populates="skus")


class ProductImage(Base):
    __tablename__ = "product_image"
    id: Mapped[BIGINT] = mapped_column(
        BIGINT, primary_key=True, autoincrement=True)
    product_id: Mapped[BIGINT] = mapped_column(
        BIGINT, ForeignKey("product_main.id"))
    url: Mapped[str] = mapped_column(String(512))
    sort: Mapped[BIGINT] = mapped_column(BIGINT, default=0)
    is_cover: Mapped[BIGINT] = mapped_column(BIGINT, default=0)
    create_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    product: Mapped["ProductMain"] = relationship(
        "ProductMain", back_populates="images")
