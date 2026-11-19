"""第 60 批：越野车压过连续减速带，车身还在弹，轮子已经悬空，落地瞬间又穿进地...

悬挂/轮胎/传动修复：载荷弹簧、多点轮胎接触、前后轴分离阻尼、
四驱扭矩分配、行程硬限位、子步同步、网络轮态、路面摩擦、
重心转移、包围盒更新、驻车制动、磨损抓地、画质参数隔离。
"""

# 各轴阻尼系数：前轴较软抑制点头，后轴较硬抑制甩尾
AXLE_DAMPING_FACTOR = {"front": 0.8, "rear": 1.0}

# 路面材质摩擦系数（相对柏油 = 1.0）
ROAD_FRICTION = {
    "asphalt": 1.0,
    "gravel": 0.8,
    "wet": 0.7,
    "mud": 0.6,
    "ice": 0.5,
    "snow": 0.4,
}

# 驻车制动可保持的最大坡度
PARKING_MAX_SLOPE = 0.3


def spring_force(stiffness, compression, load):
    """载荷弹簧力：弹簧刚度 × 压缩量，减去当前载荷（质量/载重参与）。"""
    return stiffness * compression - load


def tire_contact(distances, threshold):
    """多点轮胎接触：任一采样点距离不超过阈值即视为接地（路缘石边缘不漏检）。"""
    return any(d <= threshold for d in distances)


def axle_damping(damping, axle):
    """前后轴分离阻尼：前轴 0.8、后轴 1.0，未知轴按原值。"""
    return damping * AXLE_DAMPING_FACTOR.get(axle, 1.0)


def torque_split(torque, slip):
    """四驱扭矩分配：按打滑程度把扭矩从打滑轴移走，slip∈[0,1]。"""
    slip = min(max(slip, 0.0), 1.0)
    return torque * (1.0 - slip)


def travel_limit(travel, limit):
    """悬挂行程硬限位：钳制到 [-limit, limit]，防止轮胎穿轮拱。"""
    return max(-limit, min(limit, travel))


def substep_sync(body_dt, susp_dt):
    """刚体与悬挂子步同步：取两者较小步长，避免高速过坎能量注入。"""
    return min(body_dt, susp_dt)


def network_wheel_state(local, remote, lag):
    """网络轮态同步：按延迟向服务端轮态插值，lag≥1 时完全采用远端。"""
    t = min(max(lag, 0.0), 1.0)
    return local + (remote - local) * t


def road_friction(material, base):
    """路面摩擦：基准摩擦 × 材质系数，未知材质按柏油。"""
    return base * ROAD_FRICTION.get(material, 1.0)


def weight_transfer(accel, mass):
    """重心转移：加速度 × 质量，耦合到悬挂载荷（刹车时前轴增载）。"""
    return accel * mass


def bounds_update(bounds, wheel_pos):
    """悬挂包围盒：随轮子位置扩张，防止摄像机近裁剪穿车。"""
    lo, hi = bounds
    wlo, whi = wheel_pos
    return (min(lo, wlo), max(hi, whi))


def parking_brake(rear_lock, slope):
    """驻车制动：手刹锁止且在可保持坡度内时不溜车。"""
    return bool(rear_lock) and abs(slope) <= PARKING_MAX_SLOPE


def wear_grip(wear, base):
    """磨损抓地：基准抓地 × (1 - 磨损)，磨损 1.0 时抓地归零。"""
    wear = min(max(wear, 0.0), 1.0)
    return base * (1.0 - wear)


def quality_isolation(quality, params):
    """画质参数隔离键：按画质档位区分物理参数，低画质不再共享变软。"""
    return f"{quality}:{params}"
