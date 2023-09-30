n = int(input("enter the number: "))
x = int(input("enter : "))
sum=0
for i in range(1,n):
    pwr = (x**i)
    pdt = pwr / i 
    sum =  sum + pdt
print(f'the sum of {n} terms is {sum} ')