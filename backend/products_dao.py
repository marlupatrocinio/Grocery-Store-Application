import mysql.connector

conn = mysql.connector.connect(user = 'root', password = '123456Pw!',
                               host = 'localhost',
                               database = 'GS_app')

cursor = conn.cursor()

query = ('SELECT * FROM Product;')
cursor.execute(query)

for (product_id, product_name, uom_id, price_per_unit) in cursor:
    print(product_id, product_name, uom_id, price_per_unit)
conn.close()