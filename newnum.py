import math
n=int(input('enter thte number to check prime or not?\n'))

count=0
for i in range(1,int(math.sqrt(n)+1)):
   
    if n%i==0:
        # print(i)
        count+=1
        print(count)
        if n//i!=i:
            # print(i)
            count+=1
    


if count>2:
        print(f'The number {n} is not prime')
else:
    print(f'The number {n} is a prime number')
       
