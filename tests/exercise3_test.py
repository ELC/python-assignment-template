"""Test Suite for Exercise 3"""
import doctest


def test_hello_world_assert():
    from exercises import exercise3

    assert doctest.testmod(exercise3).failed == 0
