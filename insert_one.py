import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
people = db.people


print "insert reporting for duty"

richard = {"name" : "Richard Kreuter" , "company" :"MongoDB" , "interests" : ['horses','skydiving','fencing']}

andrew = { "_id" : "erlichson" , "name" : "Andrew", "company" : "MongoDB" , "interests" : ['running','cycling','photography'] }

try:
    people.insert_one(richard)
    people.insert_one(andrew)

except Exception as e:
    print "exception is " , type(e) , e

