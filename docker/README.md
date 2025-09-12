# Docker
### Rode toda a stack desse projeto apenas com apenas 2 passos!!
1. Duplique o arquivo .env.example e renomeie para .env
```bash
cd docker && \
cp .env.example .env
```
> Atribuia valores às variáveis de ambiente
>> INFLUXDB_DB= <br>
INFLUXDB_ADMIN_USER= <br>
INFLUXDB_ADMIN_PASSWORD= <br>
GF_SECURITY_ADMIN_USER= <br>
GF_SECURITY_ADMIN_PASSWORD= <br>

2. Finalize rodando os seguintes comandos para subir a stack completa do projeto!
```bash
cd docker && \
docker-compose up -d
```