file = open('input.txt')
reports = []
for line in file.readlines():
    reports.append([int(level) for level in line.split()])

quantity = 0
for report in reports:
    i = 1
    isIncreasing = (report[i-1] - report[i] < 0)
    isSafe = True
    while i < len(report):
        difference = report[i - 1] - report[i]
        if (isIncreasing and difference > 0) or (not isIncreasing and difference < 0) \
            or abs(difference) > 3 or abs(difference) < 1:
            isSafe = False
            break
        
        i += 1

    quantity += int(isSafe)


print(quantity)

