file = open("aoc21.txt")
ls = file.readlines()
# part 1

poss_ing = {} # stores for each allergen a set of possible ingredients

ing = set()

for s in ls:
    t = s.split("(contains ")
    ingr = t[0].split()
    allergens = "".join(list(filter(lambda x: x != ')' and x != '\n', t[1]))).split(", ")
    for a in allergens:
        if a not in poss_ing:
            poss_ing[a] = set(ingr)
        else:
            poss_ing[a] = poss_ing[a].intersection(set(ingr))
    ing = ing.union(set(ingr))


mightbe = set()
for i in poss_ing.values():
    mightbe = mightbe.union(set(i))

defnot = ing.difference( mightbe)

sum = 0
for l in ls:
    t = l.split("(contains ")
    ingr = t[0].split()
    for p in ingr:
        if p in defnot:
            sum += 1
print(sum)

# part 2

vals = [ [p,q] for (p,q) in poss_ing.items() ]
for i in range(3):
    vals.sort(key = lambda x: len(x[1]))
    for i in range(len(vals)):
        if len(vals[i][1]) == 1:
            for j in range(len(vals)):
                if j != i:
                    vals[j][1] = vals[j][1].difference(vals[i][1])

d = {}
for i in range(len(vals)):
    p = vals[i][0]
    q = vals[i][1].pop()

    vals[i] = p, q

vals.sort(key = lambda x: x[0])

for (p, q) in vals:
    print(q, end=",")
