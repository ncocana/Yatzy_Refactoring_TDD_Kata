class Yatzy:

    def __init__(self, *dice):

        # Creates a list with the dice given.
        # Example: [1, 2, 3, 4, 5]
        
        self.dice = list(dice)
    
    @staticmethod
    def chance(*dice):

        score = 0

        # Sums each element (die) in the list (dice)
        # and saves the result in the variable 'score'.
        for die in dice:
            score += die
            
        return score

    @staticmethod
    def yatzy(*dice):

        # Example: dice = (1,1,1,1,1)
        # dice.count(dice[0]) gets the value of the first value in the list and counts how many time it appears on the list.
        # If it doesn't appears 5 times, it will return '0'. Else, it will return '50'.
        # In this example, the command gets the first element (1) and counts how many times it appears on the list (5).
        # If there's a number different from the first one or less/more than 5 elements on the list, it will return '0'.

        if dice.count(dice[0]) != 5:
            return 0
        
        return 50
    
    @staticmethod
    def ones(*dice):

        # Counts the number of times that the number '1',
        # saved in the variable (constant) ONE,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (1).

        ONE = 1

        return dice.count(ONE) * ONE
    
    @staticmethod
    def twos(*dice):

        # Counts the number of times that the number '2',
        # saved in the variable (constant) TWO,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (2).

        TWO = 2

        return dice.count(TWO) * TWO
    
    @staticmethod
    def threes(*dice):

        # Counts the number of times that the number '3',
        # saved in the variable (constant) THREE,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (3).

        THREE = 3

        return dice.count(THREE) * THREE
    
    def fours(self):

        # Counts the number of times that the number '4',
        # saved in the variable (constant) FOUR,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (4).

        FOUR = 4

        return self.dice.count(FOUR) * FOUR
    
    def fives(self):

        # Counts the number of times that the number '5',
        # saved in the variable (constant) FIVE,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (5).

        FIVE = 5

        return self.dice.count(FIVE) * FIVE
    
    def sixes(self):

        # Counts the number of times that the number '6',
        # saved in the variable (constant) SIXES,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (6).

        SIXES = 6

        return self.dice.count(SIXES) * SIXES
    
    @staticmethod
    def pair(*dice):

        # Saves the value '2' in a variable,
        # referring to the sum of the two highest matching dice.
        PAIR = 2

        # Gets each number in the range of 6 to 1.
        for number in range(6, 0, -1):

            # If the number saved in the variable at the moment
            # appears 2 or more times in the list of dices,
            # return that number multiplied by itself
            # (which is the same as the sum of the two numbers).
            if dice.count(number) >= PAIR:
                return PAIR * number

        # If there are no numbers that appear 2 or more time in the list,
        # return '0'.
        return 0
    
    @staticmethod
    def two_pairs( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0