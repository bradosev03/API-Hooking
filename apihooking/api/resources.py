#api/resources

from tastypie.resources import ModelResource
from api.models import Notes

class NoteResource(ModelResource):
    class Meta:
        queryset = Notes.objects.all()
        resource_name = 'note'

