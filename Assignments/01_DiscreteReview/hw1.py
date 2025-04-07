nameList = []
nameNums = input()
for i in range(int(nameNums)):
    nameList.append(input())
for i in range(int(nameNums)):
    print("Hello, " + nameList[i] + "!")