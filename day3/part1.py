file = open("input.txt")
data = [line.split(sep="mul(") for line in file.readlines()]
maybeCorrect = []
nums = ('1', '2', '3', '4', '5',
        '6', '7', '8', '9', '0')

instructions = []
for line in data:
    for i in line:
        result = ''
        isOk = True
        for sym in i:
            if sym == ')':
                break
            elif sym in nums or sym == ',':
                result += sym
            else:
                isOk = False
                break

        if isOk:
            instructions.append([int(num) for num in result.split(',')])

sm = 0
for i in instructions:
    sm += i[0] * i[1]

print(sm)