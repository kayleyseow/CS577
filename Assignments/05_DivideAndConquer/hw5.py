# Gets the number of instances from the input
numInstances = int(input())

allInversions = []

def countInversions(listA, listB):
    S = []
    count = 0
    while (len(listA)!= 0 or len(listB)!= 0):
        # if listB has the minimum
        print("the minimum", min(listA[0], listB[0]))
        print("list B at 0",listB[0])
        if (min(listA[0], listB[0])) == listB[0]:
            print(listB[0])
            count = count + len(listA)
            S.append(listB.pop(0))
        # if listA has the minimum
        else:
            S.append(listA.pop(0))
    maxList = max(len(listA), len(listB))
    print(maxList)
    for max in maxList:
        S.append(max)
    return S, count
        
def countSort(list):
    if len(list) == 1:
        return list, 0
    middle = len(list)//2
    leftList = list[:middle]
    rightList = list[middle:]
    list1, count1 = countSort(leftList)
    list2, count2 = countSort(rightList)
    A, count = countInversions(list1, list2)
    allInversions.append(count+count1+count2)
    
# Iterate through how many instances we have
for i in range(numInstances):
    # number of jobs per graph, from input
    numElements = int(input())
    # print("numelements", numElements)

    elements = input().split(' ')
    # print(elements)
    countSort(elements)

# Print the result
for inversion in allInversions:
    print(inversion)
