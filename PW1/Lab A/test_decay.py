"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?
def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000,-0.4)


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?
def test_matches_law():
    N0 = 50000
    lam = 0.2
    dt = 0.05
    steps = 100

    counts = simulate(N0, lam, dt=dt, steps=steps, seed=42)
    actual_final = counts[-1]
    t = steps * dt
    expected_final = N0 * np.exp(-lam * t)
    assert actual_final == pytest.approx(expected_final, rel=1e-2)
