####                                           FOR LOOP
#### A for loop is used for iterating over a sequence which can  either be a list, a tuple, a dictionary, a set, or a string).


## Example
## Print each name in  students list:

students = ["rahul", "raj", "john", "kiran"]
for x in students:
  print(x)


####                                        Looping Through a String
##   Even strings are iterable objects, they contain a sequence of characters:

## Example
## Loop through the letters in the word "house":
word = "house"
for x in "house":
  print(x)

####                                        The range() Function
##   The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

## Example
## Using the range() function:
for x in range(6):       ## Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
  print(x)


## The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:
## Example
## Using the start parameter:
for x in range(2, 6):    ### range(2, 6), which means values from 2 to 6 (but not including 6):
  print(x)


##     The range() function defaults to increment the sequence by 1,
##     however it is possible to specify the increment value by adding a third parameter:
## Example
## Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):   ## increment value by adding a third parameter i.e 3
  print(x)


