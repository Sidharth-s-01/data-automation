from pymongo import MongoClient
import json
import logging

# Configure logging to log to a file, include the time, log level, and message
logging.basicConfig(
    filename='app.log',  # The log file where errors will be written
    filemode='a',        # 'a' for append mode, 'w' to overwrite the file each time
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    level=logging.ERROR  # Only log errors or above (i.e., critical)
)

try:
    # mongo = MongoClient("mongodb+srv://user:user@dataautomationcluster.mongodb.net/test?retryWrites=true&w=majority&tlsAllowInvalidCertificates=True")
    mongo=MongoClient("mongodb+srv://user:user@dataautomationcluster.8hxfh.mongodb.net",connectTimeoutMS=30000,
    socketTimeoutMS=30000)
    print("Mongo Connection sucessfull")
except:
    print("Mongo Connection Failed..")

#
dataBaseName="db"
collectionName="profile"

database=mongo[dataBaseName]
collection=database[collectionName]

print("Started Uplaoding Data...")
try:
    with open("Transformed.json",'r') as f:
        data=json.load(f)

        for person in data:
            print(type(person))
            collection.insert_one(person)
    print("Uploading Data finished.....Data uploaded Successfully...")
except Exception as E:
    print("Some error occured...Please check Log file for Error Details..")
    logging.error(f"Error: {E}",exc_info=True)

#





# print(db.list_collection_names())