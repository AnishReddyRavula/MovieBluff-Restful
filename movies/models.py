from django.db import models

class Movies(models.Model):
	"""
	This is the speacial object  that saves in database
	here each model field is self explainatory 
	for rating, mapping for each rating is done to its string
	watched on updates the watched date of the movie if provided otherwise stamps with current date
	"""

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
	watched_on = models.DateField(
		auto_now_add=True,
		blank = True,
		null = True
	)

	def __str__(self):
		return self.movie_name

	class Meta:
		verbose_name_plural = 'movies'
