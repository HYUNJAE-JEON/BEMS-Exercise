inflobj = open("Day04_02.py",encoding ="utf8")
S10 = inflobj.read(100)
print(S10)
print("-"*70)

S = inflobj.read
print(S)
print("-"*70)

inflobj = open("Day04_02.py",encoding ="utf8")
L = inflobj.readlines()
print(L)


def divide(x, y):
    try:
        result = x / y
    except Exception as e:
        print(e, "Divide by zero.")

    # 에러도 부모 자식 간의 관계가 있기 때문에 Exception을 적게 되면 에러를 포괄할 수 있다.

    else:
        print("Result is", result)
    finally:
        print("Finally, Always execution.")


divide(2, 3)
divide(4, 5)
divide(1, 0)
divide(20384702834, 8329)


def unused_1():
    try:
        raise KeyboardInterrupt
    finally:
        print('Good bye~!')


def unused():
    while 1:
        try:
            x = int(input("Please enter a number: "))
        # break
        except ValueError:
            print("Not a valid number")



import pickle

def unused():
    with open('pydata.pickle','wb') as pystore:
        pickle.dump([1, 12, 13, "a"], pystore)

l = [3,4,7]
with open('pydata.pickle', 'rb') as pyload:
     l = pickle.load(pyload)
print(l)
