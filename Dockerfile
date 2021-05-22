FROM pytorch/pytorch:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install mindsdb_native;

COPY main.py /main.py
ENTRYPOINT ["python", "/main.py"]
