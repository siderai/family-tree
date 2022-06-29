FROM python:3.7.13-slim-buster

ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1 
ENV PYTHONHASHSEED random
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PIP_DEFAULT_TIMEOUT 100

# System deps:
RUN pip install poetry

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry install --no-interaction --no-ansi

# Creating folders and files for a project:
COPY . /code
