from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = 'flood'

HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', '9000')
