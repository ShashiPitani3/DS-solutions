n=int(input('Enter the number to find all the divisors?\n'))

def print_divisors(num):
    divisors=[n for n in range(1,num+1) if num%n==0]
    print(divisors)

print_divisors(n)