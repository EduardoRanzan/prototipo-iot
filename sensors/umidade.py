from influxdb_client import Point
from influxdb_client import WriteOptions

def post_umidade(write_api, bucket, valor, sensor="umidade"):
    """Insere valor de umidade no InfluxDB"""
    umidade = (
        Point("umidade")
        .tag("sensor", sensor)
        .field("valor", float(valor))
    )
    write_api.write(bucket=bucket, record=umidade)
    print(f"✅ Umidade {valor} inserida")
