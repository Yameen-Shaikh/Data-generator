FROM python:3.8-slim-buster
 
WORKDIR /app
 
COPY . /app
 
RUN pip install -r requirements.txt
 
COPY  dataGenerator.py /

ENV FLASK_APP=dataGenerator.py
ENV FLASK_ENV=development
 
EXPOSE 8000
 
CMD ["uvicorn", "--reload", "--bind", "0.0.0.0:8000", "dataGenerator:app"]
 
 