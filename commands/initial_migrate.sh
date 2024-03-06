#!/bin/bash

# Define a role padrão como "ficker"
export PGUSER=ficker
export PGPASSWORD=ficker

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
