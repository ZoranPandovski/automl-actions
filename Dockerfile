FROM pytorch/pytorch:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install mindsdb_native==2.37.0;

COPY mdb.py /mdb.py
ENTRYPOINT ["python", "/mdb.py", "--dataset", "$INPUT_DATASET", "--target", "$INPUT_TARGET"]
