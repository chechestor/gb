from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    global db
    db.init_app(app)

def install():
    global db
    db.create_all()
    print('DB init done!')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    second_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    def __str__(self):
        return f'User({self.username}, {self.email})'
    def __repr__(self):
        return f'User({self.username}, {self.email})'


def get_user(email, password):
    #todo проверяем, чо есть такой пользователь. Возвращаем None, если нет такого пользователя или пароль не подходит
    user = User.query.filter(User.email == email).all()
    if not user:
        print("NO USER")
        return None
    user = user[0]
    if user.password != password:
        print("INCORRECT PASSWORD")
        return None
    print("RETURN USER")
    return user

def user_exists(email):
    #todo проверяем, чо есть такой пользователь. Возвращаем None, если нет такого пользователя или пароль не подходит
    user = User.query.filter(User.email == email).all()
    if not user:
        print("NO USER")
        return None
    return True

def add_user(email, password, first_name, second_name):
    #todo добавляем нового пользователя, если такой польщователь уже сущетсвует, то возвращаем None
    user = User(first_name=first_name,
                second_name=second_name,
                email=email,
                password=password)
    db.session.add(user)
    db.session.commit()
    print('User added!')
    return True

