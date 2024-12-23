import maths_functions
import pytest

@pytest.mark.alegbra
def test_algrbra_square():
     assert maths_functions.Algebra.square(2) == 4
     assert maths_functions.Algebra.square(10) == 100

@pytest.mark.algebra
def test_algebra_cube():
     assert maths_functions.Algebra.cube(2) == 8
     assert maths_functions.Algebra.cube(4) == 64

@pytest.mark.algebra
def test_algebra_add():
     assert maths_functions.Algebra.add(4,5) == 9
     assert maths_functions.Algebra.add(10,20) == 30

@pytest.mark.geometry
def test_is_triangle():
    assert maths_functions.Geometry.is_triangle(120, 40, 20) == True
    assert maths_functions.Geometry.is_triangle(45, 67, 99) == False

@pytest.mark.geometry
def test_is_quadrilateral():
    assert maths_functions.Geometry.is_quadrilateral(350, 5, 5, 0) == True
    assert maths_functions.Geometry.is_quadrilateral(11, 22, 33, 44) == False
