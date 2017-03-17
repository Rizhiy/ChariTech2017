
DB='db.sqlite3'

rm $DB
python manage.py makemigrations
python manage.py migrate

/bin/sqlite3 $DB 'INSERT INTO slate2learn_centre (id) VALUES (1);'
/bin/sqlite3 $DB 'INSERT INTO slate2learn_centre (id) VALUES (2);'
/bin/sqlite3 $DB 'INSERT INTO slate2learn_centre (id) VALUES (3);'

/bin/sqlite3 $DB < ./slate2learn/data/csv/import.sql
