#Program to find out how often a streak of six heads or six tails comes up in a randomly generated list of heads and tails.

import random
hStreak = 0
tStreak = 0
numberOfStreaks = 0
results = []
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    experimentNumber = random.randint(0, 1)
    results.append(experimentNumber)

    # Code that checks if there is a streak of 6 heads or tails in a row.

index = 0
for i in results:
    test = results[index:index + 6]
    if test == [1, 1, 1, 1, 1, 1]:
        hStreak = hStreak + 1
    if test == [0, 0, 0, 0, 0, 0]:
        tStreak = tStreak + 1
    index = index + 1

numberOfStreaks = tStreak + hStreak

print('Chance of streak: %s%%' % (numberOfStreaks / 100))