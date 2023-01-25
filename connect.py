import psycopg2

conn = psycopg2.connect(
    host= '185.46.11.105',
    database='market-data',
    user='ilya',
    password= 'password')


cur = conn.cursor()

SQL = '''CREATE TABLE test (
        user_id serial PRIMARY KEY,
        username VARCHAR ( 50 ) UNIQUE NOT NULL,
        password VARCHAR ( 50 ) NOT NULL,
        email VARCHAR ( 255 ) UNIQUE NOT NULL,
        created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
);'''

cur.execute(SQL)


cur.close()
conn.commit()

conn.close()

