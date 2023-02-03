import psycopg2

def get_connection(db_name):
    connection = psycopg2.connect(
        dbname=db_name ,
        host= 'localhost',
        user='postgres',
        password='03041996'
    )
    return connection

def create_customer():
    name=input('Введите имя покупателя: ')
    age=input('Введите возраст: ')
    address=input('Введите адресс: ')
    balance=input('Введите баланс: ')
    query = f"""INSERT INTO customers (name,age,address,balance)
        VALUES (\'{name}\',{age},\'{address}\',{balance})"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def create_order():
    name = input('Введите имя покупателя: ')
    product = input('Введите желаемый товар: ')
    count = int(input('Введите количество товара: '))
    query = f"""BEGIN TRANSACTION"""
    with conn.cursor() as cursor:
        cursor.execute(query)
    query = f"""SELECT id FROM customers WHERE name='{name}'"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        customer_id= cursor.fetchall()
    # print(f'customer_id: {customer_id}')
    query = f"""SELECT id, price, discount FROM products WHERE name='{product}'"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        product_data= cursor.fetchall()
    # print(f'product_data: {product_data}')
    with conn.cursor() as cursor:
        query = f"""INSERT INTO orders (product_count,customer_id,product_id)
                    VALUES ({count},{customer_id[0][0]},{product_data[0][0]})"""
        cursor.execute(query)
    with conn.cursor() as cursor:
        # print(type(product_data[0][2]))
        discount= 0 if not isinstance(product_data[0][2], int) else product_data[0][2]
        order_price=count*product_data[0][1]*(100-discount)/100
        # print(order_price)
        query = f"""UPDATE customers 
                    SET balance=balance-{order_price}
                    WHERE id={customer_id[0][0]}"""
        cursor.execute(query)
    with conn.cursor() as cursor:
        query = f"""UPDATE products 
                    SET count_in_stock=count_in_stock-{count}
                    WHERE id={product_data[0][0]}"""
        cursor.execute(query)
    query = f"""COMMIT TRANSACTION"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
    print(f'Итоговая цена на товар {product} в количестве {count}шт с учетом скидки в {discount}%: {order_price}')



def get_product():
    product = input('Введите желаемый товар: ')
    query = f"""select (select name as category_name from category where id=products.category_id),name,price,count_in_stock,discount,description 
                from products 
                where name='{product}'"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        customer_id = cursor.fetchall()
    print(f'Категория товара: {customer_id[0][0]}\n'
          f'Наименование товара: {customer_id[0][1]}\n'
          f'Цена товара: {customer_id[0][2]}\n'
          f'Количество товара на складе: {customer_id[0][3]}\n'
          f'Скидка: {customer_id[0][4]}\n'
          f'Описание товара: {customer_id[0][5]}\n')

def get_customers_orders():
    customer = input('Введите имя покупателя: ')
    query = f"""select (select name as product_name from products where id=orders.product_id), product_count
                    from orders 
                    where customer_id=(select id from customers where name=\'{customer}\')"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        customers_orders = cursor.fetchall()
        print(f'Покупатель: {customer} '
              f'Заказы: ')
        for item in customers_orders:
            print(f'\tНаименование продукта: {item[0]}, колличество: {item[1]}')


def get_products_discount():
    discount = int(input('Введите желаемую скидку на товар: '))
    query = f"""select (select name as category_name from category where id=products.category_id),name,price,price*(100-discount)/100 as discounted_price,count_in_stock,description 
                    from products 
                    where discount={discount}"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        products_discounted = cursor.fetchall()
    for item in products_discounted:
        print(f'\tКатегория: {item[0]}\t|'
              f'\tНаименование продукта: {item[1]}\t|'
              f'\tЦена без скидки: {item[2]}\t|'
              f'\tЦена со скидкой: {item[3]}\t|'
              f'\tКолличество на складе: {item[4]}\t|'
              f'\tОписание продукта: {item[5]}\t|')
def get_summary():
    name = input('Введите имя покупателя: ')
    product = input('Введите желаемый товар: ')
    count = int(input('Введите количество товара: '))
    query = f"""SELECT id, price, discount FROM products WHERE name='{product}'"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        product_data = cursor.fetchall()
        discount = 0 if not isinstance(product_data[0][2], int) else product_data[0][2]
        order_price = count * product_data[0][1] * (100 - discount) / 100
    print(f'Уважаемый(-ая) {name}, итоговая цена на товар {product} в количестве {count}шт с учетом скидки в {discount}%: {order_price}')


with get_connection('test_db') as conn:
    with conn.cursor() as cursor:
        query = """CREATE TABLE IF NOT EXISTS category
        (
        id serial primary key,
        name varchar(64)
        );"""

        cursor.execute(query)
        query = """CREATE TABLE IF NOT EXISTS products 
        (
        id serial primary key,
        name varchar(64),
        price int,
        count int,
        description varchar(256),
        category_id int references category(id)
        );"""
        cursor.execute(query)

        query = """CREATE TABLE IF NOT EXISTS orders
        (
        id serial primary key,
        product_count int,
        customer_id int references customers(id),
        product_id int references products(id)
        );"""
        cursor.execute(query)
        conn.commit()

    # with conn.cursor() as cursor:
    #     # query = """INSERT INTO customers (name,age,address,balance)
    #     # VALUES ('John',25,'some address 1',1000)"""
    #
    #     # query = """INSERT INTO customers (name,age,address,balance)
    #     # VALUES ('Mary>',24,'some address 2',2000)"""
    #
    #     # query = """INSERT INTO category (name)
    #     # VALUES ('cat_1'),('cat_2')"""
    #
    #
    #     # query = """INSERT INTO products (name,price,count,description,category_id)
    #     # VALUES ('product_1',100,10,'some description 1',1),
    #     # ('product_2',200,20,'some description 2',2)"""
    #     # query = """INSERT INTO orders (product_count, customer_id,product_id)
    #     # VALUES (2,1,1),(5,2,2)"""
    #     cursor.execute(query)
    #
    #     conn.commit()
    # with conn.cursor() as cursor:
    #     query = """SELECT * FROM category;"""
    #     cursor.execute(query)
    #     data = cursor.fetchall()
    #     print(f'category data: {data}')
    #
    #     query = """SELECT * FROM products JOIN category ON products.category_id = category.id;"""
    #     cursor.execute(query)
    #     data = cursor.fetchall()
    #     print(f'products data: {data}')
    #     for item in data:
    #         print(f'product id: {item[0]},\n'
    #               f'product name: {item[1]},\n'
    #               f'product price: {item[2]},\n'
    #               f'product count: {item[3]},\n'
    #               f'product description: {item[4]},\n'
    #               f'product category id: {item[5]},\n'
    #               f'product category name: {item[7]},\n'
    #               )

    # with conn.cursor() as cursor:
    #     # query = """ALTER TABLE products RENAME COLUMN count_stock TO count_in_stock;"""
    #     query = """ALTER TABLE products ALTER COLUMN discount TYPE int USING discount::int;"""
    #
    #     cursor.execute(query)
    #     conn.commit()

    while True:
        inputed_commmand= input("""
        Выберите опцию(1..6):
        1) Создать нового покупателя;
        2) Создать новый заказ;
        3) Получить информацию о конкретном продукте;
        4) Получить информация о заказах конкретного пользователя;
        5) Получить информацию о продуктах с конкретной скидкой;
        6) Предрасчет заказа;
        7) Выход.
-->>""")
        if not inputed_commmand.isdigit():
            print('Введено не верное значение. Выберите опцию от 1 до 6')
            continue
        elif int(inputed_commmand)==1:
            create_customer()
        elif int(inputed_commmand)==2:
            create_order()
        elif int(inputed_commmand)==3:
            get_product()
        elif int(inputed_commmand)==4:
            get_customers_orders()
        elif int(inputed_commmand)==5:
            get_products_discount()
        elif int(inputed_commmand)==6:
            get_summary()
        elif int(inputed_commmand)==7:
            break
        else:
            print('Введено не верное значение. Выберите опцию от 1 до 6')
            continue