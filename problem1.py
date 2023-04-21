#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
import math

while True:
  os.system('cls')
  print("Enter in the coefficients for a quadratic equation in the format:")
  print("  ax^2 + bx + c = 0")

  while True:
    try:
      a = float(input("a: "))
      b = float(input("b: "))
      c = float(input("c: "))
      break
    except ValueError:
      print("Those are not valid values for a, b or c")
      discriminant = b ** 2 - 4 * a * c

      if discriminant < 0:
        print("There are no real roots to the equation")
      else:
        frstroot = (-b + math.sqrt(discriminant)) / (2*a)
        scndroot = (-b - math.sqrt(discriminant)) / (2*a)
        break
    except ValueError as e:
      print(e)
      while True:
        answer = input("Do you want to try again? y/n ")
        if answer.lower() == "y":
          break
        elif answer.lower() == "yes":
          break
        elif answer.lower() == "n":
          exit
        elif answer.lower() == "no":
          exit

        print(f"The roots are {frstroot} and {scndroot}")