
# Ethan E. Lopez
# 002425516
# etlopez@chapman.edu
# CPSC 230 - Section 2
# Program Assignment 4

def print_sorted(integers_list):
# defines print_sorted function with argument integers_list
    integers_list.sort()
    # calls sort method to sort integers_list in ascending order
    print('Sorted list:', integers_list)
    # prints 'Sorted list:' followed by the sorted integers_list

def compute_mean(integers_list):
# defines compute_mean function with argument integers_list
    u = sum(integers_list) / len(integers_list)
    # calculates mean (u) by taking the sum of all integers in integers_list and dividing by
    # the count of numbers or the length of integers_list
    return u
    # returns mean of integers_list as the final value

def compute_variance(integers_list):
# defines compute_variance function with argument integers_list
    y = 0
    # assigns substitute value y as 0
    for i in integers_list:
    # creates a for loop for every integer i in integers_list
        j = (i - compute_mean(integers_list)) ** 2
        # computes a single point in the numerator of variance
        # takes integer i and subtracts it from the mean called from the compute_mean function
        # distance from the mean is squared
        y += j
        # with variable y adding j each time, this stores the sum of all squared distances from the mean
        # value of numerator

    o = y / len(integers_list)
    # calculates variance value with sums of squared distance y divided by integers_list length / number of terms
    return o
    # returns variance of integers_list as the final value
    
def compute_standard_dev(integers_list):
# defines compute_standard_dev function with argument integers_list
    s = (compute_variance(integers_list)) ** 0.5
    # assigns s as the square root of value variance
    # pre-calculated variance is called with compute_variance function
    # this value is raised to 0.5 (the power of 1/2) to substitute as square root
    return s
    # returns the standard deviation of integers_list as the final value
        
integers_list = []
# creates an empty list integers_list to hold future values

x = input('Please enter an integer: ')
# assigns variable x with user entered input as a string

while True:
# creates a while loop for variable x
    if x.startswith('-'):
    # evaluates if string x starts with -
        if x[1:].isdigit():
        # confirms if string x is a number starting with -, thus a negative number
            break
            # breaks loop when a negative number is input in variable x
        else:
        # confirms string x is not a number starting with -, thus an invalid string
            print('Invalid')
            # prints Invalid
            x = input('Please enter an integer: ')
            # asks the user for other string input and reassigns variable x
    elif x.isdigit():
    # evaluates if string x is an integer greater than or equal to 0
        x = int(x)
        # converts string x into integer form
        integers_list.append(x)
        # adds value integer x into integers_list
        x = input('Please enter an integer: ')
        # asks the user for other string input and reassigns variable x
    else:
    # evaluates if string x is not an integer > or = 0 or a string that starts with -
        print('Invalid')
        # prints Invalid
        x = input('Please enter an integer: ')
        # asks the user for other string input and reassigns variable x

print_sorted(integers_list)
# calls print_sorted function with argument integers_list created from while loop
# print_sorted(integers_list) prints integers_list in ascending form
print('Mean:', compute_mean(integers_list))
# calls compute_mean function with argument integers_list and prints mean
# the print statement prints Mean: followed by the result of compute_mean(integers_list)
print('Standard Deviation:', compute_standard_dev(integers_list))
# calls compute_standard_dev function with argument integers_list and prints standard deviation
# the print statement prints Standard Deviation: followed by the result of compute_standard_dev(integers_list)
