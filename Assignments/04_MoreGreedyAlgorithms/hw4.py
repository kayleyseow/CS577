# Gets the number of instances from the input
numInstances = int(input())

allIntervalLengths = []

# Function to sort the tuple by end first algorithm
def sortTuple(tup):
    tup.sort(key = lambda x:x[1])
    return tup

# Iterate through how many instances we have
for i in range(numInstances):
    # number of jobs per graph, from input
    blankPagesCache = int(input())
    pageRequests = int(input())

    requestSequence = []
    for request in range(pageRequests):
        requestSequence.append(input().split(' '))
    
    print(requestSequence)

    # intervalsTemp = []

    # # Iterate through the job intervals, input them into tuples
    # for j in range(numJobs):
    #     # Gets input as each line split, and makes it into a tuple, adds tuple to the list
    #     interval = tuple(int(x) for x in input().split(' '))
    #     if interval[0] > interval[1]:
    #         print("Invalid tuple combination: the end time is before the start time.\n")
    #         exit()
    #     elif interval[0] < 0 or interval[1] < 0:
    #         print("Invalid tuple combination: the time entered cannot be negative.\n")
    #         exit()
    #     else:
    #         intervalsTemp.append(interval)
    
    # # sort the list, and then put it in ascending order off the second value in the tuple
    # sortTuple(intervalsTemp)

    # # Declare the constants for finish first
    # currentEndTime = -1
    # schedule = []
    # count = 1

    # # We iterate through the sorted intervals list, implementing finish first
    # for interval in intervalsTemp:
    #     if currentEndTime < 0:
    #         currentEndTime = int(interval[1])
        
    #     if int(interval[0]) >= currentEndTime:
    #         currentEndTime = int(interval[1])
    #         # print(currentEndTime)
    #         count = count + 1

    # allIntervalLengths.append(count)

# Print the result
for interval in allIntervalLengths:
    print(interval)
