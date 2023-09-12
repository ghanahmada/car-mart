from django.shortcuts import render

# Create your views here.
def show_author(request):
    context = {
        "name": "Ghana Ahmada Yudistira",
        "class": "PBP B"
    }
    return render(request, "author.html", context)

def show_content(request):
    context = {
        'name': 'Porsche 918 Spyder',
        'amount': 918,
        'price': 1144000,
        'category': 'Sports Car',
        'description':"""The Porsche 918 Spyder stands out as a car with dual personalities. 
        It's a speed demon with a V8 engine and electric motors working together, dishing out 
        over 880 horsepower for an exhilarating ride. When you want to be eco-conscious, it's 
        got an electric mode for silent, emissions-free cruising. This car seamlessly combines 
        high-performance thrills and environmental responsibility, reflecting Porsche's dedication 
        to both power and the planet. """
    }

    return render(request, "content.html", context)