y1=1
y2=1
z=0
while y2<4000000:
    y2=y1+y2
    y1=y2-y1
    if (y2%2==0):
     z=z+y2
print(z)