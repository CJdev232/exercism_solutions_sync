def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    big_list=[]
    for list in lists:
        append(big_list,list)
    return big_list
        


def filter(function, list):
    items_true_in_function_given = []
    for item in list:
        if function(item):
            items_true_in_function_given.append(item)
    return items_true_in_function_given


def length(list):
    cur_length = 0
    for item in list:
        cur_length += 1
    return cur_length
        


def map(function, list):
    list_mapped = []
    for item in list:
        list_mapped.append(function(item))
    return list_mapped


def foldl(function, items, initial):
    accumulator = initial
    for item in items:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, items, initial):
    accumulator = initial
    for item in reversed(items):
        accumulator = function(accumulator,item)  
    return accumulator


def reverse(list):
    return list[::-1]
