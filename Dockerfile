FROM python:alpine
COPY . /app
WORKDIR /app

ENV MYSQL_DATABASE_HOST mysql-service.default.svc.cluster.local
# ENV MYSQL_DATABASE_USER clarus
ENV MYSQL_DATABASE_PASSWORD Clarusway_1
ENV MYSQL_DATABASE_DB phonebook

RUN pip install -r requirements.txt
EXPOSE 80
CMD python app.py