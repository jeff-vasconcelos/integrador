
FROM python:3.8
ENV PYTHONHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
EXPOSE 7000:7000
ENV ORACLE_HOME=/usr/lib/oracle/11.2/client64
ENV PATH=$PATH:$ORACLE_HOME/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib
ADD oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm /tmp/
RUN apt-get update \
    && apt -y install curl \
    && apt -y install redis-server \
    && apt-get -y install alien libaio1 \
    && alien -i /tmp/oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm \
    && ln -snf /usr/lib/oracle/11.2/client64 /opt/oracle \
    && mkdir -p /opt/oracle/network \
    && ln -snf /etc/oracle /opt/oracle/network/admin \
    && apt-get clean && rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD root /
#ENV DEBUG=1
#ENV CELERY_BROKER=redis://redis:6379
#ENV CELERY_BACKEND=redis://redis:6379
#CMD sh -c "redis-server & python manage.py runserver 0.0.0.0:7000 & celery -A setup worker -l INFO --concurrency=5 -n worker1@%h & celery -A setup worker -l INFO --concurrency=5 -n worker2@%h & celery -A setup worker -l INFO --concurrency=5 -n worker3@%h & celery -A setup worker -l INFO --concurrency=5 -n worker4@%h & celery -A setup beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler"