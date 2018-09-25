# Bag class
# Name (lower case letter)
# Capacity (How much weight it can hold)
# Load (% filled), needs to be between 90-100%
# Contains (list of items in the bag)
# Function to put items in the bag
# Function to remove items from the bag


class Bag:

    # The class constructor for the bag class containing the capacity, current_load, contains, and the name attributes
    def __init__(self, capacity=0, current_load=0, contains=0, name=""):
        self.capacity = capacity
        self.current_load = current_load
        self.contains = []
        self.name = name

    # Checks if the current capacity isn't met
    def can_add_item(self):
        if self.current_load <= 1:
            return True
        else:
            return False

    # Calculates the current load of the
    def calculate_current(self):
        return len(self.contains) / self.capacity

    # Adds an item to a bag
    def add_item(self, item):
        if self.can_add_item():
            self.contains.append(item)
            self.calculate_current()
        else:
            print("The threshold for this Bag has been met, you cannot add anymore items.")
            # For now we'll print out that we cannot handle anymore items






