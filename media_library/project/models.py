from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True, null=False)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self

class Topics(models.Model):
    topic = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self

class MediaItem(models.Model):
    type = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=17)
    author = models.CharField(max_length=100)
    image_file = models.CharField(max_length=100)
    topic = models.ForeignKey(Topics, related_name="topic_fk")
    subtopic = models.ManyToManyField(Topics, related_name="subtopic_fk")

    def save(self, *args, **kwargs):
        super(MediaItem, self).save(*args, **kwargs)

    def __str__(self):
        return self

class MediaHistory(models.Model):
    date_out = models.DateField(null=False)
    date_due = models.DateField()
    date_returned = models.DateField(null=True)
    media_item = models.ForeignKey(MediaItem)
    borrower = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        from datetime import timedelta, datetime
        delta = timedelta(days=14)

        if not self.id:
            self.date_due = datetime.now() + delta
            super(MediaHistory, self).save(*args, **kwargs)

    def __str__(self):
        return self