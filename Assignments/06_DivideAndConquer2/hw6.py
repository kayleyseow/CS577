# Gets the number of instances from the input
numInstances = int(input())

allInversions = []

def countInversions(listA, listB):
    #print(listA, listB)
    S = []
    count = 0
    while (not(len(listA)== 0 or len(listB)== 0)):

        if (min(listA[0][1], listB[0][1])) == listB[0][1]:
            count = count + len(listA)
            S.append(listB.pop(0))
        else: #(min(listA[0], listB[0])) == listA[0]:
            S.append(listA.pop(0))

    while (len(listA)!= 0 and len(listB) == 0):
        S.append(listA.pop(0))
    while (len(listB)!= 0 and len(listA) == 0):
        S.append(listB.pop(0))
    return S, count

#Output sorted array and the number of inversions
def countSort(list):
    if len(list) == 1:
        return list, 0
    # split list into left and right
    middle = len(list)//2
    leftList = list[:middle]
    rightList = list[middle:]
    list1, count1 = countSort(leftList)
    list2, count2 = countSort(rightList)
    A, count = countInversions(list1, list2)
    # allInversions.append(count+count1+count2)
    return A, (count+count1+count2)
    
# Iterate through how many instances we have
for i in range(numInstances):
    # number of jobs per graph, from input
    numElements = int(input())

    topPoints = []
    bottomPoints = []

    for x in range(numElements):
        topPoints.append(int(input()))
    for y in range(numElements):
        bottomPoints.append(int(input()))
    
    pointPairs = []
    for j in range(numElements):
        pointPairs.append((topPoints[i], bottomPoints[i]))
    pointPairs.sort(key=lambda x : x[0])

    mergedList, inversions = countSort(pointPairs)
    print("mergedList:", mergedList)
    print("inversions:", inversions)
    allInversions.append(inversions)
    

# Print the result
for inversion in allInversions:
    print(inversion)
