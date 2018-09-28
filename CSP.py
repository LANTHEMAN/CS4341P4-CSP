import Bag
import Items
# function BACKTRACKING-SEARCH(csp) returns a solution, or failure
# return BACKTRACK({ }, csp)
# function BACKTRACK(assignment, csp) returns a solution, or failure
# if assignment is complete then return assignment
# var ← SELECT-UNASSIGNED-VARIABLE(csp)
# for each value in ORDER-DOMAIN-VALUES(var , assignment, csp) do
# if value is consistent with assignment then
# add {var = value} to assignment
# inferences ← INFERENCE(csp, var , value)
# if inferences = failure then
# add inferences to assignment
# result ← BACKTRACK(assignment, csp)
# if result = failure then
# return result
# remove {var = value} and inferences from assignment
# return failure
import Items
import Bag
import InputReader
item1 = Items.Item("A", 2)
item2 = Items.Item("C", 5)
# bag1.add_item(item1)
# bag1.add_item(item2)
r = InputReader.Input('input25.txt')
r.InterpretFile()


def backtrack_search(assignment):

    pass


def valid_assignment(assignment):
    pass


def select_unassigned_variable(csp):
    pass


def back_tracking(assignment, CSP):
    CSP = []
    if valid_assignment(assignment):
        return assignment

    #remaining_item = selectNextItem()


# Put item in this bag
def unary_inclusion_constraint(dic):
    if isinstance(dic, dict):
        for i in dic.values():
            for j in i:
                print(type(j))
                if isinstance(j, Bag.Bag):
                    print(type(dic.keys()))
                    #j.add_item(dic.keys())
                    #print(j.contains[0])
                    break
        # if bag.can_add_item(item):
        #     bag.add_item(item)
        #     item.is_assigned = True
        return True
    else:
        print("You are tyring to add to an already full bag")
        return -1


# Item cannot be in this bag
def unary_exclusion_constraint(item, bag):
    if isinstance(item, Items.Item) and isinstance(bag, list(Bag.Bag)):
        return True
    else:
        return False


# Both items need to be in the same bag
def binary_equals_constraint(item_one, item_two):
    if isinstance(item_one, Items.Item) and isinstance(item_two, Items.Item):
            return True
    pass


# These items cannot go in the same Bag
def binary_does_not_equal_constraint(item_1, item_2, bags_in_question):
    # if isinstance(item_1, Items.Item) and isinstance(item_2, Items.Item) and isinstance(bags_in_question, Bag.Bag):
    #     if()
     pass


def binary_mutual_in(item_1, item_2, bag_1, bag_2):
    if isinstance(item_1, Items.Item) and isinstance(item_2, Items.Item) and isinstance(bag_1, Bag.Bag) and isinstance(bag_2, Bag.Bag):
        if item_1 in bag_1.contains:
            bag_2.add_item(item_2)
        elif item_1 in bag_2.contains:
            bag_1.add_item(item_2)
        elif item_2 in bag_1.contains:
            bag_2.add_item(item_1)
        elif item_2 in bag_1.contains:
            bag_2.add_item(item_1)
        else:
            bag_1.add_item(item_1)
            bag_2.add_item(item_2)
    pass




# unary_inclusion_constraint(item1,bag1)

# print(bag1.contains[0], item1)
unary_inclusion_constraint(r.unary_inclusive)


