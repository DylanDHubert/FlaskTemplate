FROM python:alpine

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

COPY requirements.txt requirments.txt
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "process.py"]