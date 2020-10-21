from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RestAPI.settings")
MyAPP = Celery("RestAPI")

MyAPP.config_from_object("django.conf:settings", namespace="CELERY")
MyAPP.autodiscover_tasks()
