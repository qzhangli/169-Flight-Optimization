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


# Mutation: small and random change to an existing solution
def mutate(vec, step=1):
    i = random.randint(0, len(domain) - 1)  # pick an index
    if 9-step >= vec[i] >= 0+step:
        if random.random() < 0.5:
            return vec[0:i] + [vec[i]-step] + vec[i+1:]
        else:
            return vec[0:i] + [vec[i]+step] + vec[i+1:]
    else:
        if vec[i] < 0+step:
            return vec[0:i] + [vec[i]+step] + vec[i+1:]
        else:
            return vec[0:i] + [vec[i]-step] + vec[i+1:]


# Crossover/breeding: taking two best solutions and breed
def crossover(r1, r2):
    i = random.randint(1, len(domain) - 2)  # pick an index that will be used to split
    return r1[0:i] + r2[i:]  # combine


def select_parent(func, origin, parent_size):
    score_list = []
    for v in origin:
        score_list.append((func(v), v))
    score_list.sort()
    parent = [s[1] for s in score_list]
    result = parent[0:parent_size]
    return result


def genetic_opt(domain, func, population=100, mutprob=0.2, survive_rate=0.2, maxiter=50):
    # Build an initial population
    pop = []
    for i in range(population):
        vec = [random.randint(domain[i][0], domain[i][1])
               for i in range(len(domain))]
        pop.append(vec)  # add random solutions to population

    # How many survivors from each generation
    survivor_num = int(survive_rate * population)

    # Main loop
    for i in range(maxiter):
        # select
        parent = select_parent(func, pop, survivor_num)

        # crossover
        while len(parent) < population:
            c1 = random.randint(0, survivor_num-1)  # only choose from survivors
            c2 = random.randint(0, survivor_num-1)
            parent.append(crossover(parent[c1], parent[c2]))
        for i in range(len(parent)):
            if random.random() < mutprob:
                parent[i] = mutate(parent[i])

        # update population
        pop = parent
    return pop[0]


if __name__ == "__main__":
    domain = [(0, 9)] * (len(LossFunction.people) * 2)      # no optimization
    n = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
    r = randomMethod(domain, LossFunction.totalCost)        # random optimization
    s = annealingMethod(domain, LossFunction.totalCost)     # annealing optimization
    g = genetic_opt(domain, LossFunction.totalCost)         # genetic optimization
    # LossFunction.schedule(r)
    # LossFunction.schedule(s)
    # LossFunction.schedule(g)
    print("Total Cost (no optimization):    ", LossFunction.totalCost(n))
    print("Total Cost (with random optimization):  ", LossFunction.totalCost(r))
    print("Total Cost (with simulate annealing optimization):  ", LossFunction.totalCost(s))
    print("Total Cost (with genetic optimization):  ", LossFunction.totalCost(g))
