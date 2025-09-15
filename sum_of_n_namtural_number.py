#### sum of N antural numbers

x = int(input("Enter a number: "))
sum = 0
for i in range(1, x + 1):
    sum += i
print("The sum of first", x, "natural numbers is:", sum)
