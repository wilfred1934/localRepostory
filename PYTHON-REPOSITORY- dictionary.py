########                                           Dictionary
###                       Dictionaries are used to store data values in key:value pairs.

###              A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
###                      Dictionaries are written with curly brackets, and have keys and values:{}


## example-01:
## creating and print a dictionary:
mydict = {"name": "john", "age":"10", "city":"delhi"}
print(mydict)


## Dictionary Items
## Dictionary items are ordered, changeable, and does not allow duplicates.

## Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

## Example:
mydict = {"name": "john", "age":"10", "city":"delhi"}
print(mydict["name"])


## Dictionary Items - Data Types
## The values in dictionary items can be of any data type:

## Example
## String, int, boolean, and list data types:
student = {"name": "rahul", "indian": True, "age": 20, "favColours": ["red", "blue", "green"]}
print(student)


##                           Accessing Items of a Dictionary:
## You can access the items of a dictionary by referring to its key name, inside square brackets:

## Example:
## Get the value of the "age" key:
human = {"name": "john", "age":"10", "city":"delhi"}
print(human["age"])


##### get() method will give you the same result:
human = {"name": "john", "age":"10", "city":"delhi"}
print(human.get("name"))


###                          Get Keys
### The keys() method will return a list of all the keys in the dictionary.
human = {"name": "john", "age":"10", "city":"delhi"}
print(human.keys())

###                          Get Values
### The values() method will return a list of all the values in the dictionary.
human = {"name": "john", "age":"10", "city":"delhi"}
print(human.values())

###                          Get Items
### The items() method will return each item in a dictionary, as tuples in a list.
human = {"name": "john", "age":"10", "city":"delhi"}
print(human.items())                                ### will get a list of the key:value pairs


###                       Update Dictionary
### The update() method will update the dictionary with the items from the given argument.

### The argument must be a dictionary, or an iterable object with key:value pairs.

### Example
### Update the "city" of the human by using the update() method:
human = {"name": "john", "age":"10", "city":"delhi"}
human.update({"city":"mumbai"})
print(human)

## If the item does not exist, the item will be added in the update() method.
## example:
human = {"name": "john", "age":"10", "city":"delhi"}
human.update({"school":"new high school"})
print(human)


##                          Removing Items
##  There are several methods to remove items from a dictionary: pop(), popitem(), clear(), del keyword,

## Example                            pop()
## The pop() method removes the item with the specified key name:
human = {"name": "john", "age":"10", "city":"delhi"}
human.pop("name")
print(human)

## Example                            popitem()
## The popitem() method removes the last inserted item:
human = {"name": "john", "age":"10", "city":"delhi"}
human.popitem()
print(human)

## Example                            clear()
## The clear() method empties the dictionary:
human = {"name": "john", "age":"10", "city":"delhi"}
human.clear()
print(human)

## Example                        ##    del keyword      ###
## The del keyword removes the item with the specified key name:
human = {"name": "john", "age":"10", "city":"delhi"}
del human["name"]
print(human)

## Example
## The del keyword can also delete the dictionary completely:
# human = {"name": "john", "age":"10", "city":"delhi"}
# del human
# print(human)     #this will cause an error because "human" no longer exists.


 #######                                              Loop Through a Dictionary
####        You can loop through a dictionary by using a for loop.

####        When looping through a dictionary, the return value are the keys of the dictionary.
####        but there are methods to return the values as well.


##   Example
###  Print all key names in the dictionary, one by one:
human = {"name": "john", "age":"10", "city":"delhi"}
for i in human:
    print(i)


##  Example
##  Print all values in the dictionary, one by one:
human = {"name": "john", "age":"10", "city":"delhi"}
for i in human:
    print(human[i])

## Example                           ### values() method to return values
## You can also use the values() method to return values of a dictionary:
human = {"name": "john", "age":"10", "city":"delhi"}
for i in human.values():
  print(i)

## Example                           ### keys() method to return the keys
## You can use the keys() method to return the keys of a dictionary:
human = {"name": "john", "age":"10", "city":"delhi"}
for i in human.keys():
  print(i)

## Example                           ### items() method
## Loop through both keys and values, by using the items() method:
human = {"name": "john", "age":"10", "city":"delhi"}
for keys, values in human.items():
  print(keys, values)


#####                                    Copy a Dictionary
## There are ways to make a copy, one way is to use the built-in Dictionary method copy().

## Example
## Make a copy of a dictionary with the copy() method:
human = {"name": "john", "age":"10", "city":"delhi"}
newdict = human.copy()
print(newdict)

##         ANOTHER built-in function to copy is dict().
## Example
## Make a copy of a dictionary with the dict() function:
human = {"name": "john", "age":"10", "city":"delhi"}
mydict = dict(human)
print(mydict)


####                                                  Dictionary Methods
####                        Python has a set of built-in methods that you can use on dictionaries.

# Method                  Description
# clear()            Removes all the elements from the dictionary
# copy()             Returns a copy of the dictionary
# fromkeys()         Returns a dictionary with the specified keys and value
# get()              Returns the value of the specified key
# items()            Returns a list containing a tuple for each key value pair
# keys()             Returns a list containing the dictionary's keys
# pop()              Removes the element with the specified key
# popitem()          Removes the last inserted key-value pair
# setdefault()       Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()           Updates the dictionary with the specified key-value pairs
# values()           Returns a list of all the values in the dictionary






































