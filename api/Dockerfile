FROM python:3

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt


COPY linkextractor.py /app/
COPY main.py /app/
RUN chmod a+x linkextractor.py
RUN chmod a+x main.py

ENTRYPOINT ["./main.py"]