from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("INFLUX_URL")
token = os.getenv("INFLUX_TOKEN")
org = os.getenv("INFLUX_ORG")
bucket = os.getenv("INFLUX_BUCKET")


from influxdb_client import InfluxDBClient, Point, WriteOptions

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

point = (
    Point("umidade")
    .tag("sensor", "box")
    .field("valor", 50)
)

write_api.write(bucket=bucket, record=point)
print("Teste de inserção")

client.close()
