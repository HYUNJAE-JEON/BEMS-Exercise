class Bag:
    def __init__(self):
        self.data =[]
    def add(self, x):
        self.data.append(x)
    def __repr__(self):
        return "This is Louie vuiton"
    # 클래스 객체에 대한 설명이 필요할 때 이렇게 설명 가능하다.
    def __str__(self):
        return "This is Calvin"
    def __add__(self,x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)


l = Bag()
print(l)
l.add("ring")
l.addtwice("coupone")
l + "necklace"
print(l.data)


# + 기호는 __add__ 이고, - 기호는 __sub__이다.
# * 기호는 __mul__ 이고, / 기호는 __div__이다.
# += __iadd__ -= __isub__ ~~~
