input = "157623984"
#input = "389125467"

input = list(map(int, input))



def next(input):
    curr = input[0] # the input will be rotated so the current is always the first
    pick = input[1: 4]
    input = input[4:]

    dest = curr - 1
    if dest == 0:
        dest = 9
    while dest in pick:
        dest -= 1
        if dest == 0:
            dest = 9
    i = input.index(dest)
    for j in range(3):
        input.insert( 1 + i + j, pick[j])
    
    input = input + [curr]
    return input

def after_one(input):
    while(input[0] != 1):
        a = input[0]
        input = input[1:] + [a]
    b = ""
    for i in input[1:]:
        b += str(i)
    return b

for i in range(100):
    input = next(input)

print(input, after_one(input))

# part 2

class node:
    def __init__(self, val):
        self.val = val
        self.next = None 
        self.lower = None

class doublelist:
    def __init__(self, initial, size):
        self.curr = node(initial[0])
        temp = self.curr 
        if(initial[0] == 1):
            one = temp # save the one because its lower will be one million, the other values in initial have a lower in initial

        for i in initial[1:]:
            temp.next = node(i)
            temp = temp.next
            if(temp.val == 1):
                one = temp
            last = temp
        
        highest = len(initial)
        while highest > 1:
            temp = self.findval(highest)
            highest -= 1
            temp.lower = self.findval(highest)
            temp = temp.lower
        
        lower = self.findval(len(initial))

        temp = node(len(initial) + 1)
        temp.lower = lower
        last.next = temp
        lower = temp

        for i in range(len(initial) + 2, size + 1):
            temp = node(i)
            temp.lower = lower
            lower.next = temp
            lower = temp
        temp.next = self.curr
        one.lower = temp
    
    def findval(self, val):
        temp = self.curr
        while temp != None and temp.val != val:
            temp = temp.next
        if temp.val == val:
            return temp
        else:
            return None # there is not a node in this list with the value val

    def nextturn(self):
        pick = self.curr.next
        invalid = [pick.val, pick.next.val, pick.next.next.val]
        dest = self.curr.lower
        while dest.val in invalid:
            dest = dest.lower
        self.curr.next = pick.next.next.next
        pick.next.next.next = dest.next
        dest.next = pick
        self.curr = self.curr.next

input = "157623984"
#input = "389125467"

input = list(map(int, input))

l = doublelist(input, 1000000)

for _ in range(10000000):
    l.nextturn()
temp = l.findval(1)

a = temp.next.val
b = temp.next.next.val
print(a, b, a * b)