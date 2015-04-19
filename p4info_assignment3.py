import os
import sys

hours = input("Enter hours: ")
rate = input("Enter rate: ")
hours = float(hours)
rate = float(rate)

if hours <= 40:
    pay = float(hours)*float(rate)
else:
    basic_pay = 40*rate
    extra_pay = (hours - 40)*1.5*rate
    pay = basic_pay + extra_pay

print ("Pay: %.2f" % pay)