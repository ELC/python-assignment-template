"""Test Suite for Exercise 4"""

# Traditional Assertion Test

import pytest
from exercises import exercise5


def test_division_assert_a_greater_than_b():
    assert exercise5.division(10, 2) == 5


def test_division_assert_a_less_than_b():
    assert exercise5.division(-10, 2) == -5


def test_division_assert_a_equals_b():
    assert exercise5.division(-10, -10) == 1


def test_division_assert_a_equals_zero():
    assert exercise5.division(0, 2) == 0


def test_division_assert_b_equal_zero():
    with pytest.raises(ValueError):
        exercise5.division(1, 0)


# Property Testing

from hypothesis import assume, given, strategies as st  # noqa: E402
from exercises import exercise5  # noqa: E402, F811
import math  # noqa: E402


@given(st.floats(allow_nan=False, allow_infinity=False),
       st.floats(allow_nan=False, allow_infinity=False))
def test_division_property_inverse(a, b):
    assume(b != 0)

    result = exercise5.division(a, b) * b
    assume(math.isfinite(result))
    assert math.isclose(result, a)


@given(st.floats(allow_nan=False, allow_infinity=False))
def test_division_property_reverse(a):
    assume(a != 0)
    assert exercise5.division(a, a) == 1


@given(st.floats(allow_nan=False, allow_infinity=False))
def test_division_property_identity_element(a):
    assert exercise5.division(a, 1) == a


@given(st.floats(allow_nan=False, allow_infinity=False))
def test_division_property_absorbent_element(a):
    assume(a != 0)
    assert exercise5.division(0, a) == 0


@given(st.floats(allow_nan=False, allow_infinity=False))
def test_division_property_nondefined(a):
    with pytest.raises(ValueError):
        exercise5.division(a, 0)
