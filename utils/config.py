from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_USER = getenv("DB_USER", "root")
DB_PASSWORD=getenv("DB_PASSWORD")

