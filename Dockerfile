FROM python:2.7.13-alpine
MAINTAINER "kaushik.shingne@sjsu.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
CMD ["app.py"]
