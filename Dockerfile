FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV OTEL_SIMULATOR_DEBUG=
ENV OTEL_SIMULATOR_APP_URL=http://0.0.0.0:8080

CMD ["python", "main.py"]
