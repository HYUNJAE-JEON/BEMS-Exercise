lst = [0,3,6,9]

lst.sort(reverse=True)
print(lst)

lst = list(range(9,-1,-3))
print(lst)

a = list(range(10))

print(a[9::-3])

#filter를 사용하려면 함수가 있어야한다. filter는 참,거짓을 반환하는 값을 주면 된다.

def odd(x):
    return x%3 == 0
x = list(filter(odd, a))
print(x)

print(list(filter(lambda x: x%3 == 0, a)))

#map은 연산하는 함수가 있어야한다. filter랑은 다르다.

a = list(range(4))
print(list(map(lambda x: x *3, a)))

# def convertsquaremeter(a):
#     return a * 3.305785
#
# squaremeter = eval(input("평수를 입력해주세요: "))
# x = convertsquaremeter(squaremeter)
# print(squaremeter,"평은 ",x,"m^2입니다.")

# def multiplication_table():

for n in range(1,10):
    gu = []
    x = 2
    result = x * n
    gu.append(result)
print(gu)
