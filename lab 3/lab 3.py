import random

def printList(lst):
    for row in lst:
        for element in row:
            print(element, end='   ')
        print()

n = int(input("Sətir və sütun sayını daxil edin: "))
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(random.randint(-9, 9))

print("Matris:")
printList(a)
print()

total_sum = 0

for i in range(n):
    total_sum += a[i][i] ** 2  # Baş diagonalda yerləşən ədədlərin kvadratlarının cəmi

print("Baş diagonalda yerləşən ədədlərin kvadratlarının cəmi:", total_sum)
