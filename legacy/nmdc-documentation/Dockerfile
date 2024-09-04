# Base this container image upon the official Python container image.
# Reference: https://hub.docker.com/_/python
FROM python:3.12

WORKDIR /app

# Install a package that can be used to effectively run Spinx in "watch" mode,
# wherein the web-based documentation will automatically be rebuilt whenever
# a source file changes.
# Reference: https://github.com/sphinx-doc/sphinx-autobuild
RUN pip3 install sphinx-autobuild

ADD requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 8000

# Run `sphinx-autobuild` in a way that, whenever something changes
# in the `src` directory, it rebuilds the web-based documentation
# and stores the result in `_build/html`.
CMD ["sphinx-autobuild", "--host", "0.0.0.0", "src", "_build/html"]
