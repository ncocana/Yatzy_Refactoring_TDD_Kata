from enum import Enum, unique

# A class decorator specifically for enumerations.
# It searches an enumeration’s __members__ (values), gathering any aliases it finds.
# If any are found, ValueError is raised with the details.
@unique
class Numbers(Enum):

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    # When this method is called, the class is passed as the first argument
    # instead of the instance of that class (as we normally do with methods).
    # This means that you can use the class and its properties inside
    # that method without having to instantiate the class.
    @classmethod
    def values(cls):
        return [number._value_ for number in Numbers.__members__.values()]
    
    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())