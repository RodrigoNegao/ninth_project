from django.db import models
#taggit packge
from taggit.managers import TaggableManager
from django_extensions.db.fields import AutoSlugField

def my_slugify_function(content):
    return content.replace('_', '-').lower()

# Create your models here.
class docTagg(models.Model):

    docName = models.CharField( max_length=50)
    tags = TaggableManager()
    dateDoc = models.DateTimeField(auto_now=True)

    slug = AutoSlugField(populate_from='docName',slugify_function=my_slugify_function)
    class Meta:
        verbose_name = ('DocName')
        verbose_name_plural = ('DocNames')

    def __str__(self):
        return self.docName

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('ninth_app.urls.detail', args=[str(self.slug)])
        # return "modelo/%s/" %(self.slug) #reverse("doc_detail", kwargs={"pk": self.pk})


