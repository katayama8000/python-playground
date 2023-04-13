from functions import add_numbers

ret1 = add_numbers(1, 2)
print(ret1)

# generater
l = ["Good morning", "Good afternoon", "Good night"]
for i in l:
    print(i)

# generator
print("-----------------")

def greeting():
    yield "Good morning"
    yield "Good afternoon"
    yield "Good night"

g = greeting()
print(next(g))
print(next(g))
