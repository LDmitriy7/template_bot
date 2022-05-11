FROM python:3.10.4-slim

WORKDIR /app

COPY . .

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

CMD ["python", "app.py"]