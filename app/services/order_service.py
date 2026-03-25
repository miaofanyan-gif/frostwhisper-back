import uuid
from sqlalchemy import select, func, desc
import time
from redis import Redis
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, selectinload
from typing import List, Optional
from app.models.order import OrderMain, OrderType
from app.schemas.order import OrderCreateSchema, OrderStatus, OrderType


redis_client = Redis(host='localhost', port=6379, db=2)


class OrderService:
    @staticmethod
    def create_order(db: Session, user_id: int, order_data: OrderCreateSchema):

        # 1. 幂等性校验 (简单演示：根据请求体哈希或客户端传的ide_key)
        idempotency_key = order_data.idempotency_key
        if redis_client.get(f"order_lock:{idempotency_key}"):
            raise Exception("Duplicate request processed.")

        # 2. 差异化计算金额
        total = 0.0
        ext_info = {}

        if order_data.order_type == OrderType.RENTAL:
            total = order_data.rent_price + order_data.deposit
            ext_info = {"period": order_data.period,
                        "return_date": order_data.return_date}
        elif order_data.order_type == OrderType.CUSTOM:
            total = order_data.custom_price
            ext_info = {
                "requirements": order_data.req, "lead_time": "21 days"}
        else:
            total = order_data.price

        # 3. 生成订单（模拟自动支付和发货）
        new_order = OrderMain(
            order_sn=uuid.uuid4().hex,
            user_id=user_id,
            order_type=order_data.order_type,
            total_amount=total,
            deposit=order_data.deposit or 0,
            # order_ext=ext_info,
            order_status=OrderStatus.SHIPPED,  # 自动变更状态
            payment_id=str(uuid.uuid4()),  # 模拟支付ID
            tracking_no=f"SF{uuid.uuid4().hex[:10].upper()}"  # 模拟物流单号
        )

        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        # 4. 触发异步统计任务

        # from tasks import sync_order_stats
        # sync_order_stats.delay(new_order.id)

        # 设置幂等性锁（5分钟）
        # redis_client.setex(f"order_lock:{idempotency_key}", 300, "1")

        return new_order

    @staticmethod
    def get_order_list(
        db: Session,
        user_id: Optional[int] = None,
        order_type: Optional[str] = None,
        status: Optional[int] = None,
        page: int = 1,
        page_size: int = 20
    ):
     # 1. 构建基础查询语句，同时预加载 order_items
        stmt = select(OrderMain).filter(OrderMain.is_deleted == 0).options(
            selectinload(OrderMain.order_items)  # 关键：预加载关联的 OrderItem
        )

        # 2. 动态添加过滤条件
        if user_id:
            stmt = stmt.filter(OrderMain.user_id == user_id)
        if order_type:
            stmt = stmt.filter(OrderMain.order_type == order_type)
        if status is not None:
            stmt = stmt.filter(OrderMain.order_status == status)

        # 3. 计算总数
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_result = db.execute(count_stmt)
        total = total_result.scalar_one()

        # 4. 分页与排序
        stmt = stmt.order_by(desc(OrderMain.create_time))\
                   .offset((page - 1) * page_size)\
                   .limit(page_size)

        # 5. 执行查询
        result = db.execute(stmt)

        orders = result.scalars().all()
        for order in orders:
            order.order_items

        return {
            "items": orders,
            "total": total,
            "page": page,
            "page_size": page_size
        }

    @staticmethod
    def get_order_detail(db: Session, order_sn: str, user_id: Optional[int] = None):
        """
        查询订单详情
        """
        query = db.query(OrderMain).filter(
            OrderMain.order_sn == order_sn,
            OrderMain.is_deleted == 0
        )

        # 如果是移动端接口，通常需要校验是否为当前用户的订单
        if user_id:
            query = query.filter(OrderMain.user_id == user_id)

        order = query.first()

        if not order:
            return None

        return order
