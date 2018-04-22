#!/bin/sh -eu
sleep 10
python web_app/seed_data.py
python web_app/main.py
