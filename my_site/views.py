from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:

    context: dict[str, str] = {"page_title": "Главная"}
    return render(request, "my_site/index.html", context)

def golden_ratio(request: HttpRequest) -> HttpResponse:
    context = {"page_title": "Золотое сечение"}
    return render(request, "my_site/golden_ratio.html", context)

def fractals(request: HttpRequest) -> HttpResponse:
    context = {"page_title": "Фракталы"}
    return render(request, "my_site/fractals.html", context)

def fibbonacci_numbers(request: HttpRequest) -> HttpResponse:
    context = {"page_title": "Числа Фиббоначи"}
    return render(request, "my_site/fibbonacci_numbers.html", context)

def golden_ratio_demo(request):
    # Пример данных для демо-страницы
    context = {
        "title": "Золотое сечение в веб-дизайне",
        "content": "Пример текста, который будет масштабироваться...",
        "image_url": "/static/images/Golden_Ratio_2.png",
    }
    return render(request, 'my_site/demo.html', context)