import numpy as np
from numpy import linalg as geek
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[3,4,5],[4,3,6],[8,9,0]])
#dimension of array
k=a.ndim
#shape of array
p=a.shape
#size of array
l=a.size
#trace of array
s=a.T
#sum of array
q=a.sum()
#maximum element of the array
u=a.max()
#manimum element of the array
e=a.min()
#square root
z=np.sqrt(a)
#exponential
y=np.exp(a)
#0th index of the second element
r=a[0,2]
#vertical stacking
g=np.vstack((a,b))
#horizontal stacking
h=np.hstack((a,b))
#determinant
d=np.linalg.det(a)
#rank
t=np.linalg.matrix_rank(a)
#inverse
w=np.linalg.inv(a)
#eigen value
j=geek.eigh(a)
#trace
o=np.trace(a)
#sort
e=np.sort(b)
#log
i=np.log(a)
#multiplication
c=(a*b)
#division
v=(a/b)
print 'dimensions of array:',k
print'shape of array:',p
print 'size of array:',l
print 'transpose of array:',s
print 'sum of array:',q
print 'max of array:',u
print 'min of array:',e
print 'square root:',z
print 'slicing:',r
print 'exponential:',y
print 'vertical stacking:',g
print 'horizontal stacking:',h
print 'determinant:',d
print 'rank:',t
print 'inverse:',w
print 'eigen values:',j
print 'Trace:',o
print 'sort:',e
print 'logarithmic:',i
print 'eigen values:',j
print 'trace:',o
print 'sort:',e
print 'logarithmic:',i
print 'multiplication:',c
print 'division:',v

