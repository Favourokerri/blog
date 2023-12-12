#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

# Create superuser
python manage.py createsuperuser --noinput --username=admin --email=admin@example.com

# Optionally, set the superuser password using the shell
python manage.py shell <<EOF
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
user.set_password('helvericawhite')
user.save()
EOF
