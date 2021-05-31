from math import pi

# 1.Stuttering Function
'''
Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ... and space after each,
and then the word is pronounced with a question mark ?.

stutter("incredible") ➞ "in... in... incredible?"
stutter("enthusiastic") ➞ "en... en... enthusiastic?"
stutter("outstanding") ➞ "ou... ou... outstanding?"

Notes
Assume all input is in lower case and at least two characters long.
'''
def stutter(string):
    print(string[0:2] + "..." + string[0:2] + "..." + string + "?")

# 2.Radians to Degrees
"""
Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

Examples
radians_to_degrees(1) ➞ 57.3
radians_to_degrees(20) ➞ 1145.9
radians_to_degrees(50) ➞ 2864.8

Notes
The number π can be loaded from the math module with from math import pi.
"""
def radians_to_degrees():
    rad = int(input("Enter radian: "))
    degree = (rad/pi)*180
    print("Degree: {0}".format(degree))

# 3. Curzon Number
"""
Curzon Numbers
In this challenge, establish if a given integer num is a Curzon number. 
If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29
"""
def is_curzon(num):
    x = 2**num + 1
    y = 2*num + 1
    if (x % y) == 0:
        print(True)
    else:
        print(False)

# 4.Luke, I Am Your ...
"""
Luke, I Am Your ...
Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	    Relation
Darth Vader	father
Leia	    sister
Han	        brother in law
R2D2	    droid

Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
relation_to_luke("Leia") ➞ "Luke, I am your sister."
relation_to_luke("Han") ➞ "Luke, I am your brother in law."
"""
def relation_to_luke(string):
    if string == "Darth Vader":
        print("Luke, I am your father.")
    elif string == "Leia":
        print("Luke, I am your sister.")
    elif string == "Han":
        print("Luke, I am your brother in law.")
    elif string == "R2D2":
        print("Luke, I am your droid.")
    else:
        print("Luke, we are not related at all.")

# 5.Speed and damage
"""
Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.

Examples
damage(40, 5, "second") ➞ 200
damage(100, 1, "minute") ➞ 6000
damage(2, 100, "hour") ➞ 720000

Notes
Return "invalid" if damage or speed is negative.
"""
def damage(damage, speed, time):
   if (damage > 0) and (speed > 0):
        if time == "second":
            print(damage*speed)
        elif time == "minute":
            print(damage*speed*60)
        elif time == "hour":
            print(damage*speed*60**2)
   else:
       print("Invalid")

# 6.Return the Factorial
"""
Create a function that takes an integer and returns the factorial of that integer. 
That is, the integer multiplied by all positive lower integers.

Examples
factorial(3) ➞ 6
factorial(5) ➞ 120
factorial(13) ➞ 6227020800

Notes
Assume all inputs are greater than or equal to 0.
"""
def factorial(num):
    f = range(1,num+1)
    result = 1
    for n in f:
        result *= n
    print("Factorial: " + str(result))
















