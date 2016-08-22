#!/bin/python


def contains(list, sublist):
    """ determines whether e is contained in the list """
    for ele in list:
        if ele == sublist:
            return True
    return False


integer_list = [0,1,2,3]

print("")
print("Does the list contain 3?: %r" % contains(integer_list, 3))
print("Does the list contain 5?: %r" % contains(integer_list, 5))
print("")

list1 = [1,2,3,4]
list2 = [1,2,3,4,5,6,7]
list3 = [1,2,3,5]


# Create a function which determines whether a list is contained in another list.
# Some tips:
# - use the contains function defined above in your function.
# - you want to check if each element in the sublist is contained in the list
# - you can use boolean arithmetics, short example in boolean_arithmetic.py

def sublist_contains(list, sublist):
    # for each ele in sublist
    for ele in sublist:
        # ele exists in list
        #if ele in list:
        #    pass
        #else: # not ele in list
        #    return False
        #if not ele in list:
        #    return False
        #else: # not ele in list
        #    pass
        if not ele in list:
            return False
    return True

# sublist_contains([1,2,4,3,5,6,7],[1,2,3,4]) => True

# let l be an arbitrary list
# sublist_contains([1, l, 3],l) => True


print("")
print("Expected True,  Actual %r" % sublist_contains(list2, list1))
print("Expected False, Actual %r" % sublist_contains(list3, list1))
print("Expected True,  Actual %r" % sublist_contains(list1, list1))
print("")

