from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'MatroSkin - Главная',
        'content': "MatroSkin"

    }

    return render(request, 'main/index.html', context)
    

def about(request):
    context = {
        'title': 'MatroSkin - О нас',
        'content': "О нас",
        'text_on_page': "Мы бренд одежды MatroSkin. Изготавливаем вышивку и печать объемных логотипов и изображений любой сложности и любого дизайна на футболках, худи, свитшотах. Вы можете предложить свой дизайн вышивки, цвет, размер, либо выбрать готовый вариант."
    }

    return render(request, 'main/about.html', context)