import json
import pyodbc
import connection
from connection import cursor
import datetime 
from datetime import datetime
import re

parseme=False
if parseme:
    with open("mytweets428_copy.json",encoding="utf8") as of:
        #Go through, pull all the betweens
        #Use tweet, between date
        jsonToWrite=list()
        for line in of:
            myobj=json.loads(line)
            myobj["timestamp"]=myobj["date"]+" "+myobj["time"]
            jsonToWrite.append(myobj)
        print(len(jsonToWrite))
        
        with open("modifiedtweets.json","w") as newjson:
            for jsonobj in jsonToWrite:
                json.dump(jsonobj,newjson)
                newjson.write("\n")
else:
    print("File read")
    with open("modifiedtweets.json","r") as of:
        numWithBetween=0
        for line in of:
            curjsonobj=json.loads(line)
            timsestamp_string=curjsonobj["timestamp"]
            datetimeobj=datetime.strptime(timsestamp_string, '%Y-%m-%d %H:%M:%S')
            #print(datetimeobj)
            if re.search('.*ween',curjsonobj["tweet"]):
                numWithBetween+=1
        print(str(numWithBetween))


            #Make a table of related tweets, grouped around date, time.

            