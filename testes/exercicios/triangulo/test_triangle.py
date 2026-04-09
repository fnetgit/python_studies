from triangle import Triangle


def test_is_triangle_true():
    t = Triangle(3, 4, 5)
    assert t.is_triangle() is True


def test_is_triangle_false():
    t = Triangle(2, 2, 7)
    assert t.is_triangle() is False


def test_triangle_type_equilateral():
    t = Triangle(5, 5, 5)
    assert t.triangle_type() == "Equilátero"


def test_triangle_type_isosceles():
    t = Triangle(4, 7, 7)
    assert t.triangle_type() == "Isósceles"


def test_triangle_type_scalene():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "Escaleno"


def test_triangle_has_no_zero_sides():
    t = Triangle(0, 4, 5)
    assert t.is_triangle() is False


def test_triangle_has_no_negative_sides():
    t = Triangle(-1, 4, 5)
    assert t.is_triangle() is False


def test_triangle_has_no_sides():
    t = Triangle(0, 0, 0)
    assert t.is_triangle() is False


def test_triangle_type_not_a_triangle():
    t = Triangle(1, 2, 3)
    assert t.triangle_type() == "Não é triângulo"
