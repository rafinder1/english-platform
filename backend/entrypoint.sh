#!/bin/sh

echo "Waiting for DB..."

sleep 5

echo "Running migrations..."
python manage.py migrate

echo "Seeding data..."
python manage.py seed_courses

echo "Starting server..."
exec "$@"