import matplotlib.pyplot as plt
import numpy as np

#line graph
x = np.arange(0,10,1)
print(x)
y = x + 2
print(y)
plt.xlabel("x axis")
plt.ylabel("y axis")

font1 = {'family':'serif', 'color':'red', 'size':20}
plt.title("Example graph", loc = "center", fontdict = font1)
#single dash makes a solid line and double dash dashed line,  colon is also used to make a dotted line

plt.plot(x, y, "g2-")
plt.show()

#bar graph
x = [1,4,5,7,8,10,11,14]
y = [2,5,3,6,5,9,7,8]
plt.xlabel("x axis")
plt.ylabel("y axis")
font2 = {'family':'serif', 'color':'blue', 'size':15}
plt.title("Example graph", loc = "center", fontdict = font2)
plt.bar(x,y)
plt.show()

#another one
x = [1,2,3,4]
y = [2,5,3,6]
plt.barh(x,y)
plt.show()

#histogram
age = np.random.randint(0,50,100)
bins = [0,10,20,30,40,50]
plt.hist(age, bins, rwidth = 0.8)
plt.show()