# Base this container image upon the official Python container image.
# Reference: https://hub.docker.com/_/python
FROM python:3.12

WORKDIR /app/src

# Install Python dependencies.
ADD requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

# Run `mkdocs serve` to serve the MkDocs site locally.
# Reference: https://www.mkdocs.org/user-guide/cli/#mkdocs-serve
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000", "--config-file=../mkdocs.yml"]
