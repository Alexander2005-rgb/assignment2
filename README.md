# Check if the number is odd or even
a = int(input("Enter a number: "))
This line prompts the user to enter a number. The input() function captures the user's input as a string, and int() converts it to an integer, which is then stored in the variable a.
if (a % 2 == 0):
This line checks if the number stored in a is even. The expression a % 2 calculates the remainder when a is divided by 2. If the remainder is 0, it means a is even.
    print(a, "is the even number")
If the condition in the previous line is true (i.e., a is even), this line prints a message indicating that a is an even number.
else:
This line introduces an alternative condition that will execute if the previous if condition is false (i.e., if a is not even).
    print(a, "is the odd number")
If the number a is odd (the condition in the if statement was false), this line prints a message indicating that a is an odd number.
# Sum of integers from 1 to 50 using a loop
sum = 0
This line initializes a variable sum to 0. This variable will be used to accumulate the total sum of integers from 1 to 50.
for i in range(1, 51):
This line starts a for loop that iterates over a range of numbers from 1 to 50 (inclusive). The variable i takes on each value in this range during each iteration of the loop.
    sum = sum + i
Inside the loop, this line adds the current value of i to the sum variable. This accumulates the total sum of all integers from 1 to 50.
print("The Sum of number from 1 to 50 is: ", sum)
After the loop has completed, this line prints the total sum of integers from 1 to 50, displaying the message along with the value of sum.
