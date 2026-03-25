from enum import IntEnum, Enum


class DynastyEnum(IntEnum):
    """朝代映射：用于汉服垂直分类"""
    TANG = 1    # 唐代
    SONG = 2    # 宋代
    MING = 3    # 明代
    JIN = 4     # 晋制
    DAILY = 5   # 改良/日常


class OrderStatus(IntEnum):
    """订单状态流转"""
    PENDING = 0     # 待支付
    PAID = 1        # 已支付/制作中
    SHIPPED = 2     # 跨境物流中
    RECEIVED = 3    # 已签收
    REFUNDING = 4   # 退款/售后


class RegionType(str, Enum):  # 建议继承 str，方便 JSON 序列化
    """跨境地区标识"""
    ASIA = "Asia"
    EUROPE = "Europe"
    AMERICA = "America"


class UserLayerEnum(IntEnum):
    """企划书定义的4类用户分层"""
    ENTHUSIAST = 1    # 核心汉服爱好者 (Hanfu enthusiasts)
    NEWBIE = 2        # 想要尝试的新手 (People who want Hanfu)
    SCENE_USER = 3    # 特定场景用户 (Specific scenes: weddings, photos)
    GIFT_USER = 4     # 礼品需求用户 (Buy Hanfu as gifts)


class MemberLevelEnum(IntEnum):
    """会员等级"""
    NORMAL = 0
    SILVER = 1
    GOLD = 2
    DIAMOND = 3


class CouponTypeEnum(IntEnum):
    """优惠券类型"""
    FIXED = 1      # 满减
    DISCOUNT = 2   # 折扣
    THRESHOLD = 3  # 无门槛
