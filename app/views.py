from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, "index.html")


@csrf_exempt
def bluetooth(request):
    # if request.method == 'POST':
    #     json_data = json.loads(request.body)

    #     if json_data['Bt_State'] == 'unconnected':
    #         print("Connexion au serveur")
    #         ETAT_BT = True
    #         BT_STATUT = "connected"
    #         BTN_BT_STATUT = "Cliquer pour déconnecter"

    #     elif json_data['Bt_State'] == 'connected':
    #         print("Deconnexion du serveur")
    #         ETAT_BT = False
    #         BT_STATUT = "unconnected"
    #         BTN_BT_STATUT = "Cliquer pour déconnecter"

    #     context = {
    #         'BT_STATUT': BT_STATUT,
    #         'BTN_BT_STATUT': BTN_BT_STATUT,
    #     }

    # if request.method == 'GET':
    #     ETAT_BT = False
    #     BT_STATUT = "unconnected"
    #     BTN_BT_STATUT = "Cliquer pour connecter"

    #     context = {
    #         'BT_STATUT': BT_STATUT,
    #         'BTN_BT_STATUT': BTN_BT_STATUT,
    #     }

    return render(request, "bluetooth.html")
