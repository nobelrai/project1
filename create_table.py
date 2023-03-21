from estd_connection import estd_connection

cursor = estd_connection()
cursor.execute("DROP TABLE IF EXISTS MYSHARE")

sql = """ CREATE TABLE MYSHARE( DATE CHAR(20), SYMBOL CHAR(20), NAME CHAR(100), HIGH FLOAT, LOW FLOAT ) """

cursor.execute(sql)
print("Table created successfully")
