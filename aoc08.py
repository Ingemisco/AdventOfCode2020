import re

file = open("aoc08.txt")
ls = file.readlines()

# part 1
acc = 0
pc = 0
executed = set()
while pc not in executed:
    executed.add(pc)
    instruction = ls[pc]
    if instruction.startswith("nop"):
        pc = pc + 1
    elif instruction.startswith("acc"):
        arg = instruction[4:-1]
        if arg[0] == '+':
            arg = arg[1:]
        acc += int(arg)
        pc = pc + 1
    else:
        arg = instruction[4:-1]
        if arg[0] == '+':
            arg = arg[1:]
        pc += int(arg)
print(acc)

for i in range(len(ls)):
    if ls[i].startswith("acc"):
        continue
    acc = 0
    pc = 0
    executed = set()
    while pc < len(ls):
        executed.add(pc)
        instruction = ls[pc]
        if pc == i:
            if ls[i].startswith("nop"):
                instruction = ls[i].replace("nop", "jmp")
            else:
                instruction = ls[i].replace("jmp", "nop")
        if instruction.startswith("nop"):
            pc = pc + 1
        elif instruction.startswith("acc"):
            arg = instruction[4:-1]
            if arg[0] == '+':
                arg = arg[1:]
            acc += int(arg)
            pc = pc + 1
        else:
            arg = instruction[4:-1]
            if arg[0] == '+':
                arg = arg[1:]
            pc += int(arg)
        if pc in executed:
            break
    else:
        print(acc)
