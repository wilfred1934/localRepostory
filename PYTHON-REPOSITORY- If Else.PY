#####                             Python Conditions and If statements

### Equals:                   a == b
### Not Equals:               a != b
### Less than:                a < b
### Less than or equal to:    a <= b
### Greater than:             a > b
### Greater than or equal to: a >= b

####                              ""  if Statement  ""
####              An "if statement" is written by using the if keyword.

##Example 01:
a = 33
b = 200
if b > a:
    print("true")

##Example 02:
a = 10
b = 20
if a < b:
    print("true")


####                             ""  Elif Statement  ""
##      The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

##Example 01:
a = 33
b = 33
if a > b:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


####                             ""  Else Statement  ""
##     The else keyword catches anything which isn't caught by the preceding conditions.

##Example 01:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


####                       You can also have an else without the elif:

##Example 01:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
