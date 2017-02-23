import sys
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
images = db.images  


print "remove orphan images that are not found in any album"

def remove_orphan_images():
    try:
        print "find the target images"
        cursor = images.find()
        
               
        for item in cursor:
            #print item
            #print item["_id"]
            result = db.albums.find({"images":item["_id"]}).count()  
            #print result
            if result is 0 :
                print  item["_id"]
                images.remove({"_id" : item["_id"]})
            
            
        
        
    except Exception as e:
        print "exception is " , type(e) , e

remove_orphan_images()
