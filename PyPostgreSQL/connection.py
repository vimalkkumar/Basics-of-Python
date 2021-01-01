import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="testpython",
    user="postgres",
    password="15786kumar@#"
)

cursor = con.cursor()
# cursor.execute("""CREATE TABLE stand (name char(40));""")
# cursor.execute("""INSERT INTO stand (name) VALUES ('Vijay')""")
cursor.execute("""SELECT * from stand""")
con.commit() # <--- makes sure the change is shown in the database
# con.close()
# cursor.close()
rows = cursor.fetchall()
print(rows, end='\n')

# try:
#     connect_str = "dbname='testpython' user='vimal' host='localhost' " + \
#                   "password='15786kumar@#'"
#     # use our connection values to establish a connection
#     conn = psycopg2.connect(connect_str)
#     # create a psycopg2 cursor that can execute queries
#     cursor = conn.cursor()
#     # create a new table with a single column called "name"
#     # cursor.execute("""CREATE TABLE tutorials (name char(40));""")
#     # run a SELECT statement - no data in there, but we can try it
#     cursor.execute("""SELECT * from tutorials""")
#     conn.commit() # <--- makes sure the change is shown in the database
#     conn.close()
#     cursor.close()
#     rows = cursor.fetchall()
#     print(rows)
# except Exception as e:
#     print("Uh oh, can't connect. Invalid dbname, user or password?")
#     print(e)