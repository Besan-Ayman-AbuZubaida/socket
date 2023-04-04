# Homework 3 



# Problem 1
def bool(x, lb, ub):
    '''
    Given three integer variables, x, lb, and ub, write a single boolean 
    expression that evaluates to True if x is outside the range between 
    lb and ub (inclusive), and False otherwise. 

    Inputs:
        x (int)
        lb (int): lower bound
        ub (int): upper bound
    '''
    # FILL IN YOUR CODE HERE
    return x < lb or x > ub
    
print(bool(25, 10, 20))    

# Problem 2
def num_string(x):
    '''
    Given a number x, produce a string: "POSITIVE", "NEGATIVE", "ZERO" 
    (depending on whether the number is positive, negative, or zero)

    Input:
        x (number)
    
    Returns (string): "POSITIVE", "NEGATIVE", "ZERO" 
    '''
    # FILL IN YOUR CODE HERE
    if(x==0):
        return "ZERO"
    if(x>0):
        return "POSITIVE"
    if(x<0):
        return "NEGATIVE"
print(num_string(-5))

# Problem 3
def add(a,b):
    ''' 
    Returns the sum of a and b
    
    Inputs: 
        a, b (number): inputs
    
    Returns (number): sum of a and b
    '''
    # FILL IN YOUR CODE HERE
    return a+b
print(add(2,3))

# Problem 4
def strictly_increasing(n1,n2,n3,n4):
    ''' 
    Returns true if the numbers are strictly increasing in magnitude
    (if |n4| > |n3| > |n2| > |n1|), false otherwise 

    Inputs:
        n1, n2, n3, n4 (numbers): inputs

    Returns (Boolean): true if the arguments are strictly increasing in magnitude, false otherwise
    '''
    # FILL IN YOUR CODE HERE
    return abs(n4) > abs(n3) > abs(n2) > abs(n1)
print(strictly_increasing(-5,6,-7,8))

# Problem 5    
def area(b, h):
    '''
    Returns the area of the triangle
    
    Inputs:
        b (number): base
        h (number): height
    
    Returns (number): Area of the triangle
    '''
    # FILL IN YOUR CODE HERE
    return .5*b*h
print(area(5,6))

# Problem 6
def remainder(p, q):
    '''
    Returns the remainder of p divided by q (p/q).
    
    Inputs:
        p, q (integers): inputs
        
    Returns (integer): remainder of p / q 
    '''
    # FILL IN YOUR CODE HERE
    return (p%q)
print(remainder(12,10))

# Problem 7
def dict_sep(dict):
    '''
    Given a dictinoary, return a list of its keys and a list of its values.
    e.g. dict = {"a":1, "b":2, "c":3}
    
    Returns 
    ["a","b","c"] and [1, 2, 3]
    
    Input:
        dict: dictionary
    Returns:
        list of keys
        list of values
    '''
    # FILL IN YOUR CODE HERE
    return list(dict.keys()),list(dict.values())
  
keys, values=dict_sep({"a":1, "b":2, "c":3})
print("list of keys: ", keys)
print("list of values: ", values)

