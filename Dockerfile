
FROM python:3.6.9
ENV PYTHONHONUNBUFFERED 1
MAINTAINER CLUSTER - 2021
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
ENV ORACLE_HOME=/usr/lib/oracle/11.2/client64
ENV PATH=$PATH:$ORACLE_HOME/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib
ADD oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm /tmp/
# Setup locale, Oracle instant client and Python
RUN apt-get update \
    && apt-get -y install alien libaio1 \
    && alien -i /tmp/oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm \
    && ln -snf /usr/lib/oracle/11.2/client64 /opt/oracle \
    && mkdir -p /opt/oracle/network \
    && ln -snf /etc/oracle /opt/oracle/network/admin \
    && apt-get clean && rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD root /
