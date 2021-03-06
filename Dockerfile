FROM python:3.8.8-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/
ENTRYPOINT ["sh", "/src/entrypoint.sh"]
