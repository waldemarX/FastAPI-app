from dotenv import load_dotenv
import os


load_dotenv()

# DATABASE
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

# TEST DATABASE
DB_USERNAME_TEST = os.environ.get("DB_USERNAME_TEST")
DB_PASSWORD_TEST = os.environ.get("DB_PASSWORD_TEST")
DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")


# REDIS
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

# JWT
SECRET_KEY = os.environ.get("SECRET")

# GOOGLE MAIL
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
