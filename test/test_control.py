from control.control import apply_control

def test_control():
    assert apply_control("BRAKE") == "Vehicle Stopped"