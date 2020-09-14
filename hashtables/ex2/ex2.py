class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    hashMap = {}

    for ticket in tickets:
        hashMap[ticket.source] = ticket.destination

    route.append(hashMap['NONE'])
    del hashMap['NONE']

    while len(route) < length:
        curr = route[len(route) - 1]
        route.append(hashMap[curr])

    return route