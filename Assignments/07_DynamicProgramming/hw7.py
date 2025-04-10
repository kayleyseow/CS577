# Gets the number of instances from the input
numInstances = int(input())

schedule = []

# find the overlapping intervals of the times entered
def intervals(jobs, start, left, right):
    if (left == right):
        if (jobs[left][1] > start):
            return left -1
        else:
            return left
    middle = left + ((right - left) // 2)
    if (jobs[middle][1] > start):
        return intervals(jobs, start, left, middle)
    else:
        return intervals(jobs, start, middle + 1, right)
    
# Iterate through how many instances we have
for i in range(numInstances):
    # number of jobs per graph, from input
    numJobs = int(input())
    jobs = []
    for job in range(numJobs):
        jobs.append([int(x) for x in input().strip().split(" ")])
        print(job)
    jobs.sort(key=(lambda x: x[1]))
    temp = numJobs * [0]
    temp[0] = jobs[0][2]
    for job in range(numJobs)[1:]:
        interval = intervals(jobs, jobs[job][0], 0, numJobs)
        temp[job] = max(temp[job-1], temp[interval] + jobs[job][2])
    schedule.append(temp[len(temp)-1])

# Print the result
for s in schedule:
    print(s)
