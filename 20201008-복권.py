import random
Lotto = set()
for i in range(6):
    x = random.randint(1,49)
    Lotto.add(x)
    if x in Lotto:
        x = random.randint(1,49)
    else:
        i += 1
    print(x, end= " ")

# 강사님 코드

ev = set()
while len(ev) <6:
    i = random.randint(1,45)
    ev.add(i)
print(list(ev))