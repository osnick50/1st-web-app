import os
import logging
import mysql.connector
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

db_connection = mysql.connector.connect(
    user=os.getenv("DB_USER"), 
    password=os.getenv("DB_PASSWORD"), 
    host=os.getenv("DB_HOST"), 
    database=os.getenv("DB_NAME")
    )

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
        logging.error("Error occured while loading jobs from DB: ", e)

def load_job_db(id):
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute((f"SELECT * FROM jobs WHERE id = {id}"))
        result = cursor.fetchall()
        if len(result) == 0:
            return None
        else:
            return result[0]
    except Exception as e:
        logging.error("Error occurred while getting job by ID:", e)


