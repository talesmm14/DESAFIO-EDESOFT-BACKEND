FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN mkdir /app/static
RUN mkdir /app/assets

RUN apt-get update

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# install dependencies
COPY pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root

# copy and run program
COPY . /app/
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
CMD [ "poetry", "run", "python", "-m", "main" ]
