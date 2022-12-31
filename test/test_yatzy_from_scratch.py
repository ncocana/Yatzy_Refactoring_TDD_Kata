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

@pytest.mark.testYatzy
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

'''
Ones, Twos, Threes, Fours, Fives, Sixes:
The player scores the sum of the dice that reads one, two, three, four, five, or six, respectively.
'''

@pytest.mark.testOnes
def test_ones():
    '''
    The player scores the sum of the dice that reads one
    '''
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)

@pytest.mark.testTwos
def test_twos():
    '''
    The player scores the sum of the dice that reads two
    '''
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)

@pytest.mark.testThrees
def test_threes():
    '''
    The player scores the sum of the dice that reads three
    '''
    assert 0 == Yatzy.threes(1, 1, 1, 1, 1)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)

@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(4, 5, 6, 6, 5)
    return tirada


@pytest.mark.testFours
def test_fours(inyector):
    '''
    The player scores the sum of the dice that reads four
    '''
    # Es necesario un objeto ya creado
    valorEsperado = 4
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado == inyector.fours()

@pytest.mark.testFives
def test_fives(inyector):
    '''
    The player scores the sum of the dice that reads five
    '''
    valorEsperado = 10
    assert valorEsperado == inyector.fives()


@pytest.mark.testSixs
def test_sixes(inyector):
    '''
    The player scores the sum of the dice that reads six
    '''
    valorEsperado = 12
    assert valorEsperado == inyector.sixes()

