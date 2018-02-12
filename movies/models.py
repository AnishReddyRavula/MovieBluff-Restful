from django.db import models

# Create your models here.
class Movies(models.Model):

	movie_name = models.CharField(max_length=256)
	WORSE = 1
	BAD = 2
	AVERAGE = 3
	GOOD = 4
	EXCELLENT = 5
	RATING_CHOICES = (
		(WORSE, 'Worse'),
		(BAD, "Bad"),
		(AVERAGE, "Average"),
		(GOOD, "Good"),
		(EXCELLENT, "Excellent"),
		)
	movie_rating = models.IntegerField(
        choices=RATING_CHOICES,
        blank = True,
        null = True
    )
	watched = models.BooleanField(default=False)

	def __str__(self):
		return self.movie_name

	class Meta:
		verbose_name_plural = 'movies'
