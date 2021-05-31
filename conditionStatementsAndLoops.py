import random

"""
CONDITION STATEMENTS AND LOOPS
"""
# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
def condition1():
    print("Number divisible by 7 and multiples of 5: ")
    for n in range(1500,2701):
        if n%7 == 0 and n%5==0:
            print(n)

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
"""
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""
def celsiusToFahrenheit():
    c = int(input("Enter temperature in Celsius: "))
    f = (9/5)*c+32
    print("Temperature in Fahrenheit: {}".format(f))
    f = int(input("Enter temperature in Fahrenheit: "))
    c = int(((f-32)*5)/9)
    print("Temperature in Celsius: {}".format(c))

# 3. Write a Python program to guess a number between 1 to 9.
"""
Note : User is prompted to enter a guess. 
If the user guesses wrong then the prompt appears again until the guess is correct, 
on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""
def guess19():
    rn = random.randint(1,9)
    x = False
    while x == False:
        num = int(input("Guess number form 1 to 9: "))
        if num == rn:
            x = True
            print("Congratulations, you guessed the number!")
        else:
            print("That's not the number!")

# 5. Write a Python program that accepts a word from the user and reverse it.
def reversedWord():
    word = input("Enter a word: ")
    print(word[::-1])

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers.
"""
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
def countEvenOdd():
    sample = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even = 0
    odd = 0
    for n in sample:
        if n%2==0:
            even += 1
        else:
            odd +=1
    print("Number of even numbers: {}".format(even))
    print("Number of odd numbers: {}".format(odd))

# 7. Write a Python program that prints each item and its corresponding type from the following list.
"""
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
"""
def printType():
    sample = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    for n in sample:
        print(type(n))

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
"""
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5
"""
def zeroSix():
    for n in range(0,7):
        if n==3 or n==6:
            continue
        else:
            print(n)

# 9. Write a Python program to get the Fibonacci series between 0 to 50.
"""
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""
def fibonacci():
    x,y = 0,1
    while y<50:
        print(y)
        x,y = y,x+y

# 10. Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"
def fizzBuzz():
    for n in range(1,51):
        if n%3==0:
            print("fizz")
        elif n%5==0:
            print("buzz")
        elif n%3==0 and n%5==0:
            print("fizzbuzz")
        else:
            print(n)

# 11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
"""
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""
def mnArray():
  m = int(input("Enter number of rows: "))
  n = int(input("Enter number of columns: "))

# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints
# the lines as output (all characters in lower case).
def lowerCase():
    while True:
        line = input("enter line: ")
        if len(line)==0:
            print("You have entered nothing: ")
        else:
            print(line.lower())

# 31. Write a Python program to calculate a dog's age in dog's years
"""
Note: For the first two years, a dog year is equal to 10.5 human years. 
After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
"""
def dogYears():
    dog = int(input("Input a dog's age in human years: "))
    result = 0
    for n in range(1,dog+1):
        if n<=2:
            result += 10.5
        else:
            result += 4
    print("The dog's age in dog's years is {}".format(result))

# 32. Write a Python program to check whether an alphabet is a vowel or consonant.
def vowel():
    vowel = ["a","e","i","o","u"]
    while True:
        letter = input("Enter a letter: ")
        x = vowel.count(letter)
        if x==0:
            print("Letter is a consonant!")
        else:
            print("Letter is a vowel!")

# 33. Write a Python program to convert month name to a number of days.
"""
List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days
"""
def monthDays():
    list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = input("Enter a month: ")
    month = month.lower().capitalize()
    if month == "February":
        print("28/29 days")
    elif month in ("April", "June", "September", "November"):
        print("30 days")
    elif month in ("January", "March", "May", "July", "August", "October", "December"):
        print("30 days")
    else:
        print("you didin't enter month")

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
def int20():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    sum = x+y
    if sum >= 15 and sum<=20:
        print("20")
    else:
        print(sum)

# 35. Write a Python program to check a string represent an integer or not.
def isInteger():
    x = input("Enter string: ")
    bool = x.isnumeric()
    if bool == True:
        print("String is number!")
    else:
        print("String is not a nubmer!")

def test():
    x = b"toni"
    print(type(x))

