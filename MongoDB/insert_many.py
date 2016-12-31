import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
people = db.people


print "insert reporting for duty"

richard = {"name" : "Richard Kreuter" , "company" :"MongoDB" , "interests" : ['horses','skydiving','fencing']}

andrew = { "_id" : "erlichson" , "name" : "Andrew", "company" : "MongoDB" , "interests" : ['running','cycling','photography'] }

people_to_insert = [andrew,richard]

try:
    people.insert_many(people_to_insert,ordered=False)
    
except Exception as e:
    print "exception is " , type(e) , e

