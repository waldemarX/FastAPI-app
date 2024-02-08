FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code/

RUN chmod a+x docker/*.sh

WORKDIR /code/

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]