# Stage 1: Build
FROM python:3.12 AS builder

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --only api --no-root
RUN poetry add uvicorn


# Stage 2: Run
FROM python:3.12-slim

WORKDIR /src

# Create non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
USER appuser

# Copy dependencies and source code
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY src .

CMD ["sh", "./entrypoint.sh"]
