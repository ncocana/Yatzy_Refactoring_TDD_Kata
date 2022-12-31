import pytest
from src.yatzy import Yatzy

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
The player scores the sum of the dice that reads
one, two, three, four, five, or six, respectively.
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

@pytest.mark.testPair
def test_pair():
    '''
    Pair:
    The player scores the sum of the two highest matching dice.
    '''
    # El algoritmo del metodo no es optimo, es complicado e ilegible.
    # La abstraccion, el nombre del metodo, no es adecuada
    # puesto que la categoria se llama pair.
    assert 8 == Yatzy.pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.pair(1, 2, 3, 4, 5)

@pytest.mark.testTwoPairs
def test_two_pairs():
    '''
    Two pairs:
    If there are two pairs of dice with the same number,
    the player scores the sum of these dice.
    '''
    # La categoria se llama "two pairs": la abstraccion del metodo
    # no es adecuada.
    # Mantengo notacion snake_case
    # El algoritmo del metodo no es optimo, es complicado e ilegible.

    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pairs(1, 2, 3, 4, 5)

@pytest.mark.testThreeOfAKind
def test_three_of_a_kind():
    '''
    Three of a kind:
    If there are three dice with the same number,
    the player scores the sum of these dice.
    '''
    # El algoritmo del metodo no es optimo, es complicado e ilegible.

    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)

@pytest.mark.testFourOfAKind
def test_four_of_a_kind():
    '''
    Four of a kind:
    If there are four dice with the same number,
    the player scores the sum of these dice.
    '''
    # El algoritmo del metodo no es optimo, es complicado e ilegible.

    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)
    assert 0 == Yatzy.four_of_a_kind(1, 2, 3, 4, 5)

@pytest.mark.testSmallStraight
def test_small_straight():
    '''
    Small straight:
    When placed on "small straight", if the dice reads:
      "1,2,3,4,5",
    the player scores 15 (the sum of all the dice).
    '''
    # El nombre del metodo no es consistente con la nomenclatura snake_case
    # El algoritmo es complicado e ineficiente.

    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.small_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.small_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.small_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.small_straight(1, 2, 3, 4, 6)

@pytest.mark.testLargeStraight
def test_large_straight():
    '''
    Large straight:
    When placed on "large straight", if the dice reads:
      "2,3,4,5,6",
    the player scores 20 (the sum of all the dice).
    '''
    # El nombre del metodo no es consistente con la nomenclatura snake_case
    # El algoritmo es complicado e ineficiente.

    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.large_straight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.large_straight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.large_straight(1, 2, 3, 4, 6)

@pytest.mark.testFullHouse
def test_fullHouse():
    '''
    Full house:
    If the dice are two of a kind and three of a kind,
    the player scores the sum of all the dice.
    '''

    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 0 == Yatzy.fullHouse(2, 2, 3, 3, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 4, 4)