from random import randint

RIGHT = True
LEFT = False

def getRandDirection():
  # Could be implemented with just an implicit conversion, but it looks nicer this way
    if randint(0, 1) == 1:
        return RIGHT
    return LEFT
    