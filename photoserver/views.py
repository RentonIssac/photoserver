import os

import json

from django.template import loader,Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt

from photoserver.models import MediaFile
from photoserver.forms import MediaFileForm
from photoserver.forms import CheckMediaFileExistForm

import photoserver.settings

@csrf_exempt
def test_show_xml( request ):
    result = ( 200, "OK", 0 )
    t = loader.get_template('result.xml')
    c = Context({'result':result})
    return HttpResponse( t.render(c), content_type="application/xml" )

@csrf_exempt
def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = MediaFile(owner=request.POST['owner'], mediafile=request.FILES['mediafile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('photoserver.views.upload'))
    else:
        form = MediaFileForm()  # A empty, unbound form

    #print 'xxxxxxx %s' % photoserver.settings.BASE_DIR
    # Load documents for the list page
    #MediaFile.objects.all().delete()
    documents = MediaFile.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

@csrf_exempt
def upload_json(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            mediafile_owner = request.POST['mediafile_owner']
            mediafile_size = request.POST['mediafile_size']
            mediafile_name = request.POST['mediafile_name']
            newdoc = MediaFile( mediafile=request.FILES['mediafile'], mediafile_owner=mediafile_owner, mediafile_size=mediafile_size, mediafile_name=mediafile_name )
            newdoc.save()

            response_data = {}
            response_data['rc'] = '200'
            response_data['message'] = 'OK'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        MediaFile.objects.all().delete()
        response_data = {}
        response_data['rc'] = '501'
        response_data['message'] = 'ERROR & DELETE ALL DATA'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def upload_json_check_exist(request):
    if request.method == 'POST':
        form = CheckMediaFileExistForm(request.POST, request.FILES)
        if form.is_valid():
            mediafile_owner = request.POST['mediafile_owner']
            mediafile_size = request.POST['mediafile_size']
            mediafile_name = request.POST['mediafile_name']

            response_data = {}
            try:
                MediaFile.objects.get( mediafile_owner=mediafile_owner, mediafile_size=mediafile_size, mediafile_name=mediafile_name )
                response_data['rc'] = '200'
                response_data['message'] = 'OK'
            except:
                response_data['rc'] = '404'
                response_data['message'] = 'FILE NOT FOUND'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data = {}
        response_data['rc'] = '500'
        response_data['message'] = 'ERROR'
        return HttpResponse(json.dumps(response_data), content_type="application/json")