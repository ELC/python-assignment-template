"""Test Suite for Exercise 1"""
import doctest


def test_hello_world_doctest():
    from exercises import exercise1
    assert doctest.testmod(exercise1).failed == 0
