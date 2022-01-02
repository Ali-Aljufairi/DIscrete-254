import pytest

from itcs254 import Relations as R


def test_is_reflective_1():
    assert R((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)).is_reflective((1, 2, 3, 4)) is False


def test_is_reflective_2():
    assert R((1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)).is_reflective((2, 1, 3, 4)) is True


def test_is_reflective_3():
    assert R((2, 4), (4, 2)).is_reflective((2, 1, 3, 4)) is False


def test_is_reflective_4():
    assert R((1, 2), (2, 3), (3, 4)).is_reflective((2, 1, 3, 4)) is False


def test_is_reflective_5():
    assert R((1, 1), (2, 2), (3, 3), (4, 4)).is_reflective((2, 1, 3, 4)) is True


def test_is_reflective_6():
    assert R((1, 3), (1, 4), (2, 3), (2, 4), (3, 1), (3, 4)).is_reflective((2, 1, 3, 4)) is False


def test_is_reflective_7():
    assert R((0, 0), (1, 1), (2, 2), (4, 4), (1, 2), (2, 1), (4, 2), (2, 4)).is_reflective((0, 1, 2, 4)) is True


def test_is_symmetric_1():
    assert R((1, 2), (2, 1)).is_symmetric() is True


def test_is_symmetric_2():
    assert R((1, 2), (3, 4), (2, 1)).is_symmetric() is True


def test_is_symmetric_3():
    assert R((1, 1), (2, 2), (3, 3)).is_symmetric() is True


def test_is_symmetric_4():
    assert R((1, 1), (2, 2), (3, 1)).is_symmetric() is False


def test_is_symmetric_5():
    assert R((1, 6), (2, 2), (3, 1)).is_symmetric() is True


def test_is_symmetric_6():
    assert R((1, 6), (2, 2), (3, 1), (1, 2)).is_symmetric() is False


def test_is_symmetric_7():
    assert R((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)).is_symmetric() is True


def test_is_symmetric_8():
    assert R((1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)).is_symmetric() is True


def test_is_symmetric_10():
    assert R((2, 4), (4, 2)).is_symmetric() is True


def test_is_symmetric_11():
    assert R((1, 2), (2, 3), (3, 4)).is_symmetric() is False


def test_is_symmetric_12():
    assert R((1, 1), (2, 2), (3, 3), (4, 4)).is_symmetric() is True


def test_is_symmetric_13():
    assert R((1, 3), (1, 4), (2, 3), (2, 4), (3, 1), (3, 4)).is_symmetric() is True


def test_is_symmetric_14():
    assert R((0, 0), (1, 1), (2, 2), (4, 4), (1, 2), (2, 1), (4, 2), (2, 4)).is_symmetric() is True


def test_is_symmetric_16():
    assert R((1, 3), (3, 1), (1, 1)).is_symmetric() is True


def test_is_antisymmetric_1():
    assert R((1, 1), (2, 2), (3, 3)).is_antisymmetric() is True


def test_is_antisymmetric_2():
    assert R((1, 2), (2, 2), (2, 2), (2, 3), (3, 4), (4, 1)).is_antisymmetric() is True


def test_is_antisymmetric_3():
    assert R((1, 3), (2, 2), (2, 4), (3, 1), (4, 2)).is_antisymmetric() is False


def test_is_antisymmetric_4():
    assert R((1, 3), (2, 4), (3, 1), (4, 3)).is_antisymmetric() is False


def test_is_antisymmetric_5():
    assert R((1, 1), (1, 6), (1, 3), (1, 9), (6, 1), (6, 3), (3, 1), (3, 6), (3, 3), (9, 1)).is_antisymmetric() is False


def test_is_antisymmetric_6():
    assert R((1, 1), (1, 6), (1, 3), (1, 9), (6, 1)).is_antisymmetric() is False


def test_is_antisymmetric_7():
    assert R((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)).is_antisymmetric() is False


def test_is_antisymmetric_8():
    assert R((1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)).is_antisymmetric() is False


def test_is_antisymmetric_9():
    assert R((2, 4), (4, 2)).is_antisymmetric() is False


def test_is_antisymmetric_10():
    assert R((1, 2), (2, 3), (3, 4)).is_antisymmetric() is True


def test_is_antisymmetric_11():
    assert R((1, 1), (2, 2), (3, 3), (4, 4)).is_antisymmetric() is True


def test_is_antisymmetric_12():
    assert R((1, 3), (1, 4), (2, 3), (2, 4), (3, 1), (3, 4)).is_antisymmetric() is False


def test_is_transitive_1():
    assert R((2, 4), (4, 2)).is_transitive() is False


def test_is_transitive_2():
    assert R((1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (4, 4)).is_transitive() is True


def test_is_transitive_3():
    assert R((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4)).is_transitive() is True


def test_is_transitive_4():
    assert R((1, 2), (2, 3), (3, 4)).is_transitive() is False


def test_is_transitive_5():
    assert R((1, 1), (2, 2), (3, 3), (4, 4)).is_transitive() is True


def test_is_transitive_6():
    assert R((1, 3), (1, 4), (2, 3), (2, 4), (3, 1), (3, 4)).is_transitive() is False


def test_is_transitive_7():
    assert R((0, 0), (1, 1), (2, 2), (4, 4), (1, 2), (2, 1), (4, 2), (2, 4)).is_transitive() is False
