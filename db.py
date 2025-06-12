from pymongo import MongoClient 
import os
from dotenv import load_dotenv
load_dotenv()
uri=os.getenv("mongo_uri")
client=MongoClient(uri)
#pF9DX0rfmx9ZIyiF

db=client["career_counseling"]
tech_skills_collection= db["tech_skills"]