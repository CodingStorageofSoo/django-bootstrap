from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.shortcuts import resolve_url


class User(AbstractUser):

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)

    # follower_set = models.ManyToManyField("self", blank=True)
    # following_set = models.ManyToManyField("self", blank=True)

    phone_number = models.CharField(max_length=13, blank=True,
                                    validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="please upload 48px * 48px size png/jpg.")
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)

    # def send_welcome_email(self):
    #     subject = render_to_string("accounts/welcome_email_subject.txt", {
    #         "user": self,
    #     })
    #     content = render_to_string("accounts/welcome_email_content.txt", {
    #         "user": self,
    #     })
    #     sender_email = settings.WELCOME_EMAIL_SENDER
    #     send_mail(subject, content, sender_email, [self.email], fail_silently=False)


