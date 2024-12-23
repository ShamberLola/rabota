from psycopg2 import Error
import psycopg2.extras

try:
    connection = psycopg2.connect(user="postgres",
                                  password="hohol",
                                  host="localhost",
                                  port="5432",
                                  database="washing_machine")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print("You are connected to base")

except (Exception, Error) as error:
    raise TypeError("Error while connecting to PostgreSQL", error)