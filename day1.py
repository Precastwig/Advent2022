def part1():
    f = open("day1_input.txt")
    biggest_total = 0
    numbers = f.read().splitlines()
    current = 0
    for num in numbers:
        if num == '':
            if current > biggest_total:
                biggest_total = current
            current = 0
        else:
            val = int(num)
            current += val
    if current > biggest_total:
        biggest_total = current
    print(biggest_total)

def part2():
    f = open("day1_input.txt")
    totals = []
    numbers = f.read().splitlines()
    current = 0
    for num in numbers:
        if num == '':
            totals.append(current)
            current = 0
        else:
            val = int(num)
            current += val
    totals.append(current)
    totals = sorted(totals, reverse=True)
    print(totals[0] + totals[1] + totals[2])


part1()
part2()