'''
Объедините студентов в команды по 2-5 человек в сессионных залах.

Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет"

"Зачет" ставится, если Слушатель успешно выполнил задание.
"Незачет" ставится, если Слушатель не выполнил задание.

Критерии оценивания:
1 - Слушатель создал базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.


uvicorn app2:app --reload

'''
import logging
logging.basicConfig(level=logging.DEBUG)

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, NaiveDatetime
from typing import List, Optional
import datetime


DATABASE_URL = "sqlite:///mydatabase.db"  # Подключение к SQLite
#DATABASE_URL = "postgresql://user:password@localhost/dbname"  # Подключение к PostgreSQL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


#--- DataBase Tables ------
'''
id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
'''
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(32)),
    sqlalchemy.Column("second_name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(32)),
    sqlalchemy.Column("password", sqlalchemy.String(32)),
    )

'''
Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
'''
products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(1024)),
    sqlalchemy.Column("price", sqlalchemy.Float),
    )

'''
id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
'''
orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column("product_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id')),
    sqlalchemy.Column("date", sqlalchemy.DateTime),
    sqlalchemy.Column("status", sqlalchemy.String(16)),
    )

#-------------------------------------------------------------------------
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
    )

metadata.create_all(engine)

#--- pydantic models ------
class User_set(BaseModel):  # для добавления нового
    first_name: str = Field(max_length=64)
    second_name: str = Field(max_length=64)
    email: EmailStr = Field(..., max_length=64, validate_default=[])
    password: str = Field(..., min_length=6, max_length=64)

class User(BaseModel):  # для извлечения из БД
    id : int = Field()
    first_name: str = Field(max_length=64)
    second_name: str = Field(max_length=64)
    email: EmailStr = Field(max_length=64, validate_default=[])
    password: str = Field(min_length=6, max_length=64)

class Product_add(BaseModel):
    name: str = Field(max_length='64')
    description: str = Field(max_length='1024')
    price: float = Field()

class Product(BaseModel):
    name: str = Field(max_length='64')
    description: str = Field(max_length='1024')
    price: float = Field()

class Order_add(BaseModel):
    user_id : int = Field()
    product_id: int = Field()
    status: str = Field(default='NEW')

class Order(BaseModel):
    id: int = Field()
    user_id : int = Field()
    product_id: int = Field()
    date_create: NaiveDatetime = Field()
    status: str = Field()

#-------- FastAPI -----------------
app = FastAPI()

@app.get("/init_fake/")
async def create_note():
    users_count = 10
    products_count = 5
    orders_count = 100
    for i in range(users_count):
        query = users.insert().values(first_name=f'user{i}',
                                      second_name=f'family{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=f'password{i}')
        await database.execute(query)

    for i in range(products_count):
        query = products.insert().values(name=f'Product{i}',
                                      description=f'Description of product {i}',
                                      price=i)
        await database.execute(query)

    for i in range(orders_count):
        query = orders.insert().values(user_id = i % users_count,
                                       product_id = i % products_count,
                                       date = datetime.datetime.now(),
                                       status = 'NEW')
        await database.execute(query)

        sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id')),
        sqlalchemy.Column("product_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id')),
        sqlalchemy.Column("date", sqlalchemy.DateTime),
        sqlalchemy.Column("status", sqlalchemy.String(16)),


    return {'fake users and products created'}


@app.get("/")
async def home():
    users_list = await database.fetch_all(users.select())
    # for _usr in users_list:
    #     _usr['password'] = "***"
    products_list = await database.fetch_all(products.select())
    return {'users':users_list, 'products': products_list}


# --- users -------------------------------------------
@app.post("/users/")
async def users_add(user: User_set):
    query = users.insert().values(
        first_name=user.first_name,
        second_name=user.second_name,
        email=user.email,
        password=user.password)
    last_record_id = await database.execute(query)
    return {'id': last_record_id}

@app.get("/users/{user_id}")
async def users_read(user_id):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_all(query)

@app.put("/users/{user_id}", response_model=User)
async def users_modify(user_id: int, new_user: User_set):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {'id': user_id, **new_user.dict()}

@app.delete("/users/{user_id}")
async def users_delete(user_id):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'id': user_id, 'message': 'User deleted'}

# --- products -------------------------------------------
@app.post("/products/")
async def products_add(product: Product_add):
    query = products.insert().values(
        name=product.name,
        description=product.description,
        price=product.price)
    last_record_id = await database.execute(query)
    return {'id': last_record_id}

@app.get("/products/{product_id}")
async def products_read(product_id):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_all(query)

@app.put("/products/{product_id}", response_model=Product_add)
async def product_modify(product_id: int, new_product: Product_add):
    logging.info(new_product)
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {'id': product_id, **new_product.dict()}

@app.delete("/products/{product_id}")
async def product_delete(product_id):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'id': product_id, 'message': 'Product deleted'}

# --- orders ---------------------------------------------
@app.post("/orders/")
async def orders_add(order: Order_add):
    query = orders.insert().values(
        user_id = order.user_id,
        product_id = order.product_id,
        date_create=datetime.datetime.now(),
        status = order.status)
    last_record_id = await database.execute(query)
    return {'id': last_record_id}

@app.get("/orders/{order_id}")
async def orders_read(order_id):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_all(query)

@app.put("/orders/{order_id}")
async def order_modify(order_id: int, new_order: Order_add):
    logging.info(new_order)
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {'id': order_id, **new_order.dict()}

@app.delete("/orders/{order_id}")
async def order_delete(order_id):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'id': order_id, 'message': 'Оrder deleted'}

# --------------------------------------------------------
# if __name__ == '__main__':
#     uvicorn.run(app)
