import math
def is_armstrong_number(number):
    if number<0:
        return False
    if number==0:
        return True
    num_digits=math.floor(math.log(abs(number))/math.log(10))+1
    sum_curr=0
    for digit in str(number):
        sum_curr+=math.pow(int(digit),num_digits)
    return number==sum_curr
        
    
