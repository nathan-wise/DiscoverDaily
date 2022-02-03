import random

class RandomGenerator:

    def __init__(self) -> None:
        pass

    def getRandomCharacter(self):
        characters = ["a", "b", "c", "d", "e",
                     "f", "g", "h", "i", "j", 
                     "k", "l", "m", "n", "o", "p", 
                     "q", "r", "s", "t", "u", "v", 
                     "w", "x", "y", "z"]
        randomNumber = random.randint(0, 25)
        return characters[randomNumber]

    def getRandomOffset(self):
        return random.randint(0, 500)

    def getRandomTrack(self):
        return random.randint(0,5)
