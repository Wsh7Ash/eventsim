from eventsim.simulator import simulate_mm1

def test_sim():
    res = simulate_mm1(0.5, 1.0, 100)
    assert res['served'] >= 0
