def part1():
    f = open("day2_input.txt")
    rounds = f.read().splitlines()
    score = 0
    for round in rounds:
        (opp, me) = round.split(" ")
        if me == "X":
            score += 0
        if me == "Y":
            score += 3
        if me == "Z":
            score += 6
        
        # A = rock
        # B = paper
        # C = scissors

        if opp == "A":
            if me == "Y":
                score += 1
            if me == "X":
                score += 3
            if me == "Z":
                score += 2
        if opp == "B":
            if me == "Y":
                score += 2
            if me == "X":
                score += 1
            if me == "Z":
                score += 3
        if opp == "C":
            if me == "Y":
                score += 3
            if me == "X":
                score += 2
            if me == "Z":
                score += 1
                
    print(score)

    

#def part2():
    


part1()
#part2()