import re

file = open("aoc07.txt")
ls = file.readlines()

class Bag:
    
    def __init__(self, name):
        self.name = name
        self.contains = set()
        self.contained = set()
        self.amount = {}
    
    def addBag(self, b, count):
        self.contains.add(b)
        self.amount[b.name] = count
        b.contained.add(self)
    
    def is_contained_in(self):
        a = set()
        for c in self.contained:
            a.add(c)
            a = a.union( c.is_contained_in() )
        return a 
    
    def needed_amount(self):
        sum = 0
        for b in self.contains:
            sum += self.amount[b.name] * (1 + b.needed_amount())
        return sum

graph = {} 
for l in ls:
    p = l.split(" bags contain ")
    graph[p[0]] = Bag(p[0])
for l in ls:
    p = l.split(" bags contain ")
    q = p[1].split(", ")

    for bag in q:
        a = 0
        if re.match(r"\d+", bag) is not None:
            a = int(re.match(r"(\d+)", bag).group(0))
            while re.match(r"\d", bag) is not None:
                bag = bag[1:]
        else:
            continue
        bag = bag[1:] # skip space
        name = re.match(r"(\w+ \w+)" , bag).group(0)
        graph[p[0]].addBag(graph[name], a)

print(len(graph["shiny gold"].is_contained_in()))


# part 2

print(graph["shiny gold"].needed_amount())