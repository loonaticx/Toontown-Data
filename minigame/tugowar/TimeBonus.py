"""
Resources: Anesdora
toontown/minigame/DistributedTugOfWarGameAI
toontown/minigame/TugOfWarGameGlobals
"""

import matplotlib.pyplot as plt

# Constants
TIME_BONUS_RANGE = 3.0  # initial value of timeBonus
TIME_BONUS_MIN = 2
GAME_DURATION = 40.0  # Game is 40 seconds long

deltaBonus = []
finalBonus = []
time = []

## During the Game ##
# This function will run once every second until the game ends.
def calcTimeBonus():
    timeBonus = TIME_BONUS_RANGE
    for i in range(0, int(GAME_DURATION + 1)):  # n-1
        time.append(i)
        delta = TIME_BONUS_RANGE/GAME_DURATION
        timeBonus = timeBonus - delta
        deltaBonus.append(timeBonus)
        timeBonusFinal = TIME_BONUS_MIN + int(timeBonus + .5)
        finalBonus.append(timeBonusFinal)
calcTimeBonus()

plt.xlabel("b = Time Bonus Jellybeans")
plt.ylabel("t = Duration of Minigame (seconds)")
plt.title("Bonus Jellybean Amount during Tug-Of-War Minigame")

plt.plot(deltaBonus, time, label='Delta')
plt.scatter(deltaBonus, time, label='Delta')
plt.plot(finalBonus, time, label='Final')
plt.scatter(finalBonus, time, label='Final')
plt.show()
