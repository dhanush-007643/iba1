from decision.decision import make_decision

def test_decision():
    assert make_decision(True) == "BRAKE"