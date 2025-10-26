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

#pie chart
hours_studied = [1,2,0.5,1.5,2,0.5,0.2]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
colours = ["red", "blue", "black", "green", "yellow", "maroon", "orange"]
plt.pie(hours_studied, labels = days, autopct = "%1.1f%%", colors = colours, startangle = 90, shadow = True, counterclock = False)
plt.show()

#stack plot
History = [78, 100, 13, 56, 100]
Computing = [70, 100, 1, 91, 87]
English = [78, 100, 15, 67, 75]
DT = [89, 100, 20, 74, 62]
Subjects = ["History", "Computing", "English", "DT"]
Students = ["Kalp", "Harsha", "Harry", "Ryan","Alex"]
plt.stackplot(Students, History, Computing, English, DT, labels = Subjects)
plt.legend()
plt.show()

#scatter graph
x = [1,5,2,6,7,9,8]
y = [6,3,7,1,5,8,2]
plt.scatter(x,y, color = "black", marker = "2", label = "Scatter plot", s = 150)
plt.show()