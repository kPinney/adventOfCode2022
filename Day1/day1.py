mycount = 0
with open('Day1/day1input.txt', 'r') as f:
##    print(line.strip())
    count = 0
    for line in f:
        if line == '\n':
            count += 1
print(count)

##            print([int(x) for x in line])