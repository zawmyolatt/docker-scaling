FROM python:3

RUN pip install flask

CMD flask run --host=0.0.0.0