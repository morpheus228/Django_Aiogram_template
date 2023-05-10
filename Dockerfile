FROM python:3.8-slim-buster
WORKDIR /code

# Upgrade installed packages
RUN apt-get -y update
RUN apt-get -y upgrade

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Install supervisor
RUN apt-get install  -y supervisor
COPY supervisord.conf /etc/supervisor/supervisord.conf

COPY . .

CMD ["/usr/bin/supervisord"]
