import pytest
from calculadora import Calculadora

@pytest.fixture
def dados_teste():
    return {
        "a": 10,
        "b": 5
    }

@pytest.fixture
def calculadora():
    return Calculadora()

def test_somar(calculadora, dados_teste):
    assert calculadora.somar(dados_teste["a"], dados_teste["b"]) == 15

def test_subtrair(calculadora, dados_teste):
    assert calculadora.subtrair(dados_teste["a"], dados_teste["b"]) == 5

def test_multiplicar(calculadora, dados_teste):
    assert calculadora.multiplicar(dados_teste["a"], dados_teste["b"]) == 50

def test_dividir(calculadora, dados_teste):
    assert calculadora.dividir(dados_teste["a"], dados_teste["b"]) == 2

