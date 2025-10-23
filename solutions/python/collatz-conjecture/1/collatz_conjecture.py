def steps(number):
    if number<=0:
        raise ValueError('Only positive integers are allowed')
    curr=number
    step=0
    while curr!=1 and step<=1000:
        if curr%2==0:
            curr=curr//2
            step+=1
        else:
            curr=3*curr+1
            step+=1
    if curr!=1 and step>=1000:
        return 'could not reach 1 in 1000 steps'
    else:
        return step
        
