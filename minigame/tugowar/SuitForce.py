import random

# If we are in a Toon vs. Cog game the AI has
# to determine how hard the suit is pulling, and send
# the suit's offset to the clients.  The suitForces array
# contains (duration, force) pairs.  All the durations should
# at least add up to the length of the game (40 sec).
suitId = 666
#self.suitForces = [(6,4), (2,5.5), (2,7.5), (4,8), (4,7), (8,8), (9,8.5), (4,9)]
suitForces = [(6,4), (2,5), (2,6.5), (3,8.0), (5,6), (8,8), (9,8.5), (4,9)]
suitForceMultiplier = .75
curSuitForce = 0
curSuitForces = []

suitOffset = 0
time = []

# This can be either 1, 2, 3, or 4
numPlayers = 1

curSuitForceInd = 0

for tuple in suitForces:
    if curSuitForceInd < len(suitForces):
        # add or subtract some amount of random force, so the games don't all progress the same way
        randForce = random.random()-.5
        curSuitForce = suitForceMultiplier * numPlayers * (suitForces[curSuitForceInd][1] + randForce)
        curSuitForces.append(round(curSuitForce, 2))
        time.append(suitForces[curSuitForceInd][0])
    curSuitForceInd += 1

print(time)
print(curSuitForces)