#/Users/PythonBeginner/Lesson1$ python dist.py
#Point A, X Coordinate: 234
#Point A, Y Coordinate: 34
#Point B, X Coordinate: 27
#Point B, Y Coordinate: 114
#The distance between the points A and B is 221.92
#
ax=abs(int(input('Point A,X Coordinate:')))
ay=abs(int(input('Point A,Y Coordinate:')))
bx=abs(int(input('Point B,X Coordinate:')))
by=abs(int(input('Point B,Y Coordinate:')))
import math
def Distance (ax, ay, bx, by):
    dist = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
    result=round (dist, 2)
    print ('The distance between the points A and B is '+ str(result))
Distance (ax, ay, bx, by)