def lettertopriority(letter):
    val = ord(letter) # a = 97
    if letter.isupper():
        return val - 64 + 26
    else:
        return val - 96
    

def part1():
    f = open("day3_input.txt")
    backpacks = f.read().splitlines()
    prioritysums = 0
    for backpack in backpacks:
        comp1, comp2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
        a=list(set(comp1)&set(comp2))
        prioritysums += lettertopriority(a[0])

    print(prioritysums)

def part2():
    f = open("day3_input.txt")
    backpacks = f.read().splitlines()
    prioritysums = 0

    triple = []
    for count, backpack in enumerate(backpacks, start=1):
        triple.append(backpack)
        if count % 3 == 0:
            a = list(set(triple[0])&set(triple[1]))
            b = list(set(a)&set(triple[2]))
            prioritysums += lettertopriority(b[0])
            triple = []
    print(prioritysums)

part1()
part2()