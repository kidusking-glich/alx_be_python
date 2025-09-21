Patern = int(input("Enter the size of the pattern: "))
row = 0

while row < Patern:
    for _ in range(Patern):
        print('*', end="")
    print()
    row += 1
    