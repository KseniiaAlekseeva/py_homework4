n = int(input("Enter the number of element of first set: "))
list1 = []
for i in range(n):
    list1.append(int(input(f"Enter element {i+1}: ")))

m = int(input("Enter the number of element of second set: "))
list2 = []
for i in range(m):
    list2.append(int(input(f"Enter element {i+1}: ")))

print(list1)
print(list2)

result = list(set(list1).intersection(set(list2)))
result.sort()

print(result)
