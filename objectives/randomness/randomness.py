import random


for i in range(0, 3):
    random_index = random.randint(0, 4)


def fisher_yates_shuffle(l):
    for i in range(0, len(l)-2):
        random_index = random.randint(i, len(l)-1)
        l[random_index], l[i] = l[i], l[random_index]
