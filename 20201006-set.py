import random

a = []

for i in range(1,8):
    x = random.randint(1,49)
    b = a.append(x)
    s = list("ooooppy")

y = dict(zip(s,a))


print(a)
print(s)
print(y)
# for n in s:
# 	print(n)
# '''
# 로또번호 추첨하듯이 안에 있는 걸 랜덤하게 끄집어낸다고 생각하면 된다.
# '''