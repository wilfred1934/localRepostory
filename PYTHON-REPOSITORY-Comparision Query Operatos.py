from pymongo import MongoClient
import json
import datetime

try:
  connection = MongoClient('test-server-fds4dvs45ssvkf.westus2.cloudapp.azure.com:39186', username="Training", password="Training@123")
  db = connection.TestDb
except Exception as e:
  print(f"{e}")


def findcourse (): #to find course whose duration is MORE than 3months
  durationOfCourse = db.CourseDuration.find({ "DurationInMonths" : { "$gt" :  int("3")  }})
  courseList =[]
  for i in durationOfCourse:
    courseList.append(i)
  return("DurationMoreThan3Months:", courseList)


def findcourse_01 (): #to find course whose course duration is EQUAL to or MORE than 3months
  durationOfCourse = db.CourseDuration.find({ "DurationInMonths" : { "$gte" :  int("3")  }})
  courseList =[]
  for i in durationOfCourse:
    courseList.append(i)
  return("DurationMoreThanOrEqualTo3Months:", courseList)

def findcourse_02 ():#to find course whose duration is LESS than 3months
  durationOfCourse = db.CourseDuration.find({ "DurationInMonths" : { "$lt" :  int("3")  }})
  courseList =[]
  for i in durationOfCourse:
    courseList.append(i)
  return("DurationLessThan3Months:", courseList)

def findcourse_03 ():#to find course whose duration is EQUAL to or LESS than 3months
  durationOfCourse = db.CourseDuration.find({ "DurationInMonths" : { "$lte" :  int("3")  }})
  courseList =[]
  for i in durationOfCourse:
    courseList.append(i)
  return("DurationLessThanOrEqualTo3Months:", courseList)

def findcourse_04 ():#to find course whose duration is NOT EQUAL to 3months
  durationOfCourse = db.CourseDuration.find({ "DurationInMonths" : { "$ne" :  int("3")  }})
  courseList =[]
  for i in durationOfCourse:
    courseList.append(i)
  return("DurationNotEqualTo3Months:", courseList)





if __name__=='__main__':
  # resultMoreThan3Months = findcourse ()
  # print(resultMoreThan3Months)

  # resultMoreThanOrEqualTo3Months = findcourse_01 ()
  # print(resultMoreThanOrEqual3Months)

  # resultLessThan3Months = findcourse_02 ()
  # print(resultLessThan3Months)

  # resultLessThanOrEqualTo3Months = findcourse_03 ()
  # print(resultLessThanOrEqualTo3Months)

  resultNotEqualTo3Months = findcourse_04 ()
  print(resultNotEqualTo3Months)
