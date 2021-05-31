import sys

# 1. Write a Python program to sum all the items in a list.
def sumList():
    list = [1,2,3,4,5]
    print(list)
    x = 0
    for n in list:
        x += n
    print("Sum of list: " + str(x))
    xy = sum(list)
    print("Or use sum(list) : " + str(xy))

# 2.Write a Python program that multiplies all the items in a list.
def mulitpyList():
    list = [1,2,3,4,5]
    print("List: " + str(list))
    x = 1
    for n in list:
        x *= n
    print("Product of list: {}".format(x))

# 3.Write a Python program to get the largest number from a list.
def maxInList():
    list = [1,7,3,4,5]
    print("List: " + str(list))
    largest = 0
    for n in list:
        if n > largest:
            largest = n
    print("Largest element in list is: {}".format(largest))
    # or use max() function
    print("Using max() function: {}".format(max(list)))

# 4. Write a Python program to get the smallest number from a list.
def minInList():
    list = [16,7,3,4,5]
    print("List: " + str(list))
    smallest = sys.maxsize
    for n in list:
        if n < smallest:
            smallest = n
    print("Min element of list is: {}".format(smallest))
    # or use min() function
    print("Using min function(): {}".format(min(list)))

# 5. Write a Python program to count the number of strings where the string length is 2 or
#    more and the first and last character are same from a given list of strings
"""
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
def countStrings():
    list = ['abc', 'xyz', 'aba', '1221']
    list2 = [0] * len(list)
    counter = 0
    for n in list:
        if len(n) > 2:
            if n[0] == n[-1]:
                list2[counter] = n
                counter += 1
    x = 4 - counter
    for n in range(x):
        list2.pop()
    print("Strings: {}".format(list2))
    print("Result: " + str(counter))

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a
# given list of non-empty tuples.
"""
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
def getLast(tuple):
    return tuple[-1]

def sortByLastTuple():
    sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sortedSample = sorted(sample, key=getLast)
    print(sortedSample)

# 7. Write a Python program to remove duplicates from a list.
def removeDuplicates():
    sample = [1,13,2,15,1,16,7,7]
    print("Sample list: " + str(sample))
    x = set(sample)
    print("Set made of sample list: " + str(x))
    for n in x:
        if sample.count(n) > 1:
            for m  in range(2):
                sample.remove(n)
    print("List after removing duplicates: " + str(sample))

# 8. Write a Python program to check a list is empty or not.
def checkEmpty():
    list = []
    list2 = [1,2]
    checkList = list2
    if len(checkList) != 0:
        print("List is not empty!")
    else:
        print("List is empty")

#   9. Write a Python program to clone or copy a list.
def cloneList():
    sample = [1,13,2,15,1,16,7,7]
    new_list = []
    for n in sample:
        new_list.append(n)
    print("For loop: {}".format(new_list))
    #or
    list_clone =sample.copy()
    print(".copy() : {}".format(list_clone))

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

# 11.Write a Python function that takes two lists and returns True if they have at least one common member.
def commonMember():
    sample1 = [1,2,3,4,5]
    sample2 = [1,12,13,1,5]
    counter = 0
    for n in sample1:
        for m in sample2:
            if n == m:
                print("m: {0}, n:{1}".format(m,n))
                print("True")

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
"""
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""
def remove045():
    sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print("List: {}".format(sample))
    sample.pop(0)
    sample.pop(3)
    sample.pop(3)
    print("List after removing elements: {}".format(sample))

