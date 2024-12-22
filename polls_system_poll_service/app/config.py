import os

MYSQL_USER: str = "root"
MYSQL_PASSWORD: str = "root_password"
MYSQL_DATABASE: str = "poll_db"
MYSQL_HOST: str = "localhost"
MYSQL_PORT: str = "3307"
DATABASE_URL = os.getenv("DATABASE_URL", f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}")
