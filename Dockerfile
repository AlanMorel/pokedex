FROM python:3.8

COPY . /app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["pokedex.py"]
