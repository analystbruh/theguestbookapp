# theguestbookapp
me practicing with postgresql and flask. Below is the process I used.

### install homebrew if you don't have it on mac:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

### make sure homebew is up to date if you already have it:
$ brew update

### install postrgres (first remove old postgres if it's already installed on your mac):
$ brew install postgresql

start stop postgres installed with homebrew:
$ pg_ctl -D /usr/local/var/postgres start
$ pg_ctl -D /usr/local/var/postgres stop

start the postgres server
instal pgadmin4 and use that to create the database to use in the app. pgadmin4 makees this easy.

build your app.

push flask app to heroku:
necessary files and libraries
-lib gunicorn
-lib flask-heroku (for heroku CLI)
-file reqirements.txt
-file Procfile (case sensitive, no extension) --> contents-> web: gunicorn app:app
-file runtime.txt --> contents-> python-x.x.x

install git and heroku:
$ brew install git
$ brew install heroku/brew/heroku

pushing the app out:
(install git and heroku CLI with homebrew)
in terminal cd to project directory
$ git init
$ git add .
$ git commit -m "comments"
$ heroku
$ git push heroku master

log into heroku account on the site, provision and add db
you can try this as well:
$ heroku addons:create heroku-postgresql:hobby-dev (hobby-dev is free)

go back to terminal:
$ heroku config (will show you database url)

copy DATABASE_URL and replace uri in app with it then:
$ git add app.py (or whatever filename)
$ git commit -m "comments" --dry-run (too see what is changing)
$ git commit -m "comments" (actual commit to local repo)
$ git push heroku master

create tables in new your new db on heroku based on model in app:
$ heroku run python
>>> from app import db (or from whatever the app name is)
>>> db.create_all()
>>> exit()
$ heroku logout

app should be live and working @ https://apps-name.herokuapp.com
