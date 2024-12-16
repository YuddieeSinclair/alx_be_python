pattern = int(input("Enter the size of the pattern:"))
if pattern < 0:
    print("enter a positive number")
row = 0
while row < pattern:
    for element in range(pattern):
        print("*", end="")
    print("\n")
    row+=1
