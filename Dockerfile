FROM python-3.10

WORKDIR /app/VideoEncoder

COPY requirements.txt /app/VideoEncoder

RUN pip3 install -r requirements.txt

COPY . /app/VideoEncoder

CMD python3 -m VideoEncoder
