import re

file = open("aoc18.txt")
ls = list(map( lambda x: x.replace("\n", "").replace("(", " ( ").replace(")", " ) "), file.readlines()))

def calculate(out):
    vals = []
    while len(out) > 0:
        s = out[0]
        out = out[1:]
        if s == '+':
            a = vals[0]
            b = vals[1]
            vals = [(a + b)] + vals[2:]
        elif s == '*':
            a = vals[0]
            b = vals[1]
            vals = [(a * b)] + vals[2:]
        else:
            vals = [int(s)] + vals
    return vals[0]

# part 1

def calculateline(line):
    operators = []
    out = []

    for s in line.split():
        if re.match(r"\d+", s):
            out.append(int(s))
        elif re.match(r"[+*]", s):
            while len(operators) > 0 and operators[0] != '(':
                out.append(operators[0])
                operators = operators[1:]
            operators = [s] + operators
        elif s == '(':
            operators = [s] + operators
        else: # )
            while operators[0] != '(':
                out.append(operators[0])
                operators = operators[1:]
            operators = operators[1:]
    for s in operators:
        out.append(s)
    return calculate(out)
    

t = map(calculateline, ls)

sum = 0
for p in t:
    sum += p
print(sum)
            
    

def calculateline2(line):
    operators = []
    out = []

    for s in line.split():
        if re.match(r"\d+", s):
            out.append(int(s))
        elif re.match(r"[+*]", s):
            while len(operators) > 0 and operators[0] == '+': # this is literally the only change to the above
                out.append(operators[0])
                operators = operators[1:]
            operators = [s] + operators
        elif s == '(':
            operators = [s] + operators
        else: # )
            while operators[0] != '(':
                out.append(operators[0])
                operators = operators[1:]
            operators = operators[1:]
    for s in operators:
        out.append(s)

    return calculate(out)

t = map(calculateline2, ls)

sum = 0
for p in t:
    sum += p
print(sum)