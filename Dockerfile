FROM python:3.10

WORKDIR /app

COPY . .

 
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "main.py"]
