#!/usr/bin/env bash

#delete db
rm -f db.sqlite3

# delete migrations as they can potentially cause problems
rm -f matcher/migrations/*.py
rm -rf matcher/migrations/__pycache__

#create migrations for matcher
python manage.py makemigrations mentorsforall

#create db
python manage.py migrate

#populate db
#script can now be called directly rather than STDIN > django shell
# also admin user is created in setupdb.py
python setupdb.py
