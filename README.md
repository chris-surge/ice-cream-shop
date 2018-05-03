# install stuff
`pip install -r requirements.txt` will install dependencies, if you get permission errors
then put `sudo ` in front of the command

# start the server
`python manage.py runserver`

# reset database
just delete "db.sqlite3" and run `python manage.py migrate`

# set an admin password
`python manage.py createsuperuser` and you can go to http://{youraddress}:{port}/admin

default username and password are the same for existing database: `admin / admin`
