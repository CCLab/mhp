#!/bin/sh

PROJECT_ROOT=`dirname $0`/../

if [ -e $PROJECT_ROOT/node_modules ]
then
    echo "node_modules directory exists, not reinstalling..."
else
    cd $PROJECT_ROOT
    yarn install
fi
