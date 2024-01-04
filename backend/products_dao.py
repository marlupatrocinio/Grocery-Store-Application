from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()

    query = ("SELECT Product.product_id, Product.product_name, Product.uom_id, Product.price_per_unit, uom.uom_name "
             "FROM Product INNER JOIN uom ON Product.uom_id = uom.uom_id;")
    cursor.execute(query)
    
    response = []
    for (product_id, product_name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': product_name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    return response

def insert_new_product(connection, product_data):
    cursor = connection.cursor()
    query = ("INSERT INTO Product "
             "(product_name, uom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (product_data['product_name'], product_data['uom_id'], product_data['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM Product WHERE product_id = %s" 
    cursor.execute(query, (product_id,))
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
  
    print(delete_product(connection, 10))