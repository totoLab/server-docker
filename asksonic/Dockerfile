FROM python:3.9-alpine

WORKDIR /app
RUN apk add --update gcc libc-dev libffi-dev openssl-dev git nodejs npm

RUN git clone https://github.com/srichter/asksonic.git /app

RUN pip3 install --upgrade pip

# Install Flask-Ask dependencies
RUN pip3 install aniso8601 "flask>=2.0.0,<2.2.0" "cryptography>=3.0.0" pyOpenSSL PyYAML six "Werkzeug<3.0.0" cachelib

# Install Flask-Ask
RUN pip3 install --no-dependencies git+https://github.com/srichter/flask-ask.git@flask2

# Install remaining asksonic dependencies
RUN pip3 install gunicorn py-sonic requests
RUN npm install -g foreman

# Environment
ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Command
CMD ["nf", "start"]
