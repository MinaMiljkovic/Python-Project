# Stage 1: Build
FROM python:3.12 AS builder

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --only api --no-root && poetry add uvicorn


# Stage 2: Run
FROM python:3.12-slim

WORKDIR /src

RUN groupadd -r appgroup && useradd -r -g appgroup appuser
USER appuser

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY entrypoint.sh ./entrypoint.sh
COPY src .

CMD ["sh", "./entrypoint.sh"]
