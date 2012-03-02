from django.db import models

class Zombie(models.Model):
	name_of_zombie = models.CharField(max_length=35)
	cemetery_of_zombie = models.CharField(max_length=35)


	def __unicode__(self):
		return 'Zombie ERWIN: %s - %s' % (self.pk, self.name_of_zombie,)


class Tweet(models.Model):
	state = models.CharField(max_length=100)
	tweet_zombie = models.ForeignKey('Zombie', related_name='tweet')
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return 'Tweet_of_zombie: %s - %s' % (self.pk, self.state,)

