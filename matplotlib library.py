''' 
Matplotlib is a popular Python library used for creating graphs, charts, and data visualizations.

It helps you display data visually using:

Line graphs
Bar charts
Pie charts
Histograms
Scatter plots
'''

import matplotlib.pyplot as plt
#this library will help us to plot or made visualize diagrams#


##----creating a line plot----##
x= [1,2,3,4,5]
y=[1,4,9,16,25]
plt.plot(x,y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('a random line plot')
plt.show()
##output:  as an output it will show you an entire ploted graph##



##----coustomizing line plot----##
plt.plot(x,y, color='yellow', linestyle='--',marker='o', linewidth=2,markersize=9)
plt.grid(True)
##def: the linestyle will change the desing of the line and the marker will make pointers on the plots



##----multiple plots----##
x1=[1,2,3,4,5]
y1=[10,20,30,40,50]
y2=[16,17,18,19,21]
''''''
plt.subplot(2,2,1)
plt.plot(x1,y1,color='red')
plt.title("plot no. 1")
''''''
plt.subplot(2,2,2)
plt.plot(y1,y2,color='green')
plt.title("plot no. 2")
''''''
plt.subplot(2,2,3)
plt.plot(x1,y2, color='yellow')
plt.title("plot no.3")
##output:  this will give us 3 graphs in total arrange in a series 
##plt.subplot(rows, columns, position)



##----creating bar plot----##
categories=['a','b','c','d','e']
values=[5,7,9,3,2]
plt.bar(categories,values,color='purple')
##output:  this will give us a bar graph 



##----creating histogram----##
#It groups numbers into ranges called bins and shows how many values fall in each range.
data=data=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(data,bins=5,color='black',edgecolor='orange')



##----creating scatter plot----##
#no lines will be drawn just data points will be scatted on plots
x=[1,2,3,4,5]
y=[6,7,8,9,10]
plt.scatter(x,y,color='pink', marker='*')



##----creating pychart----##
labels=['a','b','c','d']
size=[30,20,40,10]
colors=['pink','yellowgreen','lightcoral','lightskyblue']
explode=[0.2,0,0,0]#move a slice slightly away from the center to highlight it. in our eg only 1st will move cause others are 0

plt.pie(size,labels=labels, colors=colors, autopct="%1.1f%%", shadow=True)
