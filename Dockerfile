ARG CI_DEPENDENCY_PROXY_GROUP_IMAGE_PREFIX

FROM ${CI_DEPENDENCY_PROXY_GROUP_IMAGE_PREFIX}/python:3.8.17-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app


RUN apt-get update && \
    apt-get install -y build-essential python3-dev gcc g++ libffi-dev git hunspell libhunspell-dev libicu-dev wget curl && \
    apt-get purge -y --auto-remove -o APT:AutoRemove:RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.6.1 python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml .
RUN poetry install --no-root

RUN python -m spacy download en

COPY . .

RUN wget -nv -O /app/app/profanity_filter/data/en.aff https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.aff && \
    wget -nv -O /app/app/profanity_filter/data/en.dic https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.dic && \
    wget -nv -O /app/app/profanity_filter/data/ru.aff https://cgit.freedesktop.org/libreoffice/dictionaries/plain/ru_RU/ru_RU.aff && \
    wget -nv -O /app/app/profanity_filter/data/ru.dic https://cgit.freedesktop.org/libreoffice/dictionaries/plain/ru_RU/ru_RU.dic
