FROM python:2.7.15-stretch

ADD docker/requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /dga_predict

CMD ["python","run.py"]