#Write a python code to find LCM and GCM of a given list

import math

def find_lcm(x, y):
    return x * y // math.gcd(x, y)

def find_gcd(x, y):
    return math.gcd(x, y)

def lcm_of_list(num_list):
    lcm = num_list[0]
    for i in range(1, len(num_list)):
        lcm = find_lcm(lcm, num_list[i])
    return lcm

def gcd_of_list(num_list):
    gcd = num_list[0]
    for i in range(1, len(num_list)):
        gcd = find_gcd(gcd, num_list[i])
    return gcd

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("LCM of the numbers:", lcm_of_list(numbers))
print("GCD of the numbers:", gcd_of_list(numbers))
