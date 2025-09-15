from dotenv import load_dotenv
import os
from influxdb_client import InfluxDBClient, WriteOptions
from sensors.umidade import post_umidade
from sensors.temperatura import post_temperatura, delete_temperatura

load_dotenv()

url = os.getenv("INFLUX_URL")
token = os.getenv("INFLUX_TOKEN")
org = os.getenv("INFLUX_ORG")
bucket = os.getenv("INFLUX_BUCKET")

write_api = client.write_api(write_options=WriteOptions(batch_size=1))
delete_api = client.delete_api()


