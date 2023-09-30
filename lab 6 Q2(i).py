n = int(input("enter the number: "))
sum=0
for i in range(1,n):
    sum_1 = (1/i)
    sum = sum + (sum_1)
print(f'the sum of {n} terms is {sum} ')