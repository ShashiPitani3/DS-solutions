# Greatest common divisor -GCD
#To find GCD among 2 numbers find the factors of each number
#ex: n1=12,n2=15
#factors of 12:[1,2,3,4,12]
#factors of 15:[1,3,5,15]
#find the common factors among 2 numbers
#common_factors=[1,3]
#the maximum number of 1,3 is 3->3 is GCD for 2 numbers 12,15



def find_factors_of_num(num):
    n=[]
    for i in range(1,num+1):
        if num%i==0:
            n.append(i)
    return n

def find_gcd():
    n1=int(input('Enter the first number to find GCD?\n'))
    n2=int(input('Enter the second number to find GCD?\n'))
    factors_of_n1=find_factors_of_num(n1)
    factors_of_n2=find_factors_of_num(n2)
    gcd=[n for n in factors_of_n1 if n in factors_of_n2]
    return max(gcd)

gcd=find_gcd()
print(gcd)



