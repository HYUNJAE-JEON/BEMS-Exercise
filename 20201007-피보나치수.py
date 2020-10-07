def fibo(x):
    if x < 2:
        return x
    return fibo(x-1) + fibo(x-2)

x = int(input("숫자를 입력해주세요: "))



def fibo1(n):
    a, b = 0, 1
    for _ in range(n) :
        print(a, end=" ")
        a, b = b, a+b
    print()

fibo1(10)

for x in range(x):
    print(fibo(x), end=" | ")

# fibo는 재귀함수로 만든 거고 fibo1은 재귀함수가 아닌 것으로 만든 피보나치 수이다.