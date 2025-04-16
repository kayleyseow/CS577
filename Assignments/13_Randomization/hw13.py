import random

num_vars = int(input())
num_clauses = int(input())
satisfied = 0
clauses = []
for c in range(num_clauses):
    clauses.append([int(x) for x in input().strip().split()])

if __name__ == '__main__':
    while (satisfied / num_clauses < 7/8):
        vars = []
        for i in range(num_vars):
            val = [False, True]
            vars.append(random.choice(val))
        for c in range(len(clauses)):
            clause = clauses[c]
            x, y, z = vars[abs(clause[0]) - 1], vars[abs(clause[1]) - 1], vars[abs(clause[2]) - 1]
            if (clause[0] < 1):
                x = not x
            elif (clause[1] < 1):
                y = not y
            elif (clause[2] < 1):
                z = not z
            elif (x and y and z):
                satisfied += 1
    vars = [1 if x else -1 for x in vars]
    print(*vars)