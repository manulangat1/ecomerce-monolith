FROM python:3.10.0-slim-buster 

# WORKDIR 
ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME


LABEL maintainer='Emmanuel Langat'


LABEL description="This is a monolithic e-commerce application" 

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1  

ENV DEBUG=False

ENV ENVIRONMENT=staging

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get -y install netcat gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip 

COPY requirements.txt $APP_HOME/requirements.txt 

COPY . $APP_HOME/
COPY . $APP_HOME
RUN pip3 install -r $APP_HOME/requirements.txt 
RUN mkdir $APP_HOME/logs


COPY /entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# COPY /start /start
# RUN sed -i 's/\r$//g' /start
# RUN chmod +x /start


# RUN python3 manage.py collectstatic --noinput


ENTRYPOINT ["/entrypoint"]