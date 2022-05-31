FROM python-3.10

PULL ./VideoEncoder

WORKDIR /VideoEncoder

COPY requirements.txt /VideoEncoder

RUN pip3 install -r requirements.txt

COPY . /VideoEncoder

CMD python3 -m VideoEncoder
