x1,y2=map(int,input().split())
temp3=0
if(x1>y2) or (x1<y2):
    temp3=x1
    x1=y2
    y2=temp3
print(x1,y2)
