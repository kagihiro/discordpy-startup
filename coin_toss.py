import random

def toss():
    flip = random.randint(0, 1)
    if (flip == 0):
        return ('裏')
    else:
        return ('表')
