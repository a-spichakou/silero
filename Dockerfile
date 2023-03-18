FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update --fix-missing && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y apt-utils python3-pip git nano wget

RUN apt-get install -y locales && locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN mkdir silero
RUN cd ./silero

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install numpy

RUN wget -O v3_1_ru.pt https://models.silero.ai/models/tts/ru/v3_1_ru.pt
RUN mv v3_1_ru.pt model.pt

COPY app.py .

CMD gunicorn --access-logfile - -w 4 --bind 0.0.0.0:8899 app:app --timeout 15000 