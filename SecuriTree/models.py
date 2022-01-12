
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class Area(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=200)
    parent_area = models.ForeignKey(
        "self", null=True, blank=True, related_name="areas", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def doors (self):
        return Door.objects.filter(parent_area = self).order_by('id')

    def rules (self):
        Door.objects.filter(parent_area = self).order_by('id')
        return DoorAccessRule.objects.filter(door = 'EA0F4EAA-5666-4439-9E5D-6A4FFEB578DF')

    class Meta:
        ordering = ['-id']

Area.objects.all().order_by('-id')

class AccessRule(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

AccessRule.objects.all().order_by('-id')

class Door(models.Model):

    DOOR_STATUS = (
        ('closed', 'Locked'),
        ('open', 'Unlocked'),
    )

    id = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=200)
    parent_area = models.ForeignKey(
        "Area", related_name="area", on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=10, default='closed', choices=DOOR_STATUS
    )

    accessrules = models.ManyToManyField(
        AccessRule,
        blank=True,
        related_name="doors",
        through="DoorAccessRule",
        through_fields=("accessrule", "door"),
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

Door.objects.all().order_by('-id')

class DoorAccessRule(models.Model):
    door = models.ForeignKey(
        "AccessRule", related_name="dooraccessrule", on_delete=models.CASCADE
    )
    accessrule = models.ForeignKey(
        Door, related_name="dooraccessrule", on_delete=models.CASCADE
    )


class User(AbstractUser):
    username = models.CharField(max_length=256,primary_key=True)
    first_name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)

    accessrules = models.ManyToManyField(
        AccessRule,
        blank=True,
        related_name="users",
        through="UserAccessRule",
        through_fields=("accessrule", "user"),
    )

    def __str__(self):
        return self.surname


class UserAccessRule(models.Model):
    user = models.ForeignKey(
        "AccessRule", related_name="useraccessrule", on_delete=models.CASCADE
    )
    accessrule = models.ForeignKey(
        User, related_name="useraccessrule", on_delete=models.CASCADE
    )

