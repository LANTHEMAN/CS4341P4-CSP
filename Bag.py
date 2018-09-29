# Bag class
# Name (lower case letter)
# Capacity (How much weight it can hold)
# Load (% filled), needs to be between 90-100%
# Contains (list of items in the bag)
# Function to put items in the bag
# Function to remove items from the bag

import Items


class Bag(object):

    # The class constructor for the bag class containing the capacity, current_load, contains, and the name attributes
    def __init__(self, capacity, current_load, name):
        self.capacity = capacity
        self.current_load = current_load
        self.contains = []
        self.name = name

    # Checks if the current capacity isn't met
    def sum_item_weights(self, item):
        weight = 0
        for i in self.contains:
            weight += i.weight
        return weight

    def can_add_item(self, item):
        if self.current_load <= 1 and self.capacity != 0:
            current_item_weight = self.sum_item_weights(item)
            if current_item_weight <= self.capacity:
                self.calculate_current(current_item_weight)
                return True
        else:
            return False

    # Calculates the current load of the
    def calculate_current(self, current_item_weight):

        self.current_load = current_item_weight / self.capacity

    # Adds an item to a bag
    def add_item(self, item):
        if self.can_add_item(item):
            self.contains.append(item)
        else:
            return -1








