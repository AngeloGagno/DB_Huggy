FROM python:3.12

RUN pip install poetry

COPY  poetry.lock pyproject.toml /src/

WORKDIR /src

RUN poetry config virtualenvs.create false && poetry install --no-root 

COPY . /src

CMD [ "python","main.py" ]