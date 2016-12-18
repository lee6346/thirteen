from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.urls import reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import logging
log = logging.getLogger('thirteen')


@login_required(login_url='login/')
def index(request):
    log.debug('user has logged in')
    return render(request, 'index.html')


def lobby_partial(request):
    # get the HTML template from file system
    return render_to_response('partials/lobby.html')


def get_tables(request):
    a = [
        {
            'Name': 'table1',
            'AvailableSeats': 5,
            'Id': 100
        },
        {
            'Name': 'table2',
            'AvailableSeats': 4,
            'Id': 124
        },
        {
            'Name': 'table3',
            'AvailableSeats': 6,
            'Id': 55
        },
    ]
    return JsonResponse(a, safe=False)
