FROM ubuntu
WORKDIR /code
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update && apt-get install -y --no-install-recommends \
  && apt-get install -y python3 python3-pip
  && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]