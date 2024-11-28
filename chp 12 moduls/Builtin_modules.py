
# ==============================
# Statistics Module
# ==============================
# The statistics module provides functions for mathematical statistics of numeric data.
# Popular functions:
# - mean: Returns the average of a list of numbers
# - median: Finds the middle value in a sorted list
# - mode: Finds the most frequent value in the list
# - stdev: Calculates the standard deviation

from statistics import *  # Importing all statistics functions

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print("Statistics Module Outputs:")
print(f"Mean: {mean(ages)}")      # ~22.9
print(f"Median: {median(ages)}")  # 23
print(f"Mode: {mode(ages)}")      # 20
print(f"Standard Deviation: {stdev(ages)}\n")  # ~2.3

# ==============================
# Math Module
# ==============================
# The math module contains many mathematical operations and constants.
# Constants and functions:
# - pi: Value of π
# - sqrt: Square root of a number
# - pow: Exponential calculations
# - floor: Rounds down to the nearest integer
# - ceil: Rounds up to the nearest integer
# - log10: Logarithm to base 10

import math

print("Math Module Outputs:")
print(f"Pi: {math.pi}")                 # 3.141592653589793
print(f"Square Root of 2: {math.sqrt(2)}")  # 1.4142135623730951
print(f"2^3: {math.pow(2, 3)}")         # 8.0
print(f"Floor of 9.81: {math.floor(9.81)}")  # 9
print(f"Ceil of 9.81: {math.ceil(9.81)}")    # 10
print(f"log10(100): {math.log10(100)}\n")    # 2

# Importing specific functions for clarity
from math import pi, sqrt, pow, floor, ceil

print("Math Module (Selective Imports):")
print(f"Pi: {pi}")                  # 3.141592653589793
print(f"Square Root of 2: {sqrt(2)}")  # 1.4142135623730951
print(f"2^3: {pow(2, 3)}")          # 8.0
print(f"Floor of 9.81: {floor(9.81)}") # 9
print(f"Ceil of 9.81: {ceil(9.81)}\n") # 10

# Renaming imports for convenience
from math import pi as PI
print("Renamed Import Example:")
print(f"Renamed Pi as PI: {PI}\n")  # 3.141592653589793

# ==============================
# String Module
# ==============================
# The string module provides constants related to string operations:
# - ascii_letters: All ASCII letters (lowercase and uppercase)
# - digits: All numeric digits (0-9)
# - punctuation: All punctuation characters

import string

print("String Module Outputs:")
print(f"ASCII Letters: {string.ascii_letters}")  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(f"Digits: {string.digits}")                # 0123456789
print(f"Punctuation: {string.punctuation}\n")   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# ==============================
# Random Module
# ==============================
# The random module is used to generate random numbers.
# Functions:
# - random(): Generates a random float between 0 and 0.999...
# - randint(a, b): Generates a random integer between a and b (inclusive)

from random import random, randint

print("Random Module Outputs:")
print(f"Random Float: {random()}")          # A random float between 0 and 0.999...
print(f"Random Integer (5-20): {randint(5, 20)}")  # A random integer between 5 and 20 (inclusive)
