#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Generate a hash equal to the length of the trip
    hashtable = HashTable(length)
    # Generate an array to store the trip in order
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Insert each ticket into the hastable: key="source", value="destination"
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # Find the "NONE" source key and make it the first item in route array
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    # Map the values in the hash table to the route in order according to hint in README
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])


    return route
