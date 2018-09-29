# Class items contains two fields:
#   - Name is the uppercase letter denoting the item
#   - Weight is the mass of the item, an integer


class Item(object):
    # Constructor for Item class
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.bag = None
        self.is_assigned = False
