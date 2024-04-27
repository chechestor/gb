from django.db import models

# Create your models here.
from django.db import models

# Клиент
class Client(models.Model):
    name = models.CharField(max_length=64) #— имя клиента
    email = models.EmailField()    #— электронная почта клиента
    phone = models.CharField(max_length=64)    #— номер телефона клиента
    address = models.CharField(max_length=128)    #— адрес клиента
    reg_date = models.DateTimeField()   #— дата регистрации клиента
    def __str__(self):
        return (f'pk: {self.pk}, '
                f'name: {self.name}, '
                f'email: {self.email}, '
                f'phone: {self.phone}, '
                f'address: {self.address}, '
                f'red_date: {self.reg_date}')

# Товар
class Product(models.Model):
    name = models.CharField(max_length=64)  # название товара
    description = models.CharField(max_length=128)  # описание товара
    price = models.DecimalField(decimal_places=2, max_digits=10)# цена товара
    quantity = models.IntegerField()# количество товара
    reg_date = models.DateTimeField()   # дата добавления товара
    image = models.FilePathField(default='')  # имя файла продукта
    picture = models.ImageField(default='')  # имя файла продукта
    def __str__(self):
        return (f'pk: {self.pk}, '
                f'name: {self.name}, '
                f'description: {self.description}, '
                f'price: {self.price}, '
                f'quantity: {self.quantity}, '
                f'red_date: {self.reg_date}, '
                f'image: {self.image}, '
                f'picture: {self.picture}')

# Заказ

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
    #todo так-то, по-хорошему, надо еще и учитывать, что каждого товара может быть несколько
    products = models.ManyToManyField(Product)  # — связь с моделью «Товар», указывает на товары, входящие в заказ
    total_price = models.DecimalField(decimal_places=2, max_digits=10, null=True)  # — общая сумма заказа
    reg_date = models.DateTimeField()  # — дата оформления заказа    def __str__(self):
    def __str__(self):
        return (f'pk: {self.pk}, '
                f'client: {self.client}, '
                #f'products: {self.products}, '
                f'total_price: {self.total_price}, '
                f'reg_date: {self.reg_date}')

