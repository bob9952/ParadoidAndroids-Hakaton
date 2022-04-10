import random
from matplotlib.ft2font import BOLD
import numpy
import matplotlib.pyplot as plt

weight = {}

strip1 = [6, 7, 8, 5, 5, 3, 3, 4, 1, 4, 2, 2, 1, 1]
strip2 = [3, 3, 1, 2, 2, 6, 7, 8, 3, 2, 5, 4, 4, 1]
strip3 = [1, 3, 6, 7, 8, 5, 3, 4, 2, 2, 1, 1, 2, 1]

symbols = {
    1:5, # 5
    2:15, # 25
    3:50, # 60
    4:100, # 150
    5:250, # 250
    6:500, # 500
}

def check(strips):
    value = 1
    foundComb = 0

    if strips[0][0] == 6 and strips[1][0] == 6 and strips[2][0] == 6:
        return symbols[6]

    for i in range(3):
        if strips[0][i] == strips[1][i] and strips[1][i] == strips[2][i]:
            if strips[0][i] <= 5:
                foundComb = 1
                value = value * symbols[strips[0][i]]
    return value * foundComb

def printSlot(strips):
    print(str(strips[0][0]) + "|" + str(strips[1][0]) + "|" + str(strips[2][0]))
    print("-----")
    print(str(strips[0][1]) + "|" + str(strips[1][1]) + "|" + str(strips[2][1]))
    print("-----")
    print(str(strips[0][2]) + "|" + str(strips[1][2]) + "|" + str(strips[2][2]))
  
    print(check(strips))

def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]   

def selectShifts():
    global weight
    (i, j, k) = random.choices(list(weight.keys()), weights=weight.values())[0]
    return i, j, k

def generateWeights(strips):
    global weight
    
    for i in range(len(strips[0])):
        new_strip1 = shift(strips[0], i)
        for j in range(len(strips[0])):
            new_strip2 = shift(strips[1], j)
            for k in range(len(strips[0])):
                new_strip3 = shift(strips[2], k)
                multi = check([new_strip1, new_strip2, new_strip3])
                if multi == 0:
                    weight[(i, j, k)] = 1.0 
                else:
                    weight[(i, j, k)] = 1.5 / numpy.log(multi)  # < 1.0
    
    scale = 1.0 / sum(weight.values())
    
    for tuple in weight.keys():
        weight[tuple] *= scale 
           
def simulateRTPNumOfIterations(numOfIterations, color):
    global strip1, strip2, strip3
    startingCapital = 100 * numOfIterations
    currentCapital = startingCapital

    ys = []

    for n in range(numOfIterations):
        i, j, k = selectShifts()
        multi = check([shift(strip1,i), shift(strip2, j), shift(strip3, k)])
        currentCapital -= 100
        currentCapital += 100 * multi  
        currentRTP = 100.0 * currentCapital / startingCapital
        ys.append(currentRTP)

    print(100.0 * currentCapital / startingCapital, color)
    #return 100.0 * currentCapital / startingCapital

    plt.plot(range(numOfIterations), ys, color=color)

def calculateRTP():
    global strip1, strip2, strip3, weight
    currentCapital = 0.0

    for tuple, prob in weight.items():
        i, j, k = tuple
        multi = check([shift(strip1,i), shift(strip2, j), shift(strip3, k)])
        currentCapital += multi * prob

    print(100.0 * currentCapital)

generateWeights([strip1, strip2, strip3])

def tupleToString(bar):
    return f"[${bar[0]}, ${bar[1]})"

if __name__ == "__main__":
    calculateRTP()
    colors = ["red", "blue", "green", "yellow", "pink", "brown", "black"]
    '''
    bars = {
        (60, 70) : 0,
        (70, 75) : 0,
        (75, 80) : 0,
        (80, 85) : 0,
        (85, 90) : 0,
        (90, 95) : 0,
        (95, 100) : 0,
        (100, 105) : 0,
        (105, 110) : 0,
        (110, 115) : 0,
        (115, 125) : 0,
    }

    for n in range(100):
        rtp = simulateRTPNumOfIterations(100000)
        for lower_bound, upper_bound in bars.keys():
            if rtp < upper_bound and rtp >= lower_bound:
                bars[(lower_bound, upper_bound)] += 1

    bar_strings = [tupleToString(bar) for bar in bars.keys()]
    
    plt.bar(bar_strings, bars.values(), width=0.5)
    plt.show()
    '''
    for color in colors:
        simulateRTPNumOfIterations(100000, color)

    plt.xlabel('Number of spins', fontweight="bold", fontsize=14)
    plt.ylabel('Balance percentage', fontweight="bold", fontsize=14)
    plt.show()