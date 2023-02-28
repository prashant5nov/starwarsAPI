"""
TODO

1. Pull data for the first movie ("A New Hope") and save in DB.

2. Replace the data for each endpoint listed in the JSON object and insert
that data into database table

For example - "A new hope" movie has following resource endpoints -

- characters 15
- planets  7
- starships   10
- vehicles  5
- species  40


"""

from resources.films import Film   # resource model
from models.datamodels.films import Film_  # pydantic model

from dal.db_conn_helper import get_db_conn


if __name__ == "__main__":
    data = Film().get_sample_data(id_=1)
    film_data = Film_(**data)

    # create DB connection
    conn = get_db_conn()

    # to create a sql query to insert data into database.
    # DDL - CREATE
    # DML - SELECT, INSERT, UPDATE

    magic_sql = "INSERT INTO {database}.{table} ({column1}, {column2}, ....)" \
                "VALUES ({value1}, {value2})"


    # execute the query



