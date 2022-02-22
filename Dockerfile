FROM ghcr.io/deephaven/server
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
COPY app.d /app.d
