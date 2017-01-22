import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.students
grades = db.grades


print "remove lowest homework score for every student"

def add_reviewer_update_many():
    try:
        print "find the target students"
        cursor = grades.find({ "type":"homework" })
        cursor = cursor.sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)])

        prev_student_id = -1       
        for item in cursor:
            if prev_student_id <>  item["student_id"] :
                record_id = item["_id"]
                prev_student_id = item["student_id"]
                prev_score = item["score"]
                print prev_student_id
                print prev_score
                print record_id
                grades.remove({"_id" : record_id})
            
            
        
        
    except Exception as e:
        print "exception is " , type(e) , e

add_reviewer_update_many()
    


