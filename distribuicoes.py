#distribuições: aleatória exponencial e a probabilidade de evaporar

import random
import math


def evapQ(c):
    x=random.random()
    if x<1/math.log(c):
        return True
    else:
        return False


def tempoexp(m):
    x=random.random()
    return -m*math.log(x)