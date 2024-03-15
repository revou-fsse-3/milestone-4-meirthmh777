# Mbanking App RESTful API

## Requirement for Milestone 4

### How to run this project

1. create virtual environment : cntrl+shift+p, >Python: Create Environment, venv, create venv based on recommendation.
2. set up virtual environment: poetry shell
3. install all dependencies : poetry install
4. run this project : poetry run flask run

### How to set up the database

note: I use migrate in this project to make sure the database updates are saved.
in your terminal:

1. set up database : poetry run flask db
2. generate any migration : poetry run flask db migrate -m "your comment"
3. apply changes : poetry run flask db upgrade

#### Good luck! 🤞🏻

#### meirthmh
