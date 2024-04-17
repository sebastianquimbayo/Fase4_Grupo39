import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
HOST = os.getenv("HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
SERVICE_URI = os.getenv("SERVICE_URI")
PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("DB_USER")
PORT = os.getenv("PORT")