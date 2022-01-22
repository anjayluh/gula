# Git setup

1. `git clone https://github.com/anjayluh/gula.git`
2. `cd gulaNative`

# Server Installation

1. Install pipenv `pip install pipenv`
1. Set up the pipenv `pipenv install --dev` to install dependencies
    - you will need to have postgres installed if you want to run against
      psycopg2. Make sure you have the proper requirements for psycopg2 before
      pipenv instaling.
1. `pipenv shell` to active the virtual environment
1. Run database migrations `python manage.py migrate`
1. Create directories and files necessary for initial data fixtures `python manage.py runscript hydrate_filesystem`
1. Run `collectstatic` to populate static file directory `python manage.py collectstatic`
1. Create a superuser with `python manage.py createsuperuser`
1. Run dev server `python manage.py runserver 0.0.0.0:8000`
1. Browse to http://localhost:8000/
1. Confirm you can log in to the admin at http://localhost:8000/admin

## Mobile App (React Native)

1. Install nodejs - tested on v8.1.2
2. Install yarn
3. `cd gulaNative`
4. `yarn`

### Commands

 * `yarn start` - Run react-native android to point at a local emulator
 * `yarn android` - Run react-native android to point at local emulator on windows machine

 ## Astra

1. Install nodejs - tested on v8.1.2
2. Install yarn
3. `cd gulaNative`
4. `yarn`

### Commands

 * `yarn start` - To start development server
 * `yarn android` - To start development server
 