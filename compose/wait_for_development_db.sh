#!/bin/sh

export PGPASSWORD=postgres

while ! psql -h postgres --user postgres -c "select 1"
do
    sleep 1
done
