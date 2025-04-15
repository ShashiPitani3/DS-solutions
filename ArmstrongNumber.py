
#if summation of cubs of each number ends up with the same number the number is armstrong number
n=int(input('Enter the number to check the number is armstrong number or not?\n'))


def find_count_of_digits(n):
    res=0
    
    num=n

    while num>0:
        ld=num%10
        res+=ld ** 3
        print(res)
        num=num//10
    if res==n:
        return True
    else:
        return False

        
    

if find_count_of_digits(n):
    print(f"The number is armstrong number , {n}")
else:
    print(f"The number is not armstron number, {n}")


        
