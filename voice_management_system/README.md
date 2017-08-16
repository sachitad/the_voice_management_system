# Installation
We are using python3!

Create virtualenv:
You might want to check your python3 executable path `which python3`
`mkvirtualenv voice_system --python=/usr/local/bin/python3`

Install the requirements
`pip install -r requirements.txt`

Migrate the database. We are using sqlite3 for now. We will change it to postgres in the future.
`python manage.py migrate`

Load the data for you to start using system right now:
`python manage.py load_data`

Credentials for you to start using system right away:
```sh
# SuperAdmin
username: admin
password: superman

# Mentor 
username: user0
password: valid

# System Admin (the one who is able to see all the teams)
username: admin4
password: valid
```
