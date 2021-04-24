## How to run (on Linux)

```
# Cloning repository
git clone https://github.com/erayerturk/django-spotify.git
cd django-spotify

# Installing virtualenv
sudo apt-get install python3-venv
sudo apt install virtualenv

# Creating virtual environment
python3 -m venv venv
source venv/bin/activate

# Installing dependencies
pip3 install -r requirements.txt

# Creating DB
python3 manage.py migrate

# Running application
python3 manage.py runserver
```

## Third Party Libraries


- django-ninja==0.12.2
- requests==2.25.1


## Frontend

http://localhost:8000/frontend/

## Documentation

http://localhost:8000/api/docs
