#!/bin/bash

rm db.sqlite3
rm -rf ./hireframeapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations hireframeapi
python3 manage.py migrate hireframeapi
python3 manage.py loaddata seekers jobs contacts interviews notes offers
