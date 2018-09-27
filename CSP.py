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
bag1 = Bag.Bag
bag1.capacity = 3
bag1.current_load = 0
bag1.name = "B"
bag1.contains = []
item1 = Items.Item
item1.name = "A"
item1.weight = 2
# item2 = Items.Item
# item2.weight = 3
# item2.name = "C"
bag1.add_item(bag1, item1)
#bag1.add_item(bag1,item2)
print(item1.name)
#bag_list = [Bag.Bag]

#print(b[0])
# class CSP:
#     def __init__(self, ):
#     def back_tracking(self):
#         if assignment == complete
#         return
