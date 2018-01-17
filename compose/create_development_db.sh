#!/bin/sh

export PGPASSWORD=postgres

psql -h postgres --user postgres -c "create database \"mhp;\""

exit 0  # ignore errors
