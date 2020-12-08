import LossFunction
import random
import math


def randomMethod(dom, func):
    best = math.inf
    current = 0
    for i in range(1000):
        rand = [random.randint(dom[i][0], dom[i][1]) for i in range(len(dom))]
        cost = func(rand)
        if cost < best:
            best = cost
            current = rand
    return current


if __name__ == "__main__":
    # no optimization
    domain = [(0, 9)] * (len(LossFunction.people) * 2)
    r = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
    # optimization
    s = randomMethod(domain, LossFunction.totalCost)
    print(s)
    LossFunction.schedule(s)
    print("Total Cost (no optimization):    ", LossFunction.totalCost(r))
    print("Total Cost (with optimization):  ", LossFunction.totalCost(s))
