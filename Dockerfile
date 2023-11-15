FROM python:3

RUN pip install beautifulsoup4
RUN pip install requests

WORKDIR /app
COPY linkextractor.py /app/
RUN chmod a+x linkextractor.py

ENTRYPOINT ["./linkextractor.py"]