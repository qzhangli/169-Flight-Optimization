# destination, 25 people and 25 corresponding outbound airports
destination = "LAX"
airports = ['ATL', 'ORD', 'DFW', 'DEN', 'JFK',
            'SFO', 'SEA', 'LAS', 'MCO', 'EWR',
            'CLT', 'PHX', 'IAH', 'MIA', 'BOS',
            'MSP', 'FLL', 'DTW', 'PHL', 'LGA',
            'BWI', 'SLC', 'SAN', 'IAD', 'DCA']
people = ["Susan", "Barbara", "Richard", "Jennifer", "Noah",
          "David", "Robert", "William", "Michael", "Joseph",
          "Dylan", "Thomas", "Jessica", "Nathan", "Matthew",
          "Nancy", "Daniel", "Karen", "Brandon", "Jonathan",
          "James", "Jeremy", "Vincent", "Mary", "Elizabeth"]

# load flight data
raw = open("flights.txt", "r")
flights = raw.readlines()


def schedule(r):
    for i in range(int(len(r) / 2)):
        name = people[i]
        origin = airports[i]
        l1 = getFlightInfo(origin, destination, r[i * 2])
        l2 = getFlightInfo(destination, origin, r[i * 2 + 1])
        result1 = l1.split(",")[-4:]
        result2 = l2.split(",")[-4:]
        print('%10s %10s %5s-%5s $%3s $%3s %5s-%5s $%3s $%3s' % (
            name, origin, result1[0], result1[1], result1[2], result1[3][0],
            result2[0], result2[1], result2[2], result2[3][0]))


def getFlightInfo(departure, arrive, index):
    outboundFlights = []
    for f in flights:
        start1 = departure + "," + arrive
        if f.startswith(start1):
            outboundFlights.append(f)
    return outboundFlights[index]


def getMinutes(start, end):
    t1 = start.split(":")
    t2 = end.split(":")
    total = (int(t2[0]) * 60 + int(t2[1])) - (int(t1[0]) * 60 + int(t1[1]))
    assert total > 0, "Logic Error: departure before arrive"
    return total


# define cost function
def totalCost(solution):
    """
    for every minute each person staying on the airplane, the opportunity cost would be 1.
    the ticket price for each person's flight will be counted and added to the total cost.
    the airline meal rating from 0 - 5 reflects the satisfaction, choose the flights with
    high rating can increase the satisfaction and reduce the total cost by (10 * ratings).

    input:  the indexes of the flights that each person is gonna take. 2 for each person.
    return: the total cost with all the factors considered(ticket, total time, and meal)
    """
    ticket = 0
    time = 0
    meal = 0
    for i in range(int(len(solution) / 2)):
        flight_outbound_index = solution[i * 2]
        flight_inbound_index = solution[i * 2 + 1]
        departureCity = airports[i]
        arrive = destination
        l1 = getFlightInfo(departureCity, arrive, flight_outbound_index)
        l2 = getFlightInfo(arrive, departureCity, flight_inbound_index)
        # print(l1)     # outbound flight info
        # print(l2)     # inbound flight info
        l1 = l1.split(",")
        l2 = l2.split(",")
        ticket += int(l1[-2])
        ticket += int(l2[-2])
        time += getMinutes(l1[-4], l1[-3])
        time += getMinutes(l2[-4], l2[-3])
        meal += (10 * int(l1[-1]))
        meal += (10 * int(l2[-1]))
    cost = ticket + time - meal
    return cost


if __name__ == "__main__":
    solution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    totalCost(solution)
