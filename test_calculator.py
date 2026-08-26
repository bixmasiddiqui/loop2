import pytest
from fix_test.calculator import calculator

def test_addition():
    assert calculator(2, 3, "+") == 5

def test_subtraction():
    assert calculator(5, 2, "-") == 3

def test_multiplication():
    assert calculator(4, 3, "*") == 12

def test_division():
    assert calculator(10, 2, "/") == 5

def test_invalid_operation():
    assert calculator(1, 2, "%") == "Invalid operation"
