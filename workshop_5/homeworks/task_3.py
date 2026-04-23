# ==============================
# Task 3: Merge two shopping lists
# ==============================
# Two people made shopping lists with item -> quantity.
# Write merge_lists(list1, list2) that returns a combined dictionary
# where quantities are summed for items that appear in both.
#
# Expected: {"milk": 3, "bread": 3, "eggs": 12, "cheese": 1}


list1 = {"milk": 2, "bread": 1, "eggs": 12}
list2 = {"bread": 2, "cheese": 1, "milk": 1}

def merge_lists(list1, list2):
    combined = list1.copy()
    for item, quantity in list2.items():
        if item in combined:
            combined[item] += quantity
        else:
            combined[item] = quantity

    return combined

print(merge_lists(list1, list2))

print(merge_lists({"a": 17, "b": 19}, {"c": 27, "a": 3}))
