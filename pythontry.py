import numpy as np

x = [5,7,-2,2]
y = [4,5,12,0]

np.array(x)*np.array(y)
c=0
d=0
a="Nice computation"

for n in range(len(x)):
    c = c + x[n]
    d = d + y[n] 
  
print("c equals {}, while d equals {}. {}.".format(c,d,a))

print('the test works???')
