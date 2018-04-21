#!/bin/sh -eu
sleep 30
python web_app/seed_data.py
python web_app/main.py
