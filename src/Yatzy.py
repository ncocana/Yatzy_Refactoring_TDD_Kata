from src.Numbers import Numbers

class Yatzy:

    '''def __init__(self, *dice):

        # Creates a list with the dice given.
        # Example: [1, 2, 3, 4, 5]
        
        self.dice = list(dice)'''
    
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

        ONE = Numbers.ONE.value

        return dice.count(ONE) * ONE
    
    @staticmethod
    def twos(*dice):

        # Counts the number of times that the number '2',
        # saved in the variable (constant) TWO,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (2).

        TWO = Numbers.TWO.value

        return dice.count(TWO) * TWO
    
    @staticmethod
    def threes(*dice):

        # Counts the number of times that the number '3',
        # saved in the variable (constant) THREE,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (3).

        THREE = Numbers.THREE.value

        return dice.count(THREE) * THREE
    
    @staticmethod
    def fours(*dice):

        # Counts the number of times that the number '4',
        # saved in the variable (constant) FOUR,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (4).

        FOUR = Numbers.FOUR.value

        return dice.count(FOUR) * FOUR
    
    @staticmethod
    def fives(*dice):

        # Counts the number of times that the number '5',
        # saved in the variable (constant) FIVE,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (5).

        FIVE = Numbers.FIVE.value

        return dice.count(FIVE) * FIVE
    
    @staticmethod
    def sixes(*dice):

        # Counts the number of times that the number '6',
        # saved in the variable (constant) SIXES,
        # appear in the list of dices,
        # and multiplies the result for the wanted value (6).

        SIXES = Numbers.SIX.value

        return dice.count(SIXES) * SIXES
    
    @staticmethod
    def pair(*dice):

        # Saves the value '2' in a variable,
        # referring to the sum of the two highest matching dice.
        PAIR = 2

        # Calls the class Numbers and get its members values
        # in reversed order (from 6 to 1).
        for number in Numbers.reversedValues():

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

        # Calls the class Numbers and get its members values
        # in reversed order (from 6 to 1).
        for number in Numbers.reversedValues():

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

        # Calls the class Numbers and get its members values
        # in reversed order (from 6 to 1).
        for number in Numbers.reversedValues():

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
    def smallStraight(*dice):

        #For each number in a range from 1 to 5...
        for number in range(1, 6):

            #If the total count of the given number isn't equal to '1'...
            '''
            (
                e.g.:
                dice = (1,2,2,3,4)
                dice.count(2)       Counts the number of times that '2' appear in 'dice', which is '2'.
                                    '2' isn't equal to '1', so it enterns the if condition and returns '0'.
            )
            '''
            if dice.count(number) != 1:

                #Return '0'.
                return 0
        
        # If each number from 1 to 5 appear only 1 time,
        # return the sum of these numbers (1,2,3,4,5),
        # which is '15'.
        return 15
    
    @staticmethod
    def largeStraight(*dice):

        #For each number in a range from 2 to 6...
        for number in range(2, 7):

            #If the total count of the given number isn't equal to '1'...
            '''
            (
                e.g.:
                dice = (2, 2, 3, 4, 5)
                dice.count(2)       Counts the number of times that '2' appear in 'dice', which is '2'.
                                    '2' isn't equal to '1', so it enterns the if condition and returns '0'.
            )
            '''
            if dice.count(number) != 1:

                #Return '0'.
                return 0
        
        # If each number from 2 to 6 appear only 1 time,
        # return the sum of these numbers (2,3,4,5,6),
        # which is '20'.
        return 20
    
    @staticmethod
    def fullHouse(*dice):

        # Calls the functions '__low_pair' and 'three_of_a_kind'.
        # If both functions don't return '0'...
        if Yatzy.__two_of_a_kind(*dice) and Yatzy.three_of_a_kind(*dice):

            # ...return the sum of the scores (results) of both functions.
            return Yatzy.__two_of_a_kind(*dice) + Yatzy.three_of_a_kind(*dice)

        # If one of the functions or both return '0',
        # return '0' here too.
        else:
            return 0

    @staticmethod
    def __two_of_a_kind(*dice):

        # Gets the function 'pair()' and modifies it so it returns
        # the sum of the two highest matching dice but only if there are
        # two same numbers and no more.
        # If there are more than two same numbers (e.g.: (3,3,3,3,1)),
        # it will return '0'.

        PAIR = 2

        for number in Numbers.reversedValues():

            # In 'pair()', this if condition was if the count of the given number
            # was greater or equal to '2'.
            # In this function, it is modified to be equal to '2'.
            if dice.count(number) == PAIR:
                return PAIR * number

        return 0
