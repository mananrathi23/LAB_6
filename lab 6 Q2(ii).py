n = int(input("enter the number: "))
fact=1
for i in range(1,n):
    fact =fact*i
    fact_1 = (1 / fact)
print(f'the sum of {n} terms is {fact_1} ')