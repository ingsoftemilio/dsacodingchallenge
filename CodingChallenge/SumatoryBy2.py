"""
Challenge: Summatory by 2 units

Print values until the target it's met
Example it will print the values 2 pairs until a target is met, 2,4,6,8,10...22 until this value is met

"""

def summatory(target,value):
    
    if value>=target:
        return value
    
    value+=2
    print(value)
    
    return summatory(target,value)

    
res = summatory(22,0)
print("***")
print(res)