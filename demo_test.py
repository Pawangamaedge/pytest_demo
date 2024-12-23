import pytest

def add(a, b):
     return a+b

def sub(a, b):
     return a-b

# class test_class:

#      def test_add():
#           assert add(2,3) == 5
#           assert add(4,5) == 9     
#           assert add(10,20) == 30

#      def test_sub():
#           assert sub(2,3) == -1
#           assert sub(5,3) == 2
#           assert sub(6,5) == 1


def test_addition():
     assert add(2,3) == 5
     

def test_substraction():
     assert sub(3,3) == 0