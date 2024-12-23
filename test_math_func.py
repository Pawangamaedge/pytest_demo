import maths_functions

def test_algebra_square():
     assert maths_functions.Algebra.square(20) == 400
     assert maths_functions.Algebra.square(10) == 100

def test_algebra_cube():
     assert maths_functions.Algebra.cube(2) == 8
     assert maths_functions.Algebra.cube(4) == 64

def test_is_triangle():
    assert maths_functions.Geometry.is_triangle(120, 40, 20) == True
    assert maths_functions.Geometry.is_triangle(45, 67, 99) == False

def test_is_quadrilateral():
    assert maths_functions.Geometry.is_quadrilateral(350, 5, 5, 0) == True
    assert maths_functions.Geometry.is_quadrilateral(11, 22, 33, 44) == False

