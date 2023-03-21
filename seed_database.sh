rm db.sqlite3
rm -rf ./lockedinapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations lockedinapi
python3 manage.py migrate lockedinapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata muscleGroups
python3 manage.py loaddata difficulty
python3 manage.py loaddata equipment
python3 manage.py loaddata exercises
python3 manage.py loaddata routines
python3 manage.py loaddata exerciseRoutines
# Run this command to seed database:    chmod u+x ./seed_database.sh