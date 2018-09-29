import Items
import Bag
import sys

class Input(object):
    # read the whole file and create object
    def __init__(self,input_file_name):
        with open(input_file_name) as file:
            data = file.readlines()
        self.input_file = data
        self.list_of_items = []
        self.list_of_bags = []
        self.low_limit = 0
        self.upper_limit = sys.maxsize
        self.unary_inclusive = {}
        self.unary_exclusive = {}
        self.binary_equal = []
        self.binary_not_equal = []
        self.mutual_inclusive = []

    def InterpretFile(self):
        separator_counter = 0
        for i in self.input_file:
            if i[0] == '#':
                separator_counter += 1
            else:
                if separator_counter == 1:
                    self.AddItem(i)
                elif separator_counter == 2:
                    self.AddBag(i)
                elif separator_counter == 3:
                    self.AddFittingLimit(i)
                elif separator_counter == 4:
                    self.AddUnaryInclusive(i)
                elif separator_counter == 5:
                    self.AddUnaryExclusive(i)
                elif separator_counter == 6:
                    self.AddBinaryEqual(i)
                elif separator_counter == 7:
                    self.AddBinaryNotEqual(i)
                elif separator_counter == 8:
                    self.AddMutualInclusive(i)

        print(
            self.list_of_items,
            self.list_of_bags)
            # self.low_limit,
            # self.upper_limit,
            # self.unary_inclusive,
            # self.unary_exclusive,
            # self.binary_equal,
            # self.binary_not_equal,
            # self.mutual_inclusive)

    def AddItem(self,line):
        item_name, weight = line.split()
        self.list_of_items.append(Items.Item(item_name,int(weight)))

    def AddBag(self,line):
        bag_name, capacity = line.split()
        self.list_of_bags.append(Bag.Bag(int(capacity),0,bag_name))

    def AddFittingLimit(self,line):
        low_limit, upper_limit = line.split()
        self.low_limit = int(low_limit)
        self.upper_limit = int(upper_limit)

    def AddUnaryInclusive(self,line):
        ui = line.split()
        item_name = ui[0]
        bags_name = ui[1:]
        item = self.FindItem(self.list_of_items,item_name)
        bags = []
        for i in bags_name:
            bags.append(self.FindBag(self.list_of_bags,i))
        self.unary_inclusive[item] = bags

    def AddUnaryExclusive(self,line):
        ue = line.split()
        item_name = ue[0]
        bags_name = ue[1:]
        item = self.FindItem(self.list_of_items,item_name)
        bags = []
        for i in bags_name:
            bags.append(self.FindBag(self.list_of_bags,i))
        self.unary_exclusive[item] = bags

    def AddBinaryEqual(self,line):
        item_name1, item_name2 = line.split()
        item1 = self.FindItem(self.list_of_items,item_name1)
        item2 = self.FindItem(self.list_of_items, item_name2)
        self.binary_equal.append((item1,item2))

    def AddBinaryNotEqual(self,line):
        item_name1, item_name2 = line.split()
        item1 = self.FindItem(self.list_of_items,item_name1)
        item2 = self.FindItem(self.list_of_items, item_name2)
        self.binary_not_equal.append((item1,item2))

    def AddMutualInclusive(self,line):
        item_name1, item_name2, bag_name1, bag_name2 = line.split()
        item1 = self.FindItem(self.list_of_items, item_name1)
        item2 = self.FindItem(self.list_of_items, item_name2)
        bag1 = self.FindBag(self.list_of_bags,bag_name1)
        bag2 = self.FindBag(self.list_of_bags, bag_name2)
        self.mutual_inclusive.append(((item1,item2),(bag1,bag2)))

    def FindItem(self,list,name):
        for i in list:
            if i.name == name:
                return i

    def FindBag(self,list,name):
        for i in list:
            if i.name == name:
                return i
