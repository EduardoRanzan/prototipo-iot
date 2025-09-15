from influxdb_client import Point

def post_temperatura(write_api, bucket, valor, sensor="temperatura"):
    temperatura = (
        Point("temperatura")
        .tag("sensor", sensor)
        .field("valor", float(valor))
    )
    write_api.write(bucket=bucket, record=temperatura)

def delete_temperatura(delete_api, bucket, org, start, stop, sensor="temperatura", valor=None):
    predicate = f'_measurement="temperatura" AND sensor="{sensor}"'
    if valor is not None:
        predicate += f' AND valor={float(valor)}'

    delete_api.delete(
        start=start,
        stop=stop,
        predicate=predicate,
        bucket=bucket,
        org=org
    )
