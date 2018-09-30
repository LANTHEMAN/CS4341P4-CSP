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
        self.current_load_percentage = 0
        self.contains = []
        self.name = name
        self.bag_fit_limit_reached = False

    def can_add_item(self, item):
        if (self.current_load + item.weight) <= self.capacity:
            return True
        else:
            return False

    # Adds an item to a bag
    def add_item(self, item):
        if self.can_add_item(item):
            self.contains.append(item)
            self.current_load += item.weight
            self.current_load_percentage = self.current_load / self.capacity
            item.bag = self
            return True
        else:
            return False

    # Removes an item to a bag
    def remove_item(self, item):
        self.contains.remove(item)
        self.current_load -= item.weight
        self.current_load_percentage = self.current_load / self.capacity
        item.bag = None










