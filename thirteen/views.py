from django.http import HttpResponse, HttpResponseRedirect
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

def test_template(request):
    # get the HTML template from file system
    return render_to_response('partials/test.html')