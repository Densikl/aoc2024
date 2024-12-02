file = open('input.txt')
list1 = list()
list2 = list()
for line in file.readlines():
    nums = [int(num) for num in line.split()]
    list1.append(nums[0])
    list2.append(nums[1])

quantity = dict()

for num in list2:
    quantity[num] = quantity.setdefault(num, 0) + 1
    
    
sm = 0
for num in list1:
    sm += num * quantity.get(num, 0)

print(sm)