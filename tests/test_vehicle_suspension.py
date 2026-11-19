import pytest
from physics import vehicle_suspension as mod

CASES = [
    ("spring", 'm.spring_force(2.0, 0.5, 1.0) == approx(0.0)'),
    ("tire", 'm.tire_contact([1.0, 2.0, 3.0], 2.0) is True'),
    ("tire_false", 'm.tire_contact([4.0, 5.0], 2.0) is False'),
    ("axle_front", 'm.axle_damping(1.0, "front") == approx(0.8)'),
    ("axle_rear", 'm.axle_damping(1.0, "rear") == approx(1.0)'),
    ("torque", 'm.torque_split(10.0, 0.5) == approx(5.0)'),
    ("travel", 'm.travel_limit(2.0, 1.0) == approx(1.0)'),
    ("sync", 'm.substep_sync(0.02, 0.01) == approx(0.01)'),
    ("network", 'm.network_wheel_state(1, 2, 1) == 2'),
    ("road", 'm.road_friction("ice", 1.0) == approx(0.5)'),
    ("transfer", 'm.weight_transfer(2.0, 3.0) == approx(6.0)'),
    ("bounds", 'm.bounds_update((0.0, 1.0), (2.0, 3.0)) == approx((0.0, 3.0))'),
    ("park", 'm.parking_brake(True, 0.05) is True'),
    ("wear", 'm.wear_grip(0.5, 1.0) == approx(0.5)'),
    ("quality", 'm.quality_isolation("low", 1) == "low:1"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
