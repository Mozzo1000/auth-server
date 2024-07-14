#!/bin/sh

echo "Running migration.."
python -m flask db upgrade
echo "Startin gunicorn.."
exec gunicorn -w 4 -b :5000 api.app:app
