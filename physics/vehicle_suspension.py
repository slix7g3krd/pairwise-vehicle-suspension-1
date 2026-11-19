"""第 60 批：越野车压过连续减速带，车身还在弹，轮子已经悬空，落地瞬间又穿进地..."""

def spring_force(stiffness, compression, load):
    """载荷弹簧力。"""
    raise NotImplementedError("TODO: spring_force")

def tire_contact(distances, threshold):
    """多点轮胎接触。"""
    raise NotImplementedError("TODO: tire_contact")

def axle_damping(damping, axle):
    """前后轴阻尼。"""
    raise NotImplementedError("TODO: axle_damping")

def torque_split(torque, slip):
    """四驱扭矩分配。"""
    raise NotImplementedError("TODO: torque_split")

def travel_limit(travel, limit):
    """悬挂行程限位。"""
    raise NotImplementedError("TODO: travel_limit")

def substep_sync(body_dt, susp_dt):
    """刚体与悬挂子步差。"""
    raise NotImplementedError("TODO: substep_sync")

def network_wheel_state(local, remote, lag):
    """网络轮态。"""
    raise NotImplementedError("TODO: network_wheel_state")

def road_friction(material, base):
    """路面摩擦。"""
    raise NotImplementedError("TODO: road_friction")

def weight_transfer(accel, mass):
    """重心转移。"""
    raise NotImplementedError("TODO: weight_transfer")

def bounds_update(bounds, wheel_pos):
    """悬挂包围盒。"""
    raise NotImplementedError("TODO: bounds_update")

def parking_brake(rear_lock, slope):
    """驻车制动。"""
    raise NotImplementedError("TODO: parking_brake")

def wear_grip(wear, base):
    """磨损抓地。"""
    raise NotImplementedError("TODO: wear_grip")

def quality_isolation(quality, params):
    """画质参数隔离键。"""
    raise NotImplementedError("TODO: quality_isolation")
