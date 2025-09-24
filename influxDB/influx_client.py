from dotenv import load_dotenv
import os
from influxdb_client import InfluxDBClient

load_dotenv()

url = os.getenv("INFLUX_URL")
token = os.getenv("INFLUX_TOKEN")
org = os.getenv("INFLUX_ORG")
bucket = os.getenv("INFLUX_BUCKET")

client = InfluxDBClient(url=url, token=token, org=org)

def client_write_api():
    return client.write_api()

def client_query_api():
    return client.query_api()

def client_delete_api():
    return client.delete_api()

def get_bucket():
    return bucket

def get_org():
    return org