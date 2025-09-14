from pymongo import MongoClient 
import os
from dotenv import load_dotenv
load_dotenv()
uri="mongodb+srv://yashviparikh02:pF9DX0rfmx9ZIyiF@cluster0.nld2mbs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client=MongoClient(uri)
#pF9DX0rfmx9ZIyiF
#yashviparikh02:pF9DX0rfmx9ZIyiF
db=client["career_counseling"]
tech_skills_collection= db["tech_skills"]