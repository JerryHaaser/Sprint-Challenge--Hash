#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    ticket_dict = {}

    route = [None] * (len(tickets))

    # Start with ticket with None key
    # Maybe first search for key with None value

    # if ticket.key == None
    for ticket in tickets:
        if ticket.source == "NONE":
            route[0] = ticket.destination
        ticket_dict[ticket.source] = ticket.destination
        # route[0] = ticket
    # check this key for value
    # find key that matches value
    for i in range(1, len(tickets)):
        route[i] = ticket_dict[route[i-1]]
    # repeat until value == None

    # End with ticket with None value

    return route
