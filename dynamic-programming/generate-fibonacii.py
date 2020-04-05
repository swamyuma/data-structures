# what is a fibonacci sequence?
# https://en.wikipedia.org/wiki/Fibonacci_number
# Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 
# sequence: 1 1 2 3 5 8 ...
#                f(5)
#               /    \
#            f(4)     f(3)
#            / \      / \
#          f(3) f(2) f(2) f(1)
#          / \           
#        f(2) f(1)  
# three ways to solve this problem

## 1. recursion
def fib(n):

    if n<=1:
        result=1
    else:
        result=fib(n-1)+fib(n-2)
    return result

### Test case
number=1

if number <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for ii in range(number):
       print(fib(ii))


## 2. Memoization
def fib_memo(n,memo):
    
    if n==1 or n==2:
        result=1
        memo[n]=result
    else:
        result = fib_memo(n-1, memo)[0] + fib_memo(n-2, memo)[0]
        memo[n]=result
    
    return (result, memo)

### Test case
number=1
result,seq=fib_memo(number,[0]*(number+1))
print(f'fib({number})=>',seq)

## 3. Bottom_up simplest
def fib_bottom_up(n):
    # initialize
    bottom_up=[0]*(n+1)

    if n<=1:
        bottom_up[1]= 1
        return bottom_up

    bottom_up[1] =1
    for ii in range(2,(n+1)):
        bottom_up[ii] = bottom_up[ii-1]+ bottom_up[ii-2]
    return bottom_up
    
### Test case
result=fib_bottom_up(1000)
print(result)
