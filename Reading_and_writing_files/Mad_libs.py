from pathlib import Path
b = 0
lock = True
adjective = input("Enter an adjective:")
noun = input("Enter a noun:")
verb = input("Enter a verb:")
noun1 = input("Enter a noun:")
f = open(f"{Path.home()}/Testing/sen.txt", "r")
a = f.read().split()
print(a)
for x in a:
    if x == "ADJECTIVE":
        a[b] = adjective
    if x == "NOUN" and lock:
        a[b] = noun
        lock = False
    if x == "VERB":
        a[b] = verb
    if x =="NOUN":
        a[b] = noun1
    b += 1
with open(f"{Path.home()}/Testing/sen.txt", "w") as f:
    f.write(' '.join(a))
    f.close()