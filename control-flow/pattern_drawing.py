size = int(input("Enter the sie of the pattern: "))
if size <= 0:
    print("Error: Enter positive integer")

row = 0

while row < size:
    for _ in range(size):
        print("*", end="")
    print("*", end="")

    