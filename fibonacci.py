"""
  Author: Saudamini Chaurasia
  Description: Code implements a recursive function to generate the first n numbers of the Fibonacci sequence

"""


def fibonacci(n):
    if n == 0 or n == 1:

        return n

    else:

        return fibonacci(n - 2) + fibonacci(n - 1)


num = int(input("Enter a number: "))

if num < 0:
    print("Number not valid to generate Fibonacci sequence")

i = 0

print("Fibonacci Sequence: ")

for i in range(0, num):
    print(fibonacci(i))
