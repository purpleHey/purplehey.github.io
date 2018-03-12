# myfile = open("input")
import sys

# expected output 998666
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

data = sys.stdin.readlines()

countOfNums = int(data[0])
print(countOfNums)
nums = data[1]
numL = nums.split(' ')
# print(numL)

firstNum = int(numL[0])
secNum = int(numL[1])
count = 0
if countOfNums > 1:
    for thirdNum in numL[2:]:
        if not is_number(thirdNum):
            break
        print(firstNum, int(secNum), int(thirdNum))

        if(int(firstNum) >= int(secNum)):
            count += 1
            firstNum = secNum - 1

        if int(firstNum) <= int(secNum) and int(secNum) < int(thirdNum):
            # strictly increasing
            firstNum = int(secNum)
            secNum = int(thirdNum)
        else:
            count += 1
            firstNum = firstNum + 1
            secNum = firstNum + 1


print(count)