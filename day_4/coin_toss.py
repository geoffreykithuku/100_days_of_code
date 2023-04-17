import random

test_seed = input("Enter a seed number ")
random.seed(test_seed)
random_side = random.randint(0,1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")
