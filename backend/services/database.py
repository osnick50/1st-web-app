import os
import logging
import mysql.connector
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

def connect_with_db():
    try:
        db_connection = mysql.connector.connect(
            user=os.getenv("DB_USER"), 
            password=os.getenv("DB_PASSWORD"), 
            host=os.getenv("DB_HOST"), 
            database=os.getenv("DB_NAME")
            )
        return db_connection
    except Exception as e:
        logging.error(f"Error connecting to database: {e}")
        raise e


def load_jobs_from_db():
    try:
        with connect_with_db() as db_conn:
            cursor = db_conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM jobs")
            result = cursor.fetchall()
            jobs = []
            for dict_row in result:
                jobs.append(dict(dict_row))
            logging.info("Jobs loaded from DB")
            return jobs
    except Exception as e:
        logging.error("Error occured while loading jobs from DB: ", e)


def load_job_id(id):
    try:
        with connect_with_db() as db_conn:
            cursor = db_conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM jobs WHERE id = {id}")
            result = cursor.fetchall()
            if len(result) == 0:
                return None
            else:
                return result[0]
    except Exception as e:
        logging.error("Error occurred while getting job by ID:", e)


def add_application_to_db(job_id, application):
    try:
        with connect_with_db() as db_conn:
            cursor = db_conn.cursor(dictionary=True)
            query = """INSERT INTO applications 
                (job_id, full_name, email, linkedin_url, education, work_experience)
                VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(
                query, (
                job_id, 
                application['full_name'], 
                application['email'], 
                application['linkedin_url'],
                application['education'],
                application['work_experience']
            ))
            db_conn.commit()
            return True
    except Exception as e:
        logging.error(f"Failed to insert or update application into the database: {e}")
        return False
