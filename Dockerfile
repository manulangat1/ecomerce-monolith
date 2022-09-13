# FROM python:3.10.0-slim-buster 

# # WORKDIR 
# ENV APP_HOME=/app
# RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/staticfiles
# WORKDIR $APP_HOME


# # RUN addgroup -S app && adduser  app -G app
# # RUN addgroup app && adduser -DH -G app app
# LABEL maintainer='Emmanuel Langat'
##ghj


# LABEL description="This is a monolithic e-commerce application" 

# ENV PYTHONDONTWRITEBYTECODE=1

# ENV PYTHONUNBUFFERED=1  

# ENV DEBUG=False

# ENV ENVIRONMENT=staging

# RUN apt-get update \
#     && apt-get install -y build-essential \
#     && apt-get install -y libpq-dev \
#     && apt-get install -y gettext \
#     && apt-get -y install netcat gcc postgresql \
#     && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#     && rm -rf /var/lib/apt/lists/*

# RUN pip3 install --upgrade pip 

# COPY requirements.txt $APP_HOME/requirements.txt 

# COPY . $APP_HOME/
# COPY . $APP_HOME
# RUN pip3 install -r $APP_HOME/requirements.txt 
# RUN mkdir $APP_HOME/logs


# COPY /entrypoint /entrypoint
# RUN sed -i 's/\r$//g' /entrypoint
# RUN chmod +x /entrypoint

# # COPY /start /start
# # RUN sed -i 's/\r$//g' /start
# RUN chmod +x $APP_HOME/


# RUN python3 manage.py collectstatic --noinput

# # RUN python3 manage.py migrate
# # chown all the files to the app user
# # RUN chown -R app:app $APP_HOME

# # # change to the app user
# # USER app
# ENTRYPOINT ["/entrypoint"]







###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.6-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

#install other dependencies
RUN apk update && apk add --no-cache \
    libffi-dev \
    # libssl-dev \
    zlib-dev \
    jpeg-dev \
    make automake gcc g++ subversion python3-dev \ 
    gcc musl-dev python3-dev libffi-dev openssl-dev cargo \
    && export CRYPTOGRAPHY_DONT_BUILD_RUST=1

# lint
RUN pip install --upgrade pip
# RUN pip install flake8==3.9.2
COPY . .
# RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
RUN pip wheel -r ./requirements.txt --wheel-dir /usr/src/app/wheels

#########
# FINAL #
#########

# pull official base image
FROM python:3.9.6-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
RUN mkdir $APP_HOME/static
# RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/* &&   rm -rf /wheels

# copy entrypoint.prod.sh
COPY ./entrypoint .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint
RUN chmod +x  $APP_HOME/entrypoint

# copy project
COPY . $APP_HOME

#Remove all dependencies
RUN rm -rf /usr/src/app/wheels


# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user

USER app
RUN python manage.py collectstatic --noinput --settings=monolithEcommerce.settings.base

RUN chmod +x  $APP_HOME/entrypoint

# run entrypoint.prod.sh
# ENTRYPOINT ["entrypoint"]