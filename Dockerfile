
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Allow statements and log messages to immediately appear in the Knative logs
#ENV PYTHONUNBUFFERED True
# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /var/www/app
COPY ./requirements.txt /var/www/app/requirements.txt
RUN pip install -r /var/www/app/requirements.txt
COPY . /var/www/app
ENV PORT 8080
EXPOSE $PORT
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT run:app  --workers 2 --threads 8 --timeout 3600
#ENTRYPOINT ["./gunicorn.sh"]