from utils import division
import pytest

@pytest.mark.parametrize("a, b, excepted", [(10, 5, 2),
                                            (10, 2, 5),
                                            (30, -3, -10)])
def test_divis_func(a, b, excepted):
    assert (a / b) == excepted


# тупо проверяю, что результатом должна быть ошибка
# деления на ноль
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

def test_typeerror():
    with pytest.raises(TypeError):
        division(10, "wfdsdf")