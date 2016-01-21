#!/bin/sh
#Set the location of neo4j via an environment variable.

echo "Hello, $USER! We hope you have a running instance of Neo4j on you machine."
echo -n 'Please provide us with you Neo4j USERNAME: '
read username
echo -n 'Please provide us with you Neo4j PASSWORD: '
read password

export NEO4J_REST_URL=http://$username:$password@localhost:7474/db/data/

python main.py
