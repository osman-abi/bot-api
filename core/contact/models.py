

from django.db import models

# Create your models here.

class Contacts(models.Model):
    avatar                = models.ImageField(upload_to='profile_images/')
    sender_id             = models.CharField(max_length=300, blank=True, null=True)
    name                  = models.CharField(max_length=250, blank=True, null=True)
    surname               = models.CharField(max_length=250, blank=True, null=True)
    gender                = models.CharField(max_length=250, blank=True, null=True)
    latest_chosen_service = models.CharField(max_length=250, blank=True, null=True)
    # last_contact_time     = models.DateTimeField()
    # subscription          = models.DateTimeField()
    # source_id             = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class CommentAuthors(models.Model):
    user_id = models.CharField(max_length=300, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.user_id


class Comments(models.Model):
    user_id    = models.ForeignKey(CommentAuthors, on_delete=models.CASCADE, blank=True, null=True)
    post_id    = models.CharField(max_length=500, blank=True, null=True)
    comment_id = models.CharField(max_length=250, blank=True, null=True)
    user_name  = models.CharField(max_length=300, blank=True, null=True)
    comment    = models.CharField(max_length=1010, blank=True, null=True)
    is_sent    = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"from {self.user_id} comment: {self.comment}"


class ReplyMessage(models.Model):
    message = models.TextField()

    def __str__(self) -> str:
        return self.message