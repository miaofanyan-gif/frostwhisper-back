from sqlalchemy import Column, BIGINT, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"  # 表名和数据库一致

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT, nullable=False)
    product_id = Column(BIGINT, ForeignKey(
        "product_main.id"), nullable=False, comment='商品ID')
    quantity = Column(Integer, default=1, nullable=False, )
    selected = Column(Integer, default=1, nullable=False)
    create_time = Column(DateTime, default=func.now(),
                         nullable=False, comment='创建时间')
    update_time = Column(DateTime, default=func.now(),
                         onupdate=func.now(), nullable=False, comment='更新时间')
    is_deleted = Column(Integer, default=0, nullable=False,
                        comment='是否删除：0=正常，1=删除')

    # 关联商品表（和你的 ProductMain 关联方式对齐）
    product = relationship("ProductMain", backref="cart_items")
