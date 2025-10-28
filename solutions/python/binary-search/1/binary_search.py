def _binary_search_helper(search_list,value,left_idx,right_idx):
    if left_idx > right_idx:
        raise ValueError('value not in array')
    mid_idx=(left_idx+right_idx)//2
    mid_value=search_list[mid_idx]
    while (right_idx-left_idx)>0:
        if mid_value == value:
            return mid_idx
        elif mid_value < value:
            return _binary_search_helper(search_list = search_list,value = value,left_idx = mid_idx+1,right_idx = right_idx)
        elif mid_value > value:
            return _binary_search_helper(search_list = search_list,value = value,left_idx = left_idx,right_idx = mid_idx-1)
    if right_idx-left_idx == 0:
        if search_list[left_idx] != value:
            raise ValueError('value not in array')
        else:
            return left_idx

        
def find(search_list, value):
    if value is None:
        raise ValueError('Value cannot be None')
    if not search_list:
        raise ValueError('value not in array')
    return _binary_search_helper(search_list, value, 0, len(search_list) - 1)