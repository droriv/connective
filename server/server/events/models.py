from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.organizations.models import SchoolActivityGroup
from server.users.models import Consumer


class Event(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    consumers = models.ManyToManyField(
        Consumer,
        blank=True,
    )
    school_group = models.ForeignKey(
        SchoolActivityGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    locations_name = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    has_summary = models.BooleanField(default=False)
    summary_general_notes = models.CharField(
        max_length=400,
        null=True,
        blank=True,
    )
    summary_general_rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        null=True,
        blank=True,
    )
    summary_children_behavior = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        null=True,
        blank=True,
    )

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError(
                {"end_time": _("end time must occur after start time")}
            )

    def __str__(self):
        return f"{self.school_group} : {self.start_time}"
