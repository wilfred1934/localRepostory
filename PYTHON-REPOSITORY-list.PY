## LIST:
## Lists are used to store multiple items in a single variable.
## Lists are created using square brackets []:
### LIST EXAMPLES :

## example-01:
fruits = ["apple", "banana", "cherry"]
print(fruits)

## example-02:
names = ["raj", "rahul", "rohan", "rakesh", "rajesh"]
print(names)

## List Length
## To determine how many items a list has, use the len() function:

## Print the number of items in the list:
## example-01:
animals = ["dog", "cat", "lion", "tiger"]
print(len(animals))

## example-02:
numbers = [1,2,3,4,5]
print(len(numbers))


## The list() Constructor
## It is also possible to use the list() constructor when creating a new list.

## Using the list() constructor to make a List:
## example-01:
students = list(("rohan", "rakesh", "rajesh"))     # note the double round-brackets
print(students)

## example-02:
cars = list(("ms", "tata", "honda"))               # note the double round-brackets
print(cars)


## ACCESSING the ITEMS in the LIST by INDEXING
## List items are indexed and you can access them by referring to the index number:

##### Note: The first item has index 0. #####

## example-01:
##Print the second item of the list:
myList = ["apple", "banana", "cherry"]
print(myList[1])

## example-02:
##Print the fourth item of the list:
bikesList = ["yamaha", "honda", "bajaj", "ktm"]
print(bikesList[3])


## Negative Indexing in the LIST
## Negative indexing means start from the END.

###          -1 refers to the last item, -2 refers to the second last item etc.

## example-01:
##Print the last item of the list:
alphabets = ["a", "b", "c", "d"]
print(alphabets[-1])

## example-02:
##Print the first item of the list:
alphabets = ["a", "b", "c", "d"]
print(alphabets[-4])


##   Range of Indexes
## You can specify a range of indexes by specifying where to start and where to end the range.

##  When specifying a range, the return value will be a new list with the specified items.


## example-01:
## Return the third, fourth, and fifth item:
mylist = ["apple", "mango", "cherry", "orange", "papaya", "melon", "banana"]
print(mylist[2:5])

## example-02:
## Return the fifth, sixth, and seventh item:
mylist = ["apple", "mango", "cherry", "orange", "papaya", "melon", "banana"]
print(mylist[4:])


## Change Item Value
## To change the value of a specific item, refer to the index number:

## example-01:
## Change the second item in the list:
thislist = ["tiger", "lion", "zebra"]
thislist[1] = "cat"
print(thislist)

## example-02:
## Change the first item in the list:
system = ["monitor", "keyboard", "cpu"]
system[0] = "mouse"
print(system)



####    Append Items
##  To add an item to the end of the list, use the append() method:

## example-01:
## Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

## example-02:
system = ["monitor", "keyboard", "cpu"]
system.append("mouse")
print(system)


#####  Insert Items
##  To insert a list item at a specified index, use the insert() method.

## The insert() method inserts an item at the specified index:

## example-01:
## Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

## example-02:
## Insert an item as the 3 position:
fruitslist = ["apple", "banana", "cherry"]
fruitslist.insert(2, "mango")
print(fruitslist)


#### Extend List
## To append elements from another list to the current list, use the extend() method.

#### example-01:
##  Add the elements of num to alpha:
alpha = ["a", "b", "c"]
num = ["1", "2", "3"]
alpha.extend(num)
print(alpha)



#### Remove Specified Item
## The remove() method removes the specified item.

#### example-01:
##Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


####  Remove Specified Index
##   The pop() method removes the specified index.

## example-01:
## Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

## example-02:
## Remove the third item:
thislist = ["apple", "banana", "cherry", "mango"]
thislist.pop(2)
print(thislist)


####If you do not specify the index, the pop() method removes the last item.

## Example
## Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



#####      Loop Through a List
#####      You can loop through the list items by using a for loop:

### Example
##  Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


####       Loop Through the Index Numbers
####       You can also loop through the list items by referring to their index number.

####       Use the range() and len() functions to create a suitable iterable.

####    Example
####    Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])




# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method             Description
# append()    Adds an element at the end of the list
# clear()     Removes all the elements from the list
# copy()      Returns a copy of the list
# count()     Returns the number of elements with the specified value
# extend()    Add the elements of a list (or any iterable), to the end of the current list
# index()     Returns the index of the first element with the specified value
# insert()    Adds an element at the specified position
# pop()       Removes the element at the specified position
# remove()    Removes the item with the specified value
# reverse()   Reverses the order of the list
# sort()      Sorts the list
