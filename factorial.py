#print the factorial of a number using functional recursion methods
#in this pattern we are returning the values instead of passing parameters
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))


#sum of n natural numbers 
#here the type of recursion is parameterized recursion
#instead of returning the value we are printing the value once base condition is met
def sum(i,s):
    if i<1:
        print(s)
        return
    sum(i-1,s+i)
sum(3,0)

