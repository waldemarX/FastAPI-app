FROM python:3.10

RUN mkdir /code

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code/

# RUN chmod a+x docker/*.sh

# RUN alembic upgrade head

WORKDIR /code/app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]