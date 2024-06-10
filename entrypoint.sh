#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

sleep 5

# Run migrations
python manage.py migrate

# Start the server
exec "$@"