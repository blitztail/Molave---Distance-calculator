#This lets us use the math library and use code such as pow,and sqrt
import math


#this makes the user input the coordinates of the first point
x1 = int(input ("Enter the x axis of your first point") )
y1 = int(input ("Enter the y axis of your first point") )

#this makes the user input the coordinates of the  second point
x2 = int(input ("Enter the x axis of your second point") )
y2 = int(input ("Enter the y axis of your second point") )

#the solution shows how to calculate the distance
The_solution = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#this shows the user the distance of the the first point and the second point
print("the distance between your first point and your second point is", The_solution)

""""After this activity i have learned how to use terms like import,sqrt,pow and ect. This activity expanded my knowledge in coding, libraries and predefined functions. I learned from my mistakes and made use of them to get a better and cleaner results"""