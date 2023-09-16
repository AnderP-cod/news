from django.shortcuts import render


def index(request):
    data = {
        "tipe": ['Сайт сделан для публикации новостей',
                 'На этом сайте вы найдете все чтобы опубликовать свою статью, отредактировать или удалить ',
                 'Приятного чтения статей и их публикаций😊']
    }
    return render(request, 'mein/index.html', data)


def about(request):
    return render(request, 'mein/about.html')
