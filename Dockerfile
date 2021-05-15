FROM python:3.7-alpine

COPY requirements.txt /tmp/requirements.txt

RUN \
    apk add --no-cache gcc musl-dev libc-dev linux-headers && \
    pip install -r /tmp/requirements.txt

COPY . /etc/bot/

WORKDIR /etc/bot/

CMD ["python3", "main.py"]

