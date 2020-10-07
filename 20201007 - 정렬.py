>> >

def inv(x):
    return -x

>> > li.sort(key=inv): li
SyntaxError: illegal
target
for annotation
    >> > li.sort(key=inv);
    li
[91, 90, 89, 67, 45, 41, 33, 32, 23, 22, 10]
>> > li[1]
90
>> > li[1].split()
Traceback(most
recent
call
last):
File
"<pyshell#38>", line
1, in < module >
li[1].split()
AttributeError: 'int'
object
has
no
attribute
'split'
>> > li[1].reverse()
Traceback(most
recent
call
last):
File
"<pyshell#39>", line
1, in < module >
li[1].reverse()
AttributeError: 'int'
object
has
no
attribute
'reverse'
>> > li.sort(reverse=True)
>> > li
[91, 90, 89, 67, 45, 41, 33, 32, 23, 22, 10]
>> >

def inv(x):
    x

>> >

def oneth(x):
    return x % 10

>> > li.sort(key=oneth);
li
[90, 10, 91, 41, 32, 22, 33, 23, 45, 67, 89]
>> >

def odd(x):
    return x // 2

>> > li.sort(key=odd);
li
[10, 22, 23, 32, 33, 41, 45, 67, 89, 90, 91]
>> >

def odd(x):
    return x % 2

>> > li.sort(key=odd);
li
[10, 22, 32, 90, 23, 33, 41, 45, 67, 89, 91]
>> >

def odd(x):
    return x % 2 == 0

>> > li.sort(key=odd);
li
[23, 33, 41, 45, 67, 89, 91, 10, 22, 32, 90]