import os
import logging
import mysql.connector
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

db_connection = mysql.connector.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), database=os.getenv("DB_NAME"))

def load_jobs_db():
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(("SELECT * FROM jobs"))
        result = cursor.fetchall()
        jobs = []
        for dict_row in result:
            jobs.append(dict(dict_row))
        logging.info("Jobs loaded from DB")
        return jobs
    except Exception as e:
        logging.info("Error occured while loading jobs from DB: ", e)
