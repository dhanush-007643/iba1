from sensor.sensor import detect_obstacle

def test_obstacle():
    assert detect_obstacle(5) == True