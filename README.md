# stock_market_forecast
NYSE stock exchange prediction

# Build the image:
docker-compose build

# Launch microservice wrapper with Minio model storage:
docker-compose up -d

Access Minio:
http://127.0.0.1:9000/

Access Swagger UI:
http://localhost:8082/ui

Access Jupyter Notebook:
http://127.0.0.1:8888/tree (or copy and paste link with generated token for python_notebook container)

