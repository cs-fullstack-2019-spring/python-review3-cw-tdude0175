def main():
    problem1()
    # problem2()
    # problem3()
    # problem4([10, 3, 5, 6])

# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is less or equal to 1,
# or greater or equal to 10. Print the result returned from your function.
#
# BONUS: Get the number and outside_mode flag from User input instead of hardcoding it
#
# def in1to10(n, outside_mode):
#
# Examples of Expected Output:
# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True



# i'm a bit confused but i think i get it?
# if and elif for comparison


def problem1():
    number = int(input("number to compare\n"))
    mode_flag = input("True or False?\n")
    if number > 10:
        result = False
    elif number <0:
        result = False
    else:
        result =True
    if mode_flag.lower() == "true":
        mode_flag = True
    elif mode_flag.lower() == "false":
        mode_flag = False
    # flag tells it to test for inside or outside of range

    if(result == True and mode_flag ==True):
        print(f"{number} is {result}")
    elif(result == True and mode_flag == False):
        print(f"{number} is {mode_flag}")
    elif(result == False and mode_flag == False):
        print(f"{number} is {True}")
    elif(result == False and mode_flag == True):
        print(f"{number} is {result}")

# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
#
# Once the user enters the equal sign to quit,
# print all the strings that were entered as one line with each word separated by a comma and space.
#
# Example of Expected Output:
# You, Entered, These, Words, Today

# use join to bring them back together [ ' seperator between elements ' . join(array you wish to combine)
# works just like .reduce in javascript


def problem2():
    userInput = ""
    stringCollection = []
    while(userInput != "="):
        userInput = input("enter word.\n")
        if userInput != "=":
            stringCollection.append(userInput)
#     gathers strings into collection. Way to check for space? only one string allowed?
    print( " , ".join(stringCollection))
#     join can bring them together

# Given a non-negative number "num",
# return True if num is within 2 of a multiple of 10.
# Print the result from your function.
#
# BONUS: Get the number from User input instead of hardcoding it
#
# def near_ten(num):
#
# Examples of Expected Output:
# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True

def problem3():
    userInput = int(input("number within 2 of divsible by 10\n"))
    if (userInput-2)%10 == 0:
        print("True")
    elif(userInput+2)%10 == 0:
        print("True")
    elif(userInput-1)%10 == 0:
        print("true")
    elif(userInput-1)%10 == 0:
        print("true")
    elif(userInput%10 == 0):
        print("true")
    else:
        print("False")

# Given an array length 1 or more of ints,
# return the difference between the largest and smallest values in the array.
# Note: There isn't any restriction on how your approach determining what the min and max values are.
#
# def big_diff(nums):
#
# Examples of Expected Output:
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

# defining the start is not that hard
def problem4(list):
    firstNumber = 0
    secondNumber = 0        # set start with 0 since no negative numbers
    for number in list:
        if(number > firstNumber):
            firstNumber = number            # use biggest number to define both for easier comparability
            if secondNumber == 0:
                secondNumber = firstNumber
        if(number < secondNumber):  #put an if statement inside if so it cannot replace constantly
            secondNumber = number
    print(firstNumber - secondNumber)



if __name__ == '__main__':
    main()
