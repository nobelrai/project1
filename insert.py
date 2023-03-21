from estd_connection import estd_connection
from read_csv import read_csv

data = read_csv()
cursor = estd_connection()

for each in data[:5]:
    date = each['date']
    symbol = each['symbol']
    name = each['name']
    high = each['high']
    low = each['low']

print(each)
sql = f"""
INSERT INTO MYSHARE(DATE, SYMBOL, NAME, HIGH, LOW)
VALUES('{date}', '{symbol}', '{name}', '{high}', '{low}')
"""

cursor.execute((sql))
print("Data inserted successfully")
