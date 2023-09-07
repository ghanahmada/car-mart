from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Mazda 3 2021',
        'amount': 10,
        'price': 400000000,
        'category': 'SUV',
        'description':"""Mazda 3 2021 adalah salah satu model mobil kompak yang populer dari produsen otomotif Jepang, 
                        Mazda. Mobil ini telah mendapatkan banyak pengakuan atas desainnya yang elegan, kualitas bahan 
                        yang baik, serta pengalaman mengemudi yang memuaskan. """
    }

    return render(request, "main.html", context)