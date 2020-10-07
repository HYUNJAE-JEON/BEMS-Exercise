n=1
while n <9:
    n += 1
    print("--",n,"단--")
    x = 0
    while x <9:
        x += 1
        print(n,"*",x, "=", n*x)

for n in range(2,10):
    print("--",n,"단--")
    for x in range(1,10):
        print(n,"*", x,"*", n*x)
    print()