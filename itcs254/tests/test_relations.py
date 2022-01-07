import pytest

from itcs254 import Relations


# ? Test Reflexive
@pytest.mark.parametrize(
    "R,U,B", [
        ({1}, {(1, 1)}, True),
        ({1, 2, 3}, {(1, 1), (1, 3), (3, 1)}, False),
        # TODO: Add more test cases

    ]
)
def test_is_reflective(R, U, B):
    assert Relations(R, U).is_reflective() is B


# ? Test Symmetric
@pytest.mark.parametrize(
    "R,U,B", [
        ({1}, {(1, 1)}, True),
        # TODO: Add more test cases

    ]
)
def test_is_symmetric(R, U, B):
    assert Relations(R, U).is_symmetric() is B


# ? Test Antisymmetric
@pytest.mark.parametrize(
    "R,U,B", [
        ({1}, {(1, 1)}, True),
        # TODO: Add more test cases

    ]
)
def test_is_antisymmetric(R, U, B):
    assert Relations(R, U).is_antisymmetric() is B


# ? Test Transitive
@pytest.mark.parametrize(
    "R,U,B", [
        ({1}, {(1, 1)}, True),
        # TODO: Add more test cases

    ]
)
def test_is_transitive(R, U, B):
    assert Relations(R, U).is_transitive() is B
