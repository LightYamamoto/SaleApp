

FROM python:3.10-slim
WORKDIR /python-app

RUN apt-get update && apt-get install -y gcc
RUN python -m pip install --upgrade pip

COPY . .
RUN pip install -r requirements.txt
CMD ["python",  "postgres_connect.py"]
