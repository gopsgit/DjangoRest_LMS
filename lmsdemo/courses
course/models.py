from django.db import models
import uuid
# Create your models here.
import uuid
# category model
class Category(models.Model):
	id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
	slug = models.slugFild()
	tittle = models.CharField(max_length=20,null=False)

	def __str__(self):

		return self.id


#  
class  