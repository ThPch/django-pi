from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
    #Action de l'utilisateur
    if request.method == 'POST':
        json_data = json.loads(request.body)

        #L'utilisateur souhaite se connecter au bluetooth
        if json_data['Bt_State'] == 'disconnected':
            print("Connexion au serveur")
            BT_STATUT = "connected"

        #L'utilisateur souhaite deconnecter du bluetooth
        elif json_data['Bt_State'] == 'connected':
            print("Deconnexion du serveur")
            BT_STATUT = "disconnected"

        context = {
            'BT_STATUT': BT_STATUT,
        }

    #Initialisation de la page
    if request.method == 'GET':
        BT_STATUT = "disconnected"

        context = {
            'BT_STATUT': BT_STATUT,
        }

    return render(request, "index.html", context)