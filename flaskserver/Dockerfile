FROM python:3
RUN pip install pymongo
RUN pip install Flask
ADD . /app
WORKDIR /app

CMD ["python","main.py"]
