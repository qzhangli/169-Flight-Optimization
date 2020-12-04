from random import randrange

# destination and 25 outbound airports
destination = "LAX"
airports = ['ATL', 'ORD', 'DFW', 'DEN', 'JFK', 'SFO', 'SEA', 'LAS', 'MCO', 'EWR', 'CLT', 'PHX', 'IAH',
            'MIA', 'BOS', 'MSP', 'FLL', 'DTW', 'PHL', 'LGA', 'BWI', 'SLC', 'SAN', 'IAD', 'DCA']


def getTimePair():
    while True:
        m = str(randrange(60))
        if len(m) == 1:
            m = "0" + m
        outboundTime = str(randrange(1, 22)) + ":" + m

        temp1 = int(outboundTime.split(":")[0])
        temp2 = temp1 + randrange(1, 7)
        m2 = str(randrange(60))
        if len(m2) == 1:
            m2 = "0" + m2
        if temp2 < 24:
            inboundTime = str(temp2) + ":" + m2
            return outboundTime + "," + inboundTime


def generate(num):
    for airport in airports:
        x1 = []
        for _ in range(num):
            l1 = destination + "," + airport + "," + getTimePair() + "," + str(randrange(130, 600)) + "," + str(
                randrange(6))
            x1.append(l1)
        x1.sort(key=lambda i: int(str(i.split(",")[2]).split(":")[0] + str(i.split(",")[2]).split(":")[1]))
        x2 = []
        for _ in range(num):
            l2 = airport + "," + destination + "," + getTimePair() + "," + str(randrange(130, 600)) + "," + str(
                randrange(6))
            x2.append(l2)
        x2.sort(key=lambda i: int(str(i.split(",")[2]).split(":")[0] + str(i.split(",")[2]).split(":")[1]))
        for i in range(num):
            print(x1[i])
            print(x2[i])
