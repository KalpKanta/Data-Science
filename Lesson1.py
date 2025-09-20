import numpy as np
import time

num = [1,3,5,6,7,9]
print(num)
print(type(num))
array = np.array(num)
print(array)
print(type(array))
num1 = np.arange(1,100)
print(num1)

list =  []
t1 = time.time()
for i in range(0, 10000000):
    list.append(num1)
t2 = time.time()

t3 = time.time()
array1 = np.arange(0,10000000)
t4 = time.time()

print(t2 - t1)
print(t4 - t3)



array = np.arange(1,51)
print(array)
z1 = np.zeros(5, int)
print(z1)
z2 = np.zeros(5, float)
print(z2)
o1 = np.ones((5,3), int)
print(o1)

print(o1.ndim)
print(z1.ndim)
print(z2.ndim)
#ndim gives the dimentionsof the array e.g o1 is 2 dimensional

print(o1.shape)
print(z1.shape)
print(z2.shape)
#shape gives the rows and colums for an array if it is one dimensional then it will only show the rows

print(o1.size)
print(z1.size)
print(z2.size)
#size gves the total amount of values in an array

array = np.arange(1,51,5)
print(array)

array2 = np.linspace(10, 20, 6)
print(array2)
 
array1 = np.random.randint(1,100,5)
print(array1)

array3 = array2.reshape((3,2))
print(array3)

#sorting - 
array4 = np.random.randint(1, 100, 10)
print(array4)
array4n = np.sort(array4)
print(array4n)

#slicing - 
print(array4[2:5:1])
print(array4[0:5:1])
print(array4[:5:])
print(array4[::])
print(array4[::-1])

#conditional slicing - 
print(array4[[3,4,7,1,2,5]]) #not conditional slicing (selective indexes)
print(array4[array4%2 == 0])
print(array4[(array4>50) & (array4%2==0)])
array5 = np.arange(1, 9)
array5 = array5.reshape(2,4)
print(array5[0, 1:3])

x = np.arange(1,5)
y = np.arange(11,15)

print(x+y)
print(x-y)
print(x*y)
print(x/y)