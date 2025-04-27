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


from django.http import HttpResponse

def random_pattern(request: HttpRequest) -> HttpResponse:
    svg_content = f'''
    <svg ...>
        <circle cx="{random.randint(10,90)}" cy="{random.randint(10,90)}" ...>
    </svg>'''
    
    return HttpResponse(svg_content, content_type='image/svg+xml')