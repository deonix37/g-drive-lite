FROM python:3.11.4

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
