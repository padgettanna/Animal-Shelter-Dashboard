from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = '1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32343
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  
            return result.acknowledged # returns True is data inserted successfully, False otherwise      
        else:
            raise Exception("Nothing to save, because data parameter is empty") 
          
        
# Read method
    def read(self, searchData):
        if searchData is not None:
            result = self.database.animals.find(searchData)
            # returns result in a list
            return list(result) 
        else:
            raise Exception("Search parameter is missing")
            
# Update method
    def update(self, searchData, newData):
        if searchData is not None and newData is not None:
            if (self.database.animals.count_documents(searchData) == 0):
                result = 0
                
            elif (self.database.animals.count_documents(searchData) == 1):
                result = self.database.animals.update_one(searchData, {'$set': newData}).modified_count
                 
            else:
                result = self.database.animals.update_many(searchData, {'$set': newData}).modified_count
                
            return result # Returns the number of modified objects if any
        else:
            raise Exception("One of the parameters is missing")
            
# Delete method
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
            return result.deleted_count # Returns the number of deleted objects
        else:
            raise Exception("One of the parameters is missing")
