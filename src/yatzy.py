class Yatzy:

    def __init__(self, *dice):

        # Creates a list with the dice given.
        # Example: [1, 2, 3, 4, 5]
        
        self.dice = list(dice)
    
    @staticmethod
    def chance(*dice):

        # Returns the sum of each element (die) in the list (dice).
        return sum(dice)

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

        # If there are no numbers that appear 2 or more times in the list,
        # return '0'.
        return 0
    
    @staticmethod
    def two_pairs(*dice):
        PAIR = 2
        pairs = 0
        score = 0
        number = 1

        # As long as 'pairs' is less than '2',
        # and 'number' less or equal to '6'...
        while pairs < 2 and number <= 6:

            # If the count of a given number is greater or equal to '2'...
            '''
            (
               e.g. 1:
               dice = (1,3,6,3,1)
               dice.count(1) returns '2', because there are two '1' in dice list.
               Enters the if contidition.

               e.g. 2:
               dice = (1,2,2,2,1)
               dice.count(2) returns '3', because there are three '2' in dice list.
               So even though it can be considered three of a kind,
               it can also be considered a pair because there are still at least
               two numbers with the same value. Therefore, it's allowed to enter the
               if condition.
            )
            '''
            if dice.count(number) >= 2:

                # Enters the if condition, which means there's a pair of the given number.
                # Adds the pair founded to the counter 'pairs'.
                pairs += 1

                # Adds the sum of the pair to the counter 'score'.
                score += PAIR * number
            
            #Sums '1' to 'number' to continue iterating the while loop.
            number += 1
        
        # When the counter 'pairs' is equal to '2',
        # returns the final score.
        if pairs == 2:
            return score
        
        # Only one pair or none were found, returns '0'.
        else:
            return 0
    
    @staticmethod
    def three_of_a_kind(*dice):

        # Saves the value '3' in a variable,
        # referring to the sum of three dice with the same number.
        THREE = 3

        # Gets each number in the range of 6 to 1.
        for number in range(6, 0, -1):

            # If the number saved in the variable at the moment
            # appears 3 or more times in the list of dices,
            # return that number multiplied by itself
            # (which is the same as the sum of the two numbers).
            if dice.count(number) >= THREE:
                return THREE * number
        
        # If there are no numbers that appear 3 or more times in the list,
        # return '0'.
        return 0
    

    @staticmethod
    def four_of_a_kind(*dice):

        # Saves the value '4' in a variable,
        # referring to the sum of three dice with the same number.
        FOUR = 4

        # Gets each number in the range of 6 to 1.
        for number in range(6, 0, -1):

            # If the number saved in the variable at the moment
            # appears 4 or more times in the list of dices,
            # return that number multiplied by itself
            # (which is the same as the sum of the two numbers).
            if dice.count(number) >= FOUR:
                return FOUR * number
        
        # If there are no numbers that appear 4 or more times in the list,
        # return '0'.
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