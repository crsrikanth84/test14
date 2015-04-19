import os
import sys

hours = input("Enter hours: ")
rate = input("Enter rate: ")
hours = float(hours)
rate = float(rate)
pay = float(hours)*float(rate)
print ("Pay: %.2f" % pay)

