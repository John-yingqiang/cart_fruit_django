from django.core.cache import cache
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, render_to_response
from django.conf import settings
from django.template import RequestContext
import os.path
from forms import UploadForm
 
def upload_form(request):
  form = UploadForm()
  return render(request, 'upload_form.html', {'form': form})
 
def upload(request):
  if request.method == 'POST':
    for f in request.FILES:
      handle_uploaded_file(request.FILES[f])
    return HttpResponse('')
  return HttpResponse('Error')
 
def handle_uploaded_file(f):
  path = os.path.join(settings.MEDIA_ROOT, 'uploads', f.name)
  destination = open(path, 'wb+')
  for chunk in f.chunks():
    destination.write(chunk)
  destination.close()
 
def upload_progress(request):
  """
  Return JSON object with information about the progress of an upload.
  """
  progress_id = ''
  if 'X-Progress-ID' in request.GET:
    import urllib
    progress_id = request.GET['X-Progress-ID']
    list = eval(urllib.unquote_plus(request.GET['list']))
  if progress_id:
    import simplejson
    data = {
 
}
    for f in list:
      cache_key = "%s_%s_%s" % (request.META['REMOTE_ADDR'], progress_id, f)
      r = cache.get(cache_key)
      if(None == r):
        r = 0;
      data[f] = r
    return HttpResponse(simplejson.dumps(data))
  else:
    return HttpResponseServerError('Server Error: You must provide X-Progress-ID header or query param.')
 
def finish_upload(request):
  progress_id = ''
  if 'X-Progress-ID' in request.GET:
    import urllib
    progress_id = request.GET['X-Progress-ID']
    list = eval(urllib.unquote_plus(request.GET['list']))
  if progress_id:
    for f in list:
      cache_key = "%s_%s_%s" % (request.META['REMOTE_ADDR'], progress_id, f)
      cache.delete(cache_key)
    return HttpResponse(request.POST['description'] + ' upload successful')
  else:
    return HttpResponseServerError('Server Error: You must provide X-Progress-ID header or query param.')
