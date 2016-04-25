from django.db import models

class MediaFileOwner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=256)
    owner_add_time = models.DateTimeField(auto_now=True)

class MediaFile(models.Model):
    mediafile_id = models.AutoField(primary_key=True)
    mediafile = models.FileField(upload_to="MediaFiles/")
    mediafile_owner = models.ForeignKey(MediaFileOwner)
    mediafile_size = models.IntegerField()
    mediafile_name = models.CharField(max_length=256)
    mediafile_upload_time = models.DateTimeField(auto_now=True)
    def save(self):
        for field in self._meta.fields:
            if field.name == 'mediafile':
                field.upload_to = 'MediaFiles/%s' % self.mediafile_owner
        super(MediaFile, self).save()
