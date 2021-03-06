# Endpoints for storing a Constellation

Small prototype to explore the option of opening an endpoint to Northwell's digital team to allow for storing and retrieving data associated with a gigya id.

You can create a database with example data by running the command `python load_db.py`.

This creates a sqlite DB with one table "payload" with a few columns, the meaningful ones are "gigya_id" and "payload". The payload column is simply a string value that takes whatever the digital team pushes and stores that, assuming it's a JSON. We could ETL the payload into a more robust data model once the structure is known.

`models.py` shows the schema of the database and a method to load data.

`main.py` is the flask app, it has 4 endpoints.

`payload.db` is the sqlite database, this can be easily migrated to any cloud SQL db.

`requirements.txt` is a list of all the dependencies needed to run this program. You can install all of these via `pip install -r requirements.txt`.

