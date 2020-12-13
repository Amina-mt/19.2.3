import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 15, 35) == 525

    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 525, 25) == 21

    def test_substraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 98, 68) == 30

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 188, 812) == 1000