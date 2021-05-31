import sys
import datetime
import math
import calendar

# 1. Twinkle twinkle
"""
Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

Output :
Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""
def twinkle():
    print("Twinkle, twinkle, little star,\n \t How I wonder what you are!\n"
          "\t \t Up above the world so high,\n"
          "\t \t Like a diamond in the sky.\n"
          "Twinkle, twinkle, little star,\n \t How I wonder what you are" )

# 2. Write a Python program to get the Python version you are using.
def version():
    print("Pyhton version:")
    print(sys.version)
    print("Pyhton version info:")
    print(sys.version_info)

# 3. Write a Python program to display the current date and time.
"""
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
def dateTime():
    now = datetime.datetime.now()
    print("Current date and time: {}".format(now.strftime("%d-%m-%Y %H:%M:%S")))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
"""
Sample Output :
A=pi*r^2
"""
def areaCircle():
    radius = float(input("Enter radius of circle: "))
    area = math.pi*(radius**2)
    print("Area of circle: {0}".format(area))

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
def reversedName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    print(last + " " + first)

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
"""
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
def makeListTuple():
    numbers = input("Enter numbers separated by comma: ")
    list = numbers.split(",")
    tuple1 = tuple(list)
    print('List : ',list)
    print('Tuple : ',tuple1)

# 7. Write a Python program to accept a filename from the user and print the extension of that.
"""
Sample filename : abc.java
Output : java
"""
def fileExtension():
    file = input("Enter file name with extension: ")
    file = file.split(".")
    print(file[1])

# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
def firstLastColor():
    cl = ["Red","Green","White" ,"Black"]
    print("First color: {0}, last color: {1}".format(cl[0],cl[3]))

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
"""
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
def examinationSchedule():
    ed = (11, 12, 2014)
    print("The examination will start from : {0} / {1} / {2}".format(ed[0],ed[1],ed[2]))


# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""
Sample value of n is 5
Expected Result : 615
"""
def nnn(n):
    output = n+n*n+n*n*n
    print(output)

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
"""
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""
def documnets():
    print(abs.__doc__)

# 12. Write a Python program to print the calendar of a given month and year.
"""
Note : Use 'calendar' module.
"""
def calendar():
    m = int(input("Enter month: "))
    y = int(input("Enter year: "))
    print(calendar.month(y,m))