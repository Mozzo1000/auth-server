FROM python:3.12.4
WORKDIR /app

COPY .env README.md pyproject.toml entrypoint.sh ./
COPY migrations ./migrations
COPY api ./api

RUN apt update && apt install -y netcat-openbsd

RUN pip install .
ENV FLASK_ENV production

EXPOSE 5000
CMD ["gunicorn", "-b", ":5000", "api.app:app"]

ENTRYPOINT ["/app/entrypoint.sh"]