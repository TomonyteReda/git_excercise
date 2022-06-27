import numpy as np

print("hello world!")


def get_average(*args):
    return sum(args)/int(len(args))


print(get_average(1, 2, 3, 6))
