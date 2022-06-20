FROM docker.io/python:3.10-slim

COPY app.py /opt/app.py
COPY req.txt /opt/req.txt

WORKDIR /opt

RUN pip install -r req.txt

ENTRYPOINT [ "python","/opt/app.py" ]