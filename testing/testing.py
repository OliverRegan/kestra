import pandas as pd
import psycopg2

connection = psycopg2.connect(database="postgres", user="sa", password="password", host="192.168.0.103", port=31350)

cursor = connection.cursor()

# sql = """CREATE TABLE public.cluster (
#     column_1 varchar(255),
#     column_2 varchar(255)
# );"""

# sql = """INSERT INTO public.cluster (column_1, column_2) VALUES (%s, %s);"""
sql = """SELECT * FROM public.cluster"""

# cursor.execute(sql, ("test_1", "test_2"))
cursor.execute(sql)

rows = cursor.fetchall()

print(rows)
# connection.commit()

# cursor.close()
# connection.close()

# print(cursor.fetchall())

# print("Hello World");

