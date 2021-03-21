from flask import Flask, jsonify, make_response, request
from pymongo import MongoClient
import json
import datetime

try:
  connection = MongoClient('test-server-fds4dvs45ssvkf.westus2.cloudapp.azure.com:39186', username="Training", password="Training@123")
  db = connection.TestDb
except Exception as e:
  print(f"{e}")


app = Flask(__name__)



@app.route('/info', methods=["GET"])
def info_find_one ():
  data = request.args
  if data ["action"] == "find_one":
    studentDetails = db[data["collection"]].find_one({"RollNo" : data["rollNo"]})
    return make_response(jsonify({"dataOfStudents": studentDetails }))
  elif data ["action"] == "find":
    query = db[data["collection"]].find({})
    studentData=[]
    for value in query:
        studentData.append(value)
    return make_response(jsonify({"dataOfStudents": studentData }))

@app.route('/infoInsert', methods=["POST"])
def info_insertOneInsertMany ():
  data = request.json
  if data["action"] == "insert_one":
    db[data["collection"]].insert_one(data["data"])
    return make_response(jsonify({"Message": "insert successfull"}))
  elif data["action"] == "insert_many":
    db[data["collection"]].insert_many(data["data"])
    return make_response(jsonify({"Message": "insert successfull"}))

@app.route('/infoUpdate', methods=["PATCH"])
def info_updateOneUpdateMany ():
  data = request.json
  if data["action"] == "update_one":
    db[data["collection"]].update_one(data["find"], {"$set": data["data"]})
    return make_response(jsonify({"Message": "update successfull"}))
  elif data ["action"] == "update_many":
    db[data["collection"]].update_many(data["find"], {"$set": data["data"]})
    return make_response(jsonify({"Message": "update successfull"}))

@app.route('/infoDelete', methods=["DELETE"])
def info_deleteOneDeleteMany ():
  data = request.json
  if data ["action"] == "delete_one":
    db[data["collection"]].delete_one(data["data"])
    return make_response(jsonify({"Message": "delete successfull"}))
  elif data ["action"] == "delete_many":
    db[data["collection"]].delete_many(data["data"])
    return make_response(jsonify({"Message": "delete successfull"}))




if __name__=='__main__':

  app.run(debug=True)
