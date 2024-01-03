import mysql.connector

def get_all_products():
    conn = mysql.connector.connect(user = 'root', password = '123456Pw!',
                                    host = 'localhost',
                                    database = 'GS_app')

    cursor = conn.cursor()

    query = ('SELECT Product.product_id, Product.product_name, Product.uom_id, Product.price_per_unit, uom.uom_name FROM Product INNER JOIN uom ON Product.uom_id = uom.uom_id;')
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
    conn.close()
    return response

if __name__ == '__main__':
    print(get_all_products())