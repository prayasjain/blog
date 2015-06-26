from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    slug = models.SlugField(unique=True,default='')
    def save(self, *args, **kwargs):
                self.slug = slugify(self.user.username)
                super(UserProfile, self).save(*args, **kwargs)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class blogtext(models.Model):


    username= models.ForeignKey(UserProfile)
    text=models.CharField(max_length=256,blank=False)
    def __unicode__(self):
        return self.text
