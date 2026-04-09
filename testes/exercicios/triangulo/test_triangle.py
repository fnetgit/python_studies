from triangle import Triangle


def test_is_triangle_true():
    assert Triangle(3, 4, 5).is_triangle() is True


def test_is_triangle_false_sum_less():
    assert Triangle(2, 2, 7).is_triangle() is False


def test_is_triangle_false_sum_equal():
    assert Triangle(1, 2, 3).is_triangle() is False


def test_triangle_has_no_zero_sides():
    assert Triangle(0, 4, 5).is_triangle() is False
    assert Triangle(4, 0, 5).is_triangle() is False
    assert Triangle(4, 5, 0).is_triangle() is False


def test_triangle_has_no_negative_sides():
    assert Triangle(-1, 4, 5).is_triangle() is False
    assert Triangle(4, -1, 5).is_triangle() is False
    assert Triangle(4, 5, -1).is_triangle() is False


def test_triangle_has_no_sides():
    assert Triangle(0, 0, 0).is_triangle() is False


def test_triangle_type_equilateral():
    assert Triangle(5, 5, 5).triangle_type() == "Equilátero"


def test_triangle_type_isosceles():
    assert Triangle(4, 7, 7).triangle_type() == "Isósceles"
    assert Triangle(7, 4, 7).triangle_type() == "Isósceles"
    assert Triangle(7, 7, 4).triangle_type() == "Isósceles"


def test_triangle_type_scalene():
    assert Triangle(3, 4, 5).triangle_type() == "Escaleno"


def test_triangle_type_not_a_triangle():
    assert Triangle(1, 2, 3).triangle_type() == "Não é triângulo"
