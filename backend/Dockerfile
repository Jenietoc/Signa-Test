FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev postgresql-dev libffi-dev openssl-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
