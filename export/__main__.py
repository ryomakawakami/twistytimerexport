import re

if __name__ == '__main__':
    times = {}  # Indexed by cube type (333, 444, etc)
    with open('data.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                continue
            x = re.split('";*"*', line[1:].strip())
            if x[0] in times:
                if x[1] in times[x[0]]:
                    times[x[0]][x[1]].append(x)
                else:
                    times[x[0]][x[1]] = [x]
            else:
                times[x[0]] = {x[1]: [x]}

    for cubeType in times:
        for category in times[cubeType]:
            print(category)
