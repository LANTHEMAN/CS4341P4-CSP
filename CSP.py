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
    # for a in parameter.list_of_bags:
    #     print('bag name: ', a.name)
    #     for b in a.contains:
    #         print('item name: ', b.name)
    for mi in parameter.mutual_inclusive:
        # check if in item list
        if next_item in mi[0]:
            # loop through the item tuple in a single constraint
            for i in mi[0]:
                # get the value already assigned (not the current item)
                if i.bag and (i.bag in mi[1]):
                    for b in mi[1]:
                        if not b == i.bag:
                            if not parameter.list_of_bags[bag_index] == b:
                                # print('next_item: ',next_item.name,' bag[i]: ',parameter.list_of_bags[bag_index].name)
                                # print('false',mi[0][0].name,mi[0][1].name,mi[1][0].name,mi[1][1].name,'\n')
                                return False

                if i == next_item and (parameter.list_of_bags[bag_index] in mi[1]):
                    for d in mi[0]:
                        if (not d == next_item) and d.bag:
                            current_item = d
                            for c in mi[1]:
                                if not c == parameter.list_of_bags[bag_index]:
                                    if not current_item.bag == c:
                                        return False

            # check if in bag list
    #         print(1)
    #         if parameter.list_of_bags[bag_index] in i[1]:
    #             print(2)
    #             for k in i[1]:
    #                 if not k == parameter.list_of_bags[bag_index]:
    #                     the_other_bag = k
    #             for j in i[0]:
    #                 print('lmao')
    #                 if (j not in parameter.list_of_items) and (not j == next_item):
    #                     print('hahha')
    #                     print('j.bag: ',j.bag.name,'the_other: ',the_other_bag.name)
    #                     if not j.bag == the_other_bag:
    #                         print('next_item: ',next_item.name,' bag[i]: ',parameter.list_of_bags[bag_index].name)
    #                         print('false ',i[0][0].name,i[0][1].name,i[1][0].name,i[1][1].name,'\n')
    #                         return False
    #
    #     print('next_item: ', next_item.name, ' bag[i]: ', parameter.list_of_bags[bag_index].name)
    #     print('true ', i[0][0].name, i[0][1].name, i[1][0].name, i[1][1].name)
    # print('checked all MI ','\n')
    # print('next_item: ', next_item.name, ' bag[i]: ', parameter.list_of_bags[bag_index].name)
    # print('check all true','\n')
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
    if len(parameter.list_of_items) == 0:
        for a in parameter.list_of_bags:
            if .90 > a.current_load_percentage:
                print("This bag hasn't reached the threshold yet", a.name, a.current_load_percentage)
                b = parameter.list_of_bags.index(a)
                for d in a.contains:
                    print("Therefore these items cannot be resolved", d.name)
                del parameter.list_of_bags[b]
                del parameter.list_of_bags[b]
        return True

    else:
        return False


param = InputReader.Input('input26.txt')
param.InterpretFile()


result = back_tracking(param)
print('result: ', result)
for a in param.list_of_bags:
    print('bag name: ', a.name, a.current_load_percentage)
    for b in a.contains:
        pass
        print('item name: ', b.name)
