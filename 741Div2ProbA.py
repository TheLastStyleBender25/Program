def mod(a,b):
 while b>=a:
    for i in range(a,b+1):
        s=b%i
        z.append(s)
        if len(z)==2:
            if z[0]>z[1]:
                z.pop(1)
            else:
                z.pop(0)
    b-=1
 ss.append(z[0])
    
t=int(input())
z=[]
ss=[]
for i in range(t):
    a,b=map(int,input().split())
    if a>b:
        temp=b
        b=a
        a=temp
    mod(a,b)
    z.clear()

for i in range(0,len(ss)):
    print(ss[i])