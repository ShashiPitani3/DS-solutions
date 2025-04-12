n=int(input('Enter the number to check the number is armstrong number or not?\n'))


def find_count_of_digits(n):
    count=0
    digits=[]
    num=n
    while num>0:
        digits.append(num%10)
        num=num//10
        count+=1
    if find_armstrong(digits,count):
        return True
    else:
        return False
    

def find_armstrong(digits,count):
    is_armstrong=[digit ** count for digit in digits]
    if sum(is_armstrong)==n:
        return True
    else:
        return False

if find_count_of_digits(n):
    print(f"The number is armstrong number , {n}")
else:
    print(f"The number is not armstron number, {n}")


        
