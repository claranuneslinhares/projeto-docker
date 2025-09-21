FROM python:3.10

WORKDIR /app

COPY . .

 
RUN chmod +x wait-for-it.sh && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "./wait-for-it.sh", "db:3306", "--","python", "main.py"]
