# Read from Ubuntu Base Image
FROM python:2.7
RUN mkdir -p /service
# Copy over all the files of interest
ADD config.py /service/src/config.py
ADD manage.py /service/src/manage.py
ADD requirements.txt /service/requirements.txt
WORKDIR /service/
RUN pip install -r requirements.txt
CMD python -u app.py $APP_SETTINGS $DATABASE_URL
