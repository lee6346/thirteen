from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.urls import reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from config import secrets
import requests, uuid, json, urllib

import logging
log = logging.getLogger('thirteen')


@login_required(login_url='login/')
def index(request):
    log.debug('user has logged in')
    return render(request, 'index.html')


def lobby_partial(request):
    # get the HTML template from file system
    return render_to_response('partials/lobby.html')

def table_partial(request):
    return render_to_response('partials/table.html')

#todo must configure auth later
def get_tables(request):
    response = requests.get("https://thirteen-f7c9f.firebaseio.com/tables.json")
    return JsonResponse(response.text, safe=False)

def create_table_modal_partial(request):
    return render_to_response('partials/modals/create-table.html')

#http://stackoverflow.com/questions/29240940/how-do-you-authenticate-a-server-to-firebase
def create_table(request):
    new_table = {
        "id": str(uuid.uuid4()),
        "name": request.body,
        "num_players": 1
    }
    get_params = urllib.urlencode({'auth': secrets.firebase_secret})
    url = "https://thirteen-f7c9f.firebaseio.com/tables.json?" + get_params
    response = requests.post(url, json = new_table)
    print(response.text)

    return render_to_response('partials/table.html')
