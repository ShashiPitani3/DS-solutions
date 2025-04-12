n=int(input('Enter the number to check prime or not?\n'))


def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True
    

print(is_prime(n))
if is_prime(n):
    print(f'The number you have entered is a prime number , {n}')
else:
    print(f'The number you entered is not prime , {n}')