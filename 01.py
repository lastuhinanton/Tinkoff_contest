number_of_people, number_of_capacity_bus = map(int, input().split())
space = []

if (number_of_capacity_bus % 2 == 0): start = number_of_capacity_bus // 2
else: start = number_of_capacity_bus // 2 + 1

space.append(start)
start -= 1
step = 2
for i in range(2, number_of_capacity_bus + 1):
    if (i % 2 == 0):
        if (start == 0): space.append(start + step)
        else: space.append(start)
    if (i % 2 == 1):
        space.append(start + step)
        start -= 1
        step += 2

i = p = 0
while (i <= number_of_capacity_bus and p != number_of_people):
    if (i % number_of_capacity_bus == 0 and i != 0): i = 0
    print(space[i])
    i += 1
    p += 1


    