from time import time

def curious_fraction(x,y):
    result = False
    xstr = list(str(x))
    ystr = list(str(y))
    if x%10!=0 and y%10!=0 and len(xstr)>1 and x<y:
        for digit in xstr:
            try:
                ystr.remove(digit)
                xstr.remove(digit)
            except ValueError:
                pass
        if len(ystr)==1:
            x2 = int(xstr[0])
            y2 = int(ystr[0])
            if float(x*y2)/(y*x2)==1:
                result = True
    return result

start = time()
iproduct = 1
jproduct = 1
for i in range(11,99):
    for j in range(i+1,100):
        if curious_fraction(i,j):
            iproduct *= i
            jproduct *= j
div = 2
while div<=iproduct:
    if iproduct%div==0 and jproduct%div==0:
        iproduct /= div
        jproduct /= div
    else:
        div += 1

print(jproduct)
print(time()-start)
