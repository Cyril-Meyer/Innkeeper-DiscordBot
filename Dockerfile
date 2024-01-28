FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir discord.py==1.7.3
