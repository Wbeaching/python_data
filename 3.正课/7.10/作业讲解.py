
#1.计算0~100之和
num =0
for x in range(0,101):
    num +=x
print(num)
#2.计算n的n次方
n = input('输入一个值')
n = int(n)
if n ==0:
    print(0)
else:
    for x in range(n+1):
        x=x*(n+1)
    print(x)

#3.鸡兔同笼，笼子里一共有32个头，96条腿，问各有几只。
for x in range(33):
    for y in range(33):
        if x + y == 32 and x*2+y*4 == 96:
            print(x,y)
#4.有一百只马，一百单货物，大马一只可以驼三担，中马可以驼两担，两只小马托一担，问各有几只马。












