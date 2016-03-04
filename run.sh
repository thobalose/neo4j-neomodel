#!/bin/sh
# Load seed data to DB and Run the App

echo "Hello, $USER! We hope you have a running instance of Neo4j on you machine."
python web_app/seed_data.py
python web_app/main.py
