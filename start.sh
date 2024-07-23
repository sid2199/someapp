#!/usr/bin/bash

set -ex

port=8000
if [[ $1 != "" ]]; then
	port=$1
fi


source ../env/bin/activate

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:$port

