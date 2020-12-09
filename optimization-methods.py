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


def annealingMethod(dom, func, T=1000.0, t=0.98, alpha=1e-2, step=1, k_max=1e3):
    ini = [int(random.randint(dom[i][0], dom[i][1])) for i in range(len(dom))]
    k = 1
    while T > alpha:
        k += 1
        i = random.randint(0, len(dom) - 1)
        delta = random.randint(-step, step)
        new = ini[:i] + [ini[i] + delta] + ini[i+1:]
        lower = dom[i][0]
        upper = dom[i][1]
        if new[i] < lower:
            new[i] = lower
        elif new[i] > upper:
            new[i] = upper
        y = func(ini)
        yp = func(new)
        p = pow(math.e, (- y - yp) / T)
        if yp < y or random.random() < p:
            ini = new
        T = T * t
        if k >= k_max:
            break
    return ini


if __name__ == "__main__":
    domain = [(0, 9)] * (len(LossFunction.people) * 2)      # no optimization
    n = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
    r = randomMethod(domain, LossFunction.totalCost)        # random optimization
    s = annealingMethod(domain, LossFunction.totalCost)     # annealing optimization
    # LossFunction.schedule(r)
    # LossFunction.schedule(s)
    print("Total Cost (no optimization):    ", LossFunction.totalCost(n))
    print("Total Cost (with random optimization):  ", LossFunction.totalCost(r))
    print("Total Cost (with simulate annealing optimization):  ", LossFunction.totalCost(s))
