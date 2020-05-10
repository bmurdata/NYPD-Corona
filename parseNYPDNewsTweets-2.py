import json
import pyodbc
import connection

from connection import cursor

with open("mytweets428.json",encoding="utf8") as of:
    prevline=json.loads(of.readline())
    prelinekeys=prevline.keys()

    #Create Table if needed
    sqlmakeTable="CREATE TABLE mytweets428 ({params})"
    params=""
    finalparms=dict()
    
    okay=0
    errjson=0
    totals=0

    for key in prevline:

        if isinstance(prevline[key],str):
            params=params+", "+key+ " NVARCHAR(2000)"
            finalparms[key]=str()
        elif isinstance(prevline[key],bool):
            params=params+", "+key+" BIT"
            finalparms[key]=bool()
        elif isinstance(prevline[key],list):
            print(key + " needs a foreign key table")
            params=params+""
        elif isinstance(prevline[key],(float,int)):
            
            params=params+", "+key+" BIGINT"
            finalparms[key]=int()
        else:
            print(key + " is something I don't know yet")

    params=params[2:]
    sqlmakeTable.format(params=params)
    print(sqlmakeTable.format(params=params))

    #Attempt to add the table
    try:
        cursor.execute(sqlmakeTable.format(params=params))
        cursor.commit()
    except Exception as ex:
        print("Table either already in or unable to add. See error message")
        print(ex)

    
    #Put the JSON Objects in the database
    sqlInsertToTable="INSERT INTO mytweets428 VALUES ({vals})"
    sqlCheckIfExists="SELECT COUNT(1) FROM table_name WHERE id = {val};"
    for line in of:
        myvals=""
        jsonobj=json.loads(line)
       
        for param in finalparms:

            insertedFieldValue=jsonobj[param]
            jsonobjType=finalparms[param]

            if isinstance(jsonobjType,str):
                myvals=myvals+"'"+str(insertedFieldValue).replace("'","''")+"'"+", "

            elif isinstance(jsonobjType,bool):
                if insertedFieldValue is True:
                    insertedFieldValue=1
                else:
                    insertedFieldValue=0
                myvals=myvals+str(insertedFieldValue)+", "

            else:
                myvals=myvals+str(insertedFieldValue)+", "

        #print(myvals)
        myvals=myvals[:-2]

        #print(sqlInsertToTable.format(vals=myvals))
        try:
            cursor.execute(sqlInsertToTable.format(vals=myvals))
            cursor.commit()
            okay=okay+1
        except Exception as e:
            errjson=errjson+1
            print(e)
        
    print("Total errors: "+str(errjson))
    print("Total okay: "+str(okay))
    print("Total JSON Objects in the file: "+str(totals))
