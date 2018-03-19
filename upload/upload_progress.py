from django.core.files.uploadhandler import FileUploadHandler
from django.core.cache import cache
 
class UploadProgressCachedHandler(FileUploadHandler):
    """
    Tracks progress for file uploads.
    The http post request must contain a header or query parameter, 'X-Progress-ID'
    which should contain a unique string to identify the upload to be tracked.
    """
 
    def __init__(self, request=None):
        super(UploadProgressCachedHandler, self).__init__(request)
        self.progress_id = None
        self.field_name = None
        self.cache_key = None
        self.received = 0
        self.length = 0
 
    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        if 'X-Progress-ID' in self.request.GET and content_length > 0:
            self.progress_id = self.request.GET['X-Progress-ID']
            self.length = content_length
 
    def new_file(self, field_name, file_name, content_type, content_length, charset=None):
        if self.progress_id:
            self.cache_key = "%s_%s_%s" % (self.request.META['REMOTE_ADDR'], self.progress_id, field_name)
            cache.set(self.cache_key, 0)
 
    def receive_data_chunk(self, raw_data, start):
        self.received += self.chunk_size
        if self.cache_key:
            p = min(100, int(100 * self.received / self.length))
            cache.set(self.cache_key, p)
        return raw_data
     
    def file_complete(self, file_size):
        if self.cache_key:
            cache.set(self.cache_key, 100)
 
    def upload_complete(self):
        pass