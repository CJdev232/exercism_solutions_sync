def is_valid_triangle(sides):
    if len(sides)!=3:
        return False
    if min(sides)<=0:
        return False
    total_len=sum(sides)
    for index in range(3):
        if 2*sides[index]>total_len:
            return False
    return True
    
def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    return len(set(sides))==1
    


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    return len(set(sides))<=2


def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    return len(set(sides))==3
