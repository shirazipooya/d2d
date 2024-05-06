FROM python:3.10.14
WORKDIR /D2D

COPY ./requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./ ./

CMD [ "gunicorn", "--reload", "--workers=5", "--threads=1", "-b 0.0.0.0:5000", "src.app:server"]