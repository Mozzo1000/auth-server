FROM python:3.12.4-alpine
WORKDIR /app
RUN apk add build-base libpq libpq-dev

COPY README.md pyproject.toml entrypoint.sh ./
COPY migrations ./migrations
COPY api ./api

RUN pip install .
ENV FLASK_ENV=production
RUN chmod +x entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["/app/entrypoint.sh"]