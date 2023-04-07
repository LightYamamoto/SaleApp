# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import text

# Execute code in Docker 
# conn_str = "postgresql+psycopg2://nhatnguyen1011997:1011997@postgres_db:5434/database"

# # Execute code in local
# conn_str = "postgresql+psycopg2://nhatnguyen1011997:1011997@localhost:5434/database"

# engine = create_engine(conn_str)
# connection = engine.connect()


# result = connection.execute(text("SELECT * FROM Users;"))

# result.fetchall()

# connection.close()
import psycopg2

# from sqlalchemy import create_engine
# conn = psycopg2.connect('postgresql://nhatnguyen1011997:1011997%40postgres:5434/database')

# Connect to existing database
conn = psycopg2.connect(
    database="database",
    user="nhatnguyen1011997",
    password="1011997",
    host="postgres",
    port ='5434'
)

# Open cursor to perform database operation
cur = conn.cursor()

# Query the database 
cur.execute("CREATE TABLE IF NOT EXISTS Users (userId SERIAL PRIMARY KEY,firstName varchar(255) NOT NULL,phone bigint NOT NULL);")
cur.execute("INSERT INTO Users(firstName, phone) VALUES ('Nguyen', 12321312321),('Yamamoto', 432723472346);")

# cur.fetchall()
# for row in rows:
#     print(row)

# Close communications with database
cur.close()
conn.close()




