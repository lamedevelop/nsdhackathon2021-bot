FROM python:3.7-alpine

ENV PACKAGES='\
    gcc\
    musl-dev\
    libc-dev\
    linux-headers\
    '

COPY requirements.txt /tmp/requirements.txt

RUN \
    apk add --no-cache $PACKAGES && \
    pip install -r /tmp/requirements.txt

COPY . /etc/bot/

WORKDIR /etc/bot/

CMD ["python", "main.py"]

