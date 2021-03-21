import csv
from pymongo import MongoClient
import json
import datetime as dt
import csv

try:
  connection = MongoClient('test-server-fds4dvs45ssvkf.westus2.cloudapp.azure.com:39186', username="Training", password="Training@123")
  db = connection.TestDb
except Exception as e:
  print(f"{e}")

# find function ##
def xxx_FIND ():  # Selects documents in a collection or view and RETURNS a CURSOR to the selected documents.
  query1 = db.cars.find({})   # Returns a CURSOR OBJECT.
  print(query1)
                  # Here, we are converting a cursor object to a list of documents.
  query2 = list(db.cars.find({}))  # Will Return a LIST OF Documents.
  print(query2)

        # In This Method, using FOR LOOP we can get a LIST of Documents.
  query3 = db.cars.find({}) # Returns a CURSOR OBJECT.
  myList = []               # first create an new empty list.
  for i in query3:          # Use FOR LOOP to APPEND/ADD document to the above created Empty List.
    myList.append(i)
  print(myList)


### find_one function ##
def xxx_FIND_ONE ():   #  Returns One document that satisfies the criteria specified as the first argument to this method.
  query = db.cars.find_one({"_id": "1"})    # Will ONLY FIND the document with the specified "_id".
  print(query)


### insert_one function ##
def xxx_INSERT_ONE ():                      # Inserts a document into a collection.
  query = db.cars.insert_one({ "_id" : "10",
                               "company" : "vw",
                               "model" : "polo",
                               "year" : "2015"
                              })
  print(query)

### insert_many function ##
def xxx_INSERT_MANY ():                      #Inserts multiple documents into a collection.
  query = db.cars.insert_many([{ "_id" : "11",
                               "company" : "vw",
                               "model" : "vento",
                               "year" : "2014"
                              },{ "_id" : "12",
                               "company" : "tata",
                               "model" : "taigo",
                               "year" : "2011"
                              },{ "_id" : "13",
                               "company" : "maruti",
                               "model" : "ciaz",
                               "year" : "2005"
                              }])
  print(query)

### insert function ##
def xxx_INSERT ():  ##Inserts a document or (list of) documents into a collection.

                                            # Here, first we will Insert a single document.
  query1 = db.cars.insert({ "_id" : "14",
                           "company" : "maruti",
                           "model" : "alto",
                           "year" : "2002"
                          })
  print(query)

                                            # Here, first we will Insert a LIST of documents.
  query2 = db.cars.insert([{ "_id" : "15",
                           "company" : "maruti",
                           "model" : "alto",
                           "year" : "2003"
                          },{ "_id" : "16",
                           "company" : "maruti",
                           "model" : "alto",
                           "year" : "2004"
                          }])
  print(query2)


### update one function ##
def xxx_UPDATE_ONE ():      ## Updates a single document within the collection based on the filter.
 query = db.cars.update_one({"_id" : "16"},
                           { "$set" : {"company" : "car", "model" : "sunny"}})
 print(query)

### update many function ##
def xxx_UPDATE_MANY ():     ## Updates all documents that match the specified filter for a collection.
 query = db.cars.update_many({"_id" : {"$in" : ["1", "2", "3", "4"]}},
                             {"$set" : {"variant" : "petrol"}})
 print(query)

### delete one function ##
def xxx_DELETE_ONE ():        ## Removes/DELETES a single document from a collection.
  query = db.cars.delete_one({"_id" : "5"})
  print(query)

### delete many function ##
def xxx_DELETE_MANY ():        ## Removes all documents that match the filter from a collection.
  query = db.cars.delete_many({"_id" : {"$in" : ["15", "16"]}})
  print(query)


if __name__=='__main__':
 # xxx_FIND ()
 # xxx_FIND_ONE ()
 #xxx_INSERT_ONE ()
 #xxx_INSERT_MANY ()
 #xxx_INSERT ()
 #xxx_UPDATE_ONE ()
 #xxx_UPDATE_MANY ()
 #xxx_DELETE_ONE ()
 #xxx_DELETE_MANY ()

