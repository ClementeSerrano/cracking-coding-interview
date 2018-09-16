# Problem 1
'''
We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.

In the Gregorian calendar three criteria must be taken into account to identify leap years:

1. The year can be evenly divided by 4, is a leap year, unless:
1.1. The year can be evenly divided by 100, it is NOT a leap year, unless:
1.1.1. The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

Task:
You are given the year, and you have to write a function to check if the year is leap or not.

Constraints:
1900<=y<=10^5
'''


def is_leap(year):
    leap = False

    if year >= 1900 and year <= 10**5:
        if year % 400 == 0:
            leap = True
        elif year % 4 == 0 and year % 100 != 0:
            leap = True

    return leap


# Problem 2
'''
Read an integer N.

Without using any string methods, try to print the following:

123...N

Note that "..." represents the values in between.

Input Format:
The first line contains an integer N.

Output Format:
Output the answer as explained in the task.
'''


def generate_secuence(n):
    aux_array = []
    for i in range(1, n+1):
        aux_array.append(str(i))
    return ''.join(aux_array)


A = [3, 4, 7, 7, 6, 6]
print(generate_secuence(20))
