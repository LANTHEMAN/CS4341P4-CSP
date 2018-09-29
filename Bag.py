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
        self.bag_fit_limit_reached = False

    # Checks if the current capacity isn't met
    def sum_item_weights(self, item):
        if not self.contains:
            weight = 0;
            return weight
        elif self.contains is not None:
            for i in self.contains:
                weight = item.weight + i.weight
                return weight

    def can_add_item(self, item):
        if (self.current_load + item.weight) <= self.capacity:
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
            self.current_load += item.weight
            return True
        else:
            return False

    # Removes an item to a bag
    def remove_item(self, item):
        self.contains.remove(item)
        self.current_load -= item.weight










