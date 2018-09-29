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


def check_upper_bag_limit(parameter, bag_index):
    if len(parameter.list_of_bags[bag_index].contains) + 1 <= parameter.upper_limit:
        return True
    else:
        return False


def check_unary_inclusive(next_item, parameter, bag_index):
    if next_item in parameter.unary_inclusive:
        if parameter.list_of_bags[bag_index] in parameter.unary_inclusive[next_item]:
            return True
        else:
            #print("The bag you tried to add is not in unary inclusive list")
            return False
    else:
        return True


def check_unary_exclusive(next_item, parameter, bag_index):
    if next_item in parameter.unary_exclusive:
        if parameter.list_of_bags[bag_index] not in parameter.unary_exclusive[next_item]:
            return True
        else:
            #print("The bag you tried to add is in unary exclusive list")
            return False
    return True


def check_binary_equal(next_item,parameter,bag_index):
    for i in parameter.binary_equal:
        if next_item in i:
            for j in i:
                if not j == next_item:
                    if j in parameter.list_of_items:
                        return True
                    elif j.bag == parameter.list_of_bags[bag_index]:
                        return True
                    else:
                        return False

    return True


def check_binary_not_equal(next_item,parameter,bag_index):
    for i in parameter.binary_not_equal:
        if next_item in i:
            for j in i:
                if not j == next_item:
                    if j in parameter.list_of_items:
                        return True
                    elif not j.bag == parameter.list_of_bags[bag_index]:
                        return True
                    else:
                        return False
    return True


def check_mutual_inclusive(next_item,parameter,bag_index):
    for i in parameter.mutual_inclusive:
        # check if in item list
        if next_item in i[0]:
            # check if in bag list
            if parameter.list_of_bags[bag_index] in i[1]:
                for k in i[1]:
                    if not k == parameter.list_of_bags[bag_index]:
                        current_bag = k
                for j in i[0]:
                    if not j == next_item:
                        if j in parameter.list_of_items:
                            return True
                        elif j.bag == k:
                            return True
                        else:
                            return False
    return True


def valid_assignment(next_item,parameter,bag_index):
    if(
            check_upper_bag_limit(parameter, bag_index) and
            check_unary_inclusive(next_item,parameter,bag_index) and
            check_unary_exclusive(next_item, parameter, bag_index) and
            check_binary_equal(next_item, parameter, bag_index) and
            check_binary_not_equal(next_item, parameter, bag_index) and
            check_mutual_inclusive(next_item, parameter, bag_index)):
        return True
    else:
        return False


def select_unassigned_variable(parameter):
    return parameter.list_of_items.pop(0)


def back_tracking(parameter):
    if finished(parameter):
        return True

    if parameter.list_of_items:
        next_item = select_unassigned_variable(parameter)
    else:
        return False

    for i in range(len(parameter.list_of_bags)):
        if valid_assignment(next_item, parameter,i):
            added = parameter.list_of_bags[i].add_item(next_item)
            if added:
                outcome = back_tracking(parameter)
                if outcome:
                    return True
                else:
                    parameter.list_of_bags[i].remove_item(next_item)
    parameter.list_of_items.append(next_item)
    return False


def finished(parameter):
    for a in parameter.list_of_bags:
        if 0.9 > a.current_load_percentage:
            return False
    if len(parameter.list_of_items) == 0:
        return True
    else:
        return False


param = InputReader.Input('input23.txt')
param.InterpretFile()
result = back_tracking(param)
print('result: ', result)
for i in param.list_of_bags:
    print('bag name: ',i.name)
    for j in i.contains:
        print('item name: ', j.name)
#

#
#
# # Item cannot be in this bag
# def unary_exclusion_constraint(item, bag):
#     if isinstance(item, Items.Item) and isinstance(bag, list(Bag.Bag)):
#         return True
#     else:
#         return False
#
#
# # Both items need to be in the same bag
# def binary_equals_constraint(item_one, item_two):
#     if isinstance(item_one, Items.Item) and isinstance(item_two, Items.Item):
#             return True
#     pass
#
#
# # These items cannot go in the same Bag
# def binary_does_not_equal_constraint(item_1, item_2, bags_in_question):
#     # if isinstance(item_1, Items.Item) and isinstance(item_2, Items.Item) and isinstance(bags_in_question, Bag.Bag):
#     #     if()
#      pass
#
#
# def binary_mutual_in(item_1, item_2, bag_1, bag_2):
#     if isinstance(item_1, Items.Item) and isinstance(item_2, Items.Item) and isinstance(bag_1, Bag.Bag) and isinstance(bag_2, Bag.Bag):
#         if item_1 in bag_1.contains:
#             bag_2.add_item(item_2)
#         elif item_1 in bag_2.contains:
#             bag_1.add_item(item_2)
#         elif item_2 in bag_1.contains:
#             bag_2.add_item(item_1)
#         elif item_2 in bag_1.contains:
#             bag_2.add_item(item_1)
#         else:
#             bag_1.add_item(item_1)
#             bag_2.add_item(item_2)
#     pass
#
#
#
#
# # unary_inclusion_constraint(item1,bag1)
#
# # print(bag1.contains[0], item1)
# unary_inclusion_constraint(r.unary_inclusive)


