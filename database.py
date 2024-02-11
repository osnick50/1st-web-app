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
            os.getenv('INSTANCE_CONNECTION_NAME'),
            'pymysql',
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            db=os.getenv('DB_NAME'),
        )
        return conn
    except Exception as e:
        logging.error("Error initializing DB connection: ", e)


engine = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
