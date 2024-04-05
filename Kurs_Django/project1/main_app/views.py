from django.shortcuts import render

import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

#html_template = ''

def home(request):
    logger.info('Страница HOME')

    html = (html_template
            .replace('<!-- title -->', "Home page")
            .replace('<!-- content -->', "Домашняя старница с привествием"))

    return HttpResponse(html)

def about(request):
    logger.info('Страница Об')
    html = (html_template
            .replace('<!-- title -->', "Об мене")
            .replace('<!-- content -->', "Я есть Грут.<br />\\_(о0)_/"))
    return HttpResponse(html)

html_template = '''
<html>
<head>
    <meta charset="UTF-8">
<style>
body{
            background: #eee; /* цвет фона страницы */
}
.Myform{
            width:300px; /* ширина блока */
            background: #fff; /* фон блока */
            border-radius: 10px; /* закругленные углы блока */
            margin: 10% auto; /* отступ сверху и выравнивание по середине */
            box-shadow: 2px 2px 4px 0px #000000; /* тень блока */
}
.Myform h1 {
            margin: 0; /* убираем отступы */
            background-color: #282830; /* фон заголовка */
            border-radius: 10px 10px 0 0; /* закругляем углы сверху */
            color: #fff; /* цвет текста */
            font-size: 14px; /* размер шрифта */
            padding: 20px; /* отступы */
            text-align: center; /* выравниваем текст по центру */
            text-transform: uppercase; /* все символы заглавные */
}
.inp{
            padding:20px; /* отступы */
}

input{
            border: 1px solid #dcdcdc; /* рамка */
            padding: 12px 10px; /* отступы текста */
            width: 260px; /* ширина */
            border-radius: 5px 5px 0 0; /* закругленные углы сверху */
}

.btn{
            background: #1dabb8; /* фон */
            border-radius: 5px; /* закругленные углы */
            color: #fff; /* цвет текста */
            /*float: right; /* выравнивание справа */
            font-weight: bold; /* жирный текст */
            margin: 10px; /* отступы */
            padding: 12px 20px; /* оступы для текста */
}

.info{
            width:130px; /* ширина */
            float: left; /* выравнивание слева */
}
a{
            color:#999; /* цвет ссылки */
            text-decoration: none; /* убираем подчеркивание */

}
a:hover{
            color: #1dabb8; /* цвет ссылки при наведении */

}

</style>
</head>
<body>

<div class="Myform">

    <h1><!-- title --></h1>

    <div class="inp">
        <!-- content -->
    </div>

</div>

</body>
</html>

'''

