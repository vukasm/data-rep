import mysql.connector
import dbconfig as cfg

class ChocolatesDAO:
    db=""
    #connect to the database
    def __init__(self):
        self.db=mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )
        print("connection made") #sanity check

    #Create.
    def create(self,chocolate):
        #taking in json object chocolate
        
        cursor=self.db.cursor()
        sql="insert into chocolates (id, brand, kind, price) values (%s,%s,%s,%s)"
        values=[
            chocolate['id'],
            chocolate['brand'],
            chocolate['kind'],
            chocolate['price']        
            ]
        cursor.execute(sql,values)
        self.db.commit()
        return cursor.lastrowid

    #Get all.
    def getAll(self):
        cursor=self.db.cursor()
        sql='select * from chocolates'
        cursor.execute(sql)
        results=cursor.fetchall() #gets all as tuples
        #convert into json array
        returnArray=[]
        print(results) #sanity check, returned tuples
        
        for result in results:
            print(result)
            returnArray.append(self.convert_to_dict(result))
        return returnArray

    #Find by ID.
    def findbyId(self,id):
        cursor=self.db.cursor()
        sql='select * from chocolates where id=%s'
        values=[id]
        cursor.execute(sql,values)
        result=cursor.fetchone() 
        #convert into json array
        return self.convert_to_dict(result)


    #Update.
    def update(self,chocolate):
        cursor=self.db.cursor()
        sql="update chocolates set brand=%s, kind=%s, price=%s where id=%s"
        values=[ #the order needs to match above order
            chocolate['brand'],
            chocolate['kind'],
            chocolate['price'],
            chocolate['id']      
            ]
        cursor.execute(sql,values)
        self.db.commit()
        return chocolate

    #Delete.
    def delete(self,id):
        cursor=self.db.cursor()
        sql='delete from chocolates where id=%s'
        values=[id]
        cursor.execute(sql,values)
        
        return {}


    #Method to convert tuple to dict.
    def convert_to_dict(self,result):
        colnames=['id','brand','kind','price']
        chocolate={}

        if result:
            for i, colName in enumerate(colnames):
                value=result[i] #extract the value of each.
                chocolate[colName]=value 
        return chocolate

chocolatesDAO=ChocolatesDAO() #instance
