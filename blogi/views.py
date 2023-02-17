from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Postaus


def postaukset(request):
    postaukset = Postaus.objects.all()
    context = {"postaukset": postaukset}
    return render(
        request,
        "blogi/postauslista.html",
        context,
    )


def nayta_postaus(request, id):
    postaus = Postaus.objects.get(id=id)
    context = {"postaus": postaus}
    return render(request, "blogi/postaus.html", context)


def uusi_postaus(request):
    if request.method == "GET":
        # 1. Lomake näytetään ensimmäistä kertaa
        return render(request, "blogi/uusi postaus.html")
    elif request.method == "POST":
        # 2. Käyttäjä täytti ja lähetti lomakkeen

        # Luetaan lomakkeen tiedot POST-datasta
        otsikko = request.POST['otsikko']
        teksti= request.POST['teksti']

        # Luodan uusi Postaus-objekti
        postaus = Postaus.objects.create(
            otsikko=otsikko,
            teksti=teksti,
        )

        # Muodostetaan URL-osoite luotuun Postaus-objektiin
        url = reverse('nayta_postaus', args=(postaus.id,))
        
        # Palautetaan uudelleenohjaus uuden postaus-objektin URL:iin
        return redirect (url)