n = int(input("Enter the number of shrubs: "))

berries = []
for i in range(n):
    berries.append(
        int(input(f"Enter the number of berries on the shrub {i+1}: ")))

print("Initial berries", berries)

sum_berries = []
max_berries = 0
for i in range(n):
    berries = berries[1:]+berries[:1]
    sum3 = sum(berries[0:3], 0)
    if sum3 > max_berries:
        max_berries = sum3
    print(f"Berries is {berries}. For {berries[1]} sum3 is {sum3}.")

print(f"Maximum berries for one module is {max_berries}.")
