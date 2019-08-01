import pytest
from calculator import Calculator, CalculatorError

class TestCalculator():

    @pytest.fixture()
    def test_setup(self):
        global cal 
        cal = Calculator()

    def test_add(self, test_setup):
        result = cal.add(2, 3)
        assert result == 5

    def test_add_str(self, test_setup):
        with pytest.raises(CalculatorError) as context:
            result = cal.add("two", 3)
        assert str(context.value) == "'two' is not a number"

    def test_divide(self, test_setup):
        result = cal.divide(6, 3)
        assert result == 2

    def test_divide_zero(self, test_setup):
        with pytest.raises(CalculatorError) as context:
            result = cal.divide(6, 0)
        assert str(context.value) == "Can not divide by zero!"