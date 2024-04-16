## Задание

Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
- имя клиента
- электронная почта клиента
- номер телефона клиента
- адрес клиента
- дата регистрации клиента

Поля модели «Товар»:
- название товара
- описание товара
- цена товара
- количество товара
- дата добавления товара

Поля модели «Заказ»:
- связь с моделью «Клиент», указывает на клиента, сделавшего заказ
- связь с моделью «Товар», указывает на товары, входящие в заказ
- общая сумма заказа
- дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой ба

## Решение

В Базе катулаьно добавление всех сущностей (клиент, товар, заказ), изменение всех сущностей (на случай ошибок оператора при вводе). Удаление актуально только на случаи чистки БД от безнадежно утаревших записей, если совсем плохо живется с большим размером БД. А так вообще, пусть остается история.


### Создание и просмотр двух клинетов

python manage.py client_create Peater mil@mail.ru +79265646830 "Bakery streek London"
python manage.py client_create Mikhael momo@gmail.com +7966123456 "Bishkeke City Chuy 110"
python manage.py client_list

### Создание и просмотр двух товаров

python manage.py product_create tapki 1.12 10 'Every day usage carpers'
python manage.py product_create shlepki 2.27 10 'Sea visit carpers'
python manage.py product_list


### Создание и просмотр заказа

python manage.py order_create 1 1 2
python manage.py order_list

### Изменение товаров в заказе

python manage.py order_update 1 2
python manage.py order_list

### Удаление и просмотр заказа

python manage.py order_delete 1
python manage.py order_list





