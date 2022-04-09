import random
import numpy
import matplotlib.pyplot as plt

weight = {}

strip1 = [6, 7, 8, 5, 5, 3, 3, 4, 1, 4, 2, 2, 1, 1]
strip2 = [3, 3, 1, 2, 2, 6, 7, 8, 3, 2, 5, 4, 4, 1]
strip3 = [1, 3, 6, 7, 8, 5, 3, 4, 2, 2, 1, 1, 2, 1]

symbols = {
    1:2, # 5
    2:5, # 25
    3:10, # 60
    4:60, # 150
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
        #print(i)
        new_strip1 = shift(strips[0], i)
        for j in range(len(strips[0])):
            new_strip2 = shift(strips[1], j)
            for k in range(len(strips[0])):
                new_strip3 = shift(strips[2], k)
                multi = check([new_strip1, new_strip2, new_strip3])
                if multi == 0:
                    weight[(i, j, k)] = 1.0 
                else:
                    weight[(i, j, k)] = 1.0 / numpy.log(numpy.log(multi))
    
    scale = len(weight.keys()) / sum(weight.values())
    #print(scale)
    for tuple in weight.keys():
        weight[tuple] *= scale 
           
def simulateRTPNumOfIterations(numOfIterations, color):
    global strip1, strip2, strip3
    startingCapital = 100 * numOfIterations
    currentCapital = startingCapital
    # average = 100

    ys = []

    for n in range(numOfIterations):
        i, j, k = selectShifts()
        multi = check([shift(strip1,i), shift(strip2, j), shift(strip3, k)])
        currentCapital -= 100
        currentCapital += 100 * multi  
        currentRTP = 100.0 * currentCapital / startingCapital
        ys.append(currentRTP)

    print(100.0 * currentCapital / startingCapital, color)

    plt.plot(range(numOfIterations), ys, color=color)
    

def simulateRTP():
    global strip1, strip2, strip3, weight
    startingCapital = sum(weight.values())
    currentCapital = 0

    for tuple, prob in weight.items():
        i, j, k = tuple
        multi = check([shift(strip1,i), shift(strip2, j), shift(strip3, k)])
        currentCapital += multi * prob

    print(100.0 * currentCapital / startingCapital)

generateWeights([strip1, strip2, strip3])

if __name__ == "__main__":
    simulateRTP()
    colors = ["red", "blue", "green", "yellow", "pink", "brown", "black"]

    for color in colors:
        simulateRTPNumOfIterations(100000, color)
    plt.show()