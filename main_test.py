import pytest
import math
import sympy
from your_module import simpson, rectangle, trapezoid, f  # Замените `your_module` на имя вашего файла

# Примерные значения для интегрирования функции sin(x) от 0 до π
EXACT_VALUE = 2  # Интеграл от sin(x) от 0 до π равен 2

def test_simpson():
    result = simpson(0, math.pi, 100, f)
    assert pytest.approx(result, rel=1e-2) == EXACT_VALUE

def test_rectangle():
    result = rectangle(0, math.pi, 100, f)
    assert pytest.approx(result, rel=1e-2) == EXACT_VALUE

def test_trapezoid():
    result = trapezoid(0, math.pi, 100, f)
    assert pytest.approx(result, rel=1e-2) == EXACT_VALUE

def test_function_f():
    # Проверим значения функции f(x) = sin(x) в нескольких точках
    assert f(0) == 0
    assert f(math.pi/2) == 1
    assert f(math.pi) == 0
    assert f(3*math.pi/2) == -1
    assert f(2*math.pi) == 0

# Проверка на негативное значение для n (количество шагов)
def test_invalid_n():
    with pytest.raises(ZeroDivisionError):
        simpson(0, math.pi, 0, f)
    with pytest.raises(ZeroDivisionError):
        rectangle(0, math.pi, 0, f)
    with pytest.raises(ZeroDivisionError):
        trapezoid(0, math.pi, 0, f)

# Дополнительные тесты можно добавить по мере необходимости.

