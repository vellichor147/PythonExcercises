# 1.Convert decimal number to binary number
"""
Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number.
(1024 ,516, 256, 128, 64, 32, 16, 8, 4, 2, 1)

Examples
binary(1) ➞ "1"
binary(5) ➞ "101"
binary(10) ➞ "1010"


Notes
Numbers will always be below 1024 (not including 1024).
If a binary conversion for 0 is attempted, return "0".
"""
def binary(num):
    if num == 0:
        print(0)
    else:
        list = [None]*11    #creates empty list with 11 None elements
        x = 1024
        for n in range(0,11):
            list[n] = x
            x= x/2
        #print(list)
        binary = ""

        #convert to binary
        for n in list:
            if n > num:
                binary += "0"
            else:
                num -= n
                binary += "1"

        #remove zeros from beginning
        length = len(binary)
        while binary[0] == "0":
            x = 0
            binary = binary[x+1:length]
            x +=1
        print(binary)

# 2.
"""
Find ASCII Charcode of Inverse Case Character
Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.

Examples
Given that:
  - "A" char code is: 65
  - "a" char code is: 97

counterpartCharCode("A") ➞ 97

counterpartCharCode("a") ➞ 65
Notes
The argument will always be a single character.
Not all inputs will have a counterpart (e.g. numbers), in which case return the inputs char code.
"""