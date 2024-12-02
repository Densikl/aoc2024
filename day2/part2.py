file = open('input.txt')
reports = []
for line in file.readlines():
    reports.append([int(level) for level in line.split()])

def isReportSafe(report):
    i = 1
    badLevelIndexes = []
    isSafe = True
    isIncreasing = (report[i-1] - report[i] < 0)
    while i < len(report):
        difference = report[i - 1] - report[i]
        if (isIncreasing and difference > 0) or (not isIncreasing and difference < 0) \
            or abs(difference) > 3 or abs(difference) < 1:
            badLevelIndexes.append(i-2)
            badLevelIndexes.append(i-1)
            badLevelIndexes.append(i)
            isSafe = False
            break
        
        i += 1

    return (isSafe, badLevelIndexes)


quantity = 0
for report in reports:
    isSafe, badIndexes = isReportSafe(report) 
    if isSafe:
        quantity += 1
        continue

    for i in badIndexes:
        newReport = [*report]
        newReport.pop(i)
        isSafe, _ = isReportSafe(newReport)
        if isSafe:
            quantity += 1
            break

print(quantity)

