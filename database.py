import os
import sqlalchemy
import pymysql
from google.cloud.sql.connector import Connector, IPTypes


ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
connector = Connector(ip_type)

def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        os.getenv('INSTANCE_CONNECTION_NAME'),
        'pymysql',
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        db=os.getenv('DB_NAME'),
    )
    return conn

engine = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)



