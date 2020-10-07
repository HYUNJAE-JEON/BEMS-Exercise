def fact(x):
    if x ==0:
        return 1
    return x*fact(x-1)
x=10
print('\n')
print(x, 'fact(%d)'%x)
print('-'*7)

for n in range(x):
    print(n, fact(n))


# 재귀함수를 사용한 계산

def factorial(x):
    ans = 1
    for i in range(2, x+1):
        ans = ans*i
    return ans

x=10
print('\n')
print(x, 'fact(%d)'%x)
print('-'*7)

for n in range(x):
    print(n, factorial(n), fact(n))


# 재귀함수를 사용하지 않은 계산