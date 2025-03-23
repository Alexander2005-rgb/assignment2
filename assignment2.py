#check the number is odd or even
a=int(input("Enter a number: "))
if(a%2==0):
    print(a," is the even number")
else:
    print(a,"is the odd number")

#sum of integer from 1 to 50  using  a loop
sum =0
for i in range(1,51):
     sum=sum+i
print("The Sum of number from 1 to 50 is: ",sum)
