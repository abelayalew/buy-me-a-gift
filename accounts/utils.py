from string import digits
import random


def random_otp(length=6):
    return ''.join(random.choice(digits) for _ in range(length))
