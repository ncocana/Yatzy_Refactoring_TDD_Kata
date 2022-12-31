import pytest
from src.yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.

@pytest.mark.testChance
def test_chance():
    '''
    Chance:
    The player scores the sum of all dice, no matter what they read.
    '''

    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

def test_yatzy():
    '''
    Yatzy:
    If all dice have the same number, the player scores 50 points.
    '''
    
    # dice significa "dados" pero exige un unico argumento
    # => interfaz abstraccion del metodo no es coherente
    # con el resto de metodos
    # El codigo para iterar sobre dice es muy complejo
    # El algoritmo para averiguar si todos los dados son iguales
    # es muy complejo
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 2, 1)

@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada


@pytest.mark.testFours
def test_fours(inyector):
    # Es necesario un objeto ya creado
    valorEsperado = 4
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado == inyector.fours()