import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.school
grades = db.students


print "remove lowest homework score for every student"

def add_reviewer_update_many():
    try:
        print "find the target students"
        cursor = grades.find({ "scores.type":"homework" })
        #cursor = cursor.sort([("studet_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)])

        #prev_student_id = -1       
        for item in cursor:
            #if prev_student_id <>  item["student_id"] :
                record_id = item["_id"]
                record = item["scores"]
                #prev_student_id = item["student_id"]
                #prev_score = item["score"]
                #print prev_student_id
                #print prev_score
                print "collect homework scores"
                print record[2]["score"]
                print record[3]["score"]
                print record_id
                if record[2]["score"] > record[3]["score"]:
                    remscore = record[3]["score"]
                if record[3]["score"] > record[2]["score"]:
                    remscore = record[2]["score"]
                print "deleting score is "
                print remscore
                grades.update({"_id": record_id }  , {"$pull": { "scores" : { "type" : "homework" , "score":remscore }    }  })
                #grades.remove({"_id" : record_id})
            
            
        
        
    except Exception as e:
        print "exception is " , type(e) , e

add_reviewer_update_many()
    


