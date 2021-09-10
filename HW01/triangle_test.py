import pytest
from triangle import classify_triangle

def test_valid_triangle():
    assert classify_triangle(1,1,2) == "Invalid triangle"

def test_equilateral_triangle():
    assert classify_triangle(1,1,1) == "Equilateral triangle"

def test_right_scalene_triangle():
    assert classify_triangle(5,12,13) == "Right triangle and Scalene triangle"

def test_scalene_triangle():
    assert classify_triangle(15,32,34) == "Scalene triangle"

def test_isosceles_triangle():
    assert classify_triangle(3,3,5) == "Isosceles triangle"
