FROM python:3.12.2-alpine

WORKDIR /D2D

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./

CMD [ "gunicorn", "--reload", "--workers=5", "--threads=1", "-b 0.0.0.0:5000", "src.app:server"]