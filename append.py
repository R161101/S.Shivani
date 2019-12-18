import numpy as np
a=np.asarray([1,2,3])
b=np.asarray([4,5,6])
l=len(a)
for i in range(0,l):
       b=np.append(b,a[i])
print b
