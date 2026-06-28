def factorial(n):
    if n==0 and n==1:
        return 1
    elif n<0:
        return "factorial is not defined for negative integers."
    else:
        return n*factorial(n-1)
    
print(factorial(5))
print(factorial(0))
print(factorial(-3))