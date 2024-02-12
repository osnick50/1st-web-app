import os
import logging
import sqlalchemy
import pymysql
from google.cloud.sql.connector import Connector, IPTypes

logging.basicConfig(level=logging.INFO)

ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
connector = Connector(ip_type)

def getconn() -> pymysql.connections.Connection:
    try:
        logging.info("Initialize connection with DB")
        conn: pymysql.connections.Connection = connector.connect(
            os.environ['INSTANCE_CONNECTION_NAME'],
            'pymysql',
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS'],
            db=os.environ['DB_NAME'],
        )
        logging.info("Connection with SQL initialized")
        return conn
    except Exception as e:
        logging.error("Error initializing DB connection: ", e)


engine = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

def load_jobs_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(sqlalchemy.text("SELECT * FROM jobs"))
            jobs_list = []
            for dict_row in result.mappings():
                jobs_list.append(dict(dict_row))
            logging.info("Jobs loaded from DB")
            return jobs_list
    except Exception as e:
        logging.info("Error occured while loading jobs from DB: ", e)