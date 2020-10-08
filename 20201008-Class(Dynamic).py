def Mymyclass():
    class Myclass:
        "A simple example class"
        __i = 123
        def f(self):
            return "hello world"
        print(Myclass._Myclass__i)
Myclass()

# __ 밑줄 2개는 속성을 숨기는 방법이다.

def unused2():
    class Myclass:
        "A simple example class"
        i = 123
        # init은 생성자 함수로 객체를 만들어지는 시점에서 처리가 된다.
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart
        #self는 무시하면 되고 self 뒤에 있는 인자들은 무시하면 안된다.
        def f(self):
            return 'hello world'
    c = Myclass(2,3) #instnatiation (=create object) #인자를 뒤에 전달해주어야한다.
    c.counter = 1

    # 클래스 내용 안에 counter 라는 변수가 없었는데 동적으로 만들 수 있다.
    # 값을 읽어서 변환시킬 수 있고 만들었다 지웠다 쓸 수 있다.
    # 실행시간에 이것저것 변화할 수 있는 것을 동적이라고 이야기한다.
    # 파이썬의 단점이면서 장점이다. 유연하게 동작하는데 유연하게
    # 동작하는 건 어떻게 동작할지 모른다고 볼 수 있다.
    # 물렁물렁한 지점토 느낌이다. 3.0 블루투스에 대한 코드에서 4.0으로 업그레이드가 되었을 때도
    # 동적인 부분을 활용해 기존 객체를 바꾸지 않고 사용이 가능하다.

    while c.counter < 10:
        print(c.counter, end =" ")
        c.counter +=1
    print("before\n",c.counter)
    del c.counter
    print("after\n",c.counter) #error
    print(c.r)
    print(c.i)
    print(Myclass.i)


def unused_1():
    print(Myclass.i)
    y = Myclass
    print(y.f(x))
    print(y.i)
    x = Myclass()
