mycount = 0
with open('day1input.txt', 'r') as f:
##    print(line.strip())
    count = 0
    for line in f:
        if line == '\n':
            count += 1
print(count)

##with open('day1input.txt', 'r') as f:
##        print(' '.join(f.splitlines()))
with open('day1input.txt', 'r') as f:
    for line in f:
        if line != '\n':
            print([int(x) for x in line])