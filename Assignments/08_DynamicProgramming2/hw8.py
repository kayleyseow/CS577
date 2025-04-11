# Gets the number of instances from the input
numInstances = int(input())

maxValues = []

# find the max value that the knapsack can hold
def knapsack(capacity, wi, value, nth):
    # Base case if if we have no items or no capacity to hold values
    # if (nth == 0 or capacity == 0):
    #     return 0
    # if (wi[nth-1] > capacity):
    #     return knapsack(capacity, wi, value, nth-1)
    # else:
    #     return max(value[nth-1] + knapsack(capacity-wi[nth-1], wi, value, nth-1), knapsack(capacity, wi, value, nth-1))
    matrix = [[0 for x in range(capacity + 1)] for x in range(nth + 1)]
    for i in range(nth + 1):
        for w in range(capacity + 1):
            if (i == 0 or w == 0):
                matrix[i][w] = 0
            elif (wi[i-1] <= w):
                matrix[i][w] = max(value[i-1] + matrix[i-1][w-wi[i-1]], matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]
    return matrix[nth][capacity]

# Iterate through how many instances we have
for i in range(numInstances):
    # number of items per instance, from input
    temp = input().strip().split(" ")
    numItems = int(temp[0])
    capacity = int(temp[1])
    # capacity = int(input().strip().split(" "))
    # print("numItems", numItems)
    # print("capacity", capacity)
    items = []
    values = []
    weights = []
    for item in range(numItems):
        items.append([int(x) for x in input().strip().split(" ")])
        # print(items[item])
        values.append(int(items[item][0]))
        # print(values)
        weights.append(int(items[item][1]))
        # print(weights)
    # print(items)
    maxValues.append(knapsack(capacity, values, weights, numItems))

# Print the result
for mValue in maxValues:
    print(mValue)
