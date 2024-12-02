file = open('input.txt')
list1 = list()
list2 = list()
for line in file.readlines():
    nums = [int(num) for num in line.split()]
    list1.append(nums[0])
    list2.append(nums[1])

list1.sort(reverse=True)
list2.sort(reverse=True)

sm = 0
while len(list1) > 0 and len(list2):
    sm += abs(list1.pop() - list2.pop())

print(sm)
