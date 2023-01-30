"""Test Suite for Exercise 5"""

# Traditional Assertion Test

import pytest
from exercises import exercise5


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (10, -2, -5),
        (-10, 2, -5),
        (-10, -10, 1),
        (0, 2, 0),
        (0, -2, 0),
    ],
    ids=[
        "a>0, b>0",
        "a>0, b<0",
        "a<0, b>0",
        "a<0, b<0",
        "a=0, b>0",
        "a=0, b<0"
    ],
)
def test_division_concrete_examples(a: float, b: float, expected: float):
    assert exercise5.division(a, b) == expected


def test_division_denominator_equal_zero():
    with pytest.raises(ValueError):
        exercise5.division(1, 0)


# Property Testing

from hypothesis import assume, given, strategies as st  # noqa: E402
from exercises import exercise5  # noqa: E402, F811
import math  # noqa: E402

finate_floats = st.floats(allow_nan=False, allow_infinity=False)


@given(finate_floats, finate_floats)
def test_division_property_inverse(a, b):
    assume(b != 0)

    result = exercise5.division(a, b) * b
    assume(math.isfinite(result))
    assert math.isclose(result, a, abs_tol=1e-5), result


@given(finate_floats)
def test_division_property_reverse(a):
    assume(a != 0)
    assert exercise5.division(a, a) == 1


@given(finate_floats)
def test_division_property_identity_element(a):
    assert exercise5.division(a, 1) == a


@given(finate_floats)
def test_division_property_absorbent_element(a):
    assume(a != 0)
    assert exercise5.division(0, a) == 0


@given(finate_floats)
def test_division_property_nondefined(a):
    with pytest.raises(ValueError):
        exercise5.division(a, 0)
