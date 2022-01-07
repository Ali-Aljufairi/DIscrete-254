import pytest

from itcs254 import Relations


# ? Test Reflexive
@pytest.mark.parametrize(
    "U,R,B", [
        ({1}, {(1, 1)}, True),
        ({1, 2, 3}, {(1, 1), (1, 3), (3, 1)}, False),
        ({1, 2, 3, 4}, {(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)}, False),
        ({1, 2, 3, 4}, {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)}, True),
        ({1, 2, 3, 4}, {(2, 4), (4, 2)}, False),
        ({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 4)}, False),
        ({1, 2, 3, 4}, {(1, 1), (2, 2), (3, 3), (4, 4)}, True),


        # TODO: Add more test cases

    ]
)
def test_is_reflective(U, R, B):
    assert Relations(U, R).is_reflective() is B


# ? Test Symmetric
@pytest.mark.parametrize(
    "U,R,B", [
        ({1}, {(1, 1)}, True),
        # TODO: Add more test cases
        ({1, 2, 3, 4}, {(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)}, False),
        ({1, 2, 3, 4}, {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)}, True),
        ({1, 2, 3, 4}, {(2, 4), (4, 2)}, True),
        ({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 4)}, False),
        ({1, 2, 3, 4}, {(1, 1), (2, 2), (3, 3), (4, 4)}, True),


    ]
)
def test_is_symmetric(U, R, B):
    assert Relations(U, R).is_symmetric() is B


# ? Test Antisymmetric
@pytest.mark.parametrize(
    "U,R,B", [
        ({1}, {(1, 1)}, True),
        # TODO: Add more test cases
        ({1, 2, 3, 4}, {(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)}, False),
        ({1, 2, 3, 4}, {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)}, False),
        ({1, 2, 3, 4}, {(2, 4), (4, 2)}, False),
        ({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 4)}, True),
        ({1, 2, 3, 4}, {(1, 1), (2, 2), (3, 3), (4, 4)}, True),



    ]
)
def test_is_antisymmetric(U, R, B):
    assert Relations(U, R).is_antisymmetric() is B


# ? Test Transitive
@pytest.mark.parametrize(
    "U,R,B", [
        ({1}, {(1, 1)}, True),
        # TODO: Add more test cases
        ({1, 2, 3, 4}, {(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)}, True),
        ({1, 2, 3, 4}, {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)}, True),
        ({1, 2, 3, 4}, {(2, 4), (4, 2)}, False),
        ({1, 2, 3, 4}, {(1, 2), (2, 3), (3, 4)}, False),
        ({1, 2, 3, 4}, {(1, 1), (2, 2), (3, 3), (4, 4)}, True),



    ]
)
def test_is_transitive(U, R, B):
    assert Relations(U, R).is_transitive() is B
