
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9

# Allow statements and log messages to immediately appear in the Knative logs
#ENV PYTHONUNBUFFERED True
# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /var/www/app
COPY ./requirements.txt /var/www/app/requirements.txt
RUN pip install -r /var/www/app/requirements.txt
COPY ./gunicorn.sh /app/gunicorn.sh
COPY . /var/www/app
ENV PORT 8080
EXPOSE $PORT
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT run:app  --workers 2 --threads 8 --timeout 3600
#ENTRYPOINT ["./gunicorn.sh"]