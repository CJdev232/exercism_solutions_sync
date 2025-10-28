def open_box(item):
    box=[]
    if is_leaf(item):
        if item is not None:
            box.append(item)
    else:
        for subitem in item:
            box.extend(open_box(subitem))
    return box
def is_leaf(item):
    return not isinstance(item, (list, tuple, dict))
    
            
    
def flatten(iterable):
    flattened=[]
    for item in iterable:
        flattened.extend(open_box(item))
    return flattened
