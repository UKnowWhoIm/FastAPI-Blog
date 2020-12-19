from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Parent of 'app' directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Load Environment Variables
load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.environ["SECRET_KEY"]

POSTGRES_DB = os.environ["postgres_db"]
