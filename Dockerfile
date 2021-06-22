# Imagem base da qual vai ser criada a imagem modificada:
FROM python:3.6.9
ENV PYTHONUNBUFFERED 1
# Responsável do projeto:
MAINTAINER Leandro Auzier da Silva
# copia os arquivos para uma pasta, nesse caso no HUB:
COPY . /app
# Assim que o container carregar,direciona para aonde a instalação dos requerimentos vai ser feita
WORKDIR /app
#Executar todas as dependencias: (apt-cache pois não precisa de barra de progresso)
RUN apt-get update
RUN apt install -y redis-server
#apt-get -y install python3-pip &&
RUN pip3 install -r requirements.txt
# Assim que o cointainer startar, executar:
#ENTRYPOINT /bin/sh

# Identificar que porta o container vai usar:
