# coding: utf-8
#!/usr/bin/env python
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals

signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')

def create_admin(app, created_models, verbosity, **kwargs):
  if not settings.DEBUG:
    return
  try:
    auth_models.User.objects.get(username='admin')
  except auth_models.User.DoesNotExist:
    assert auth_models.User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
  else:
    print 'Admin, já existe.'

signals.post_syncdb.connect(create_admin,
    sender=auth_models, dispatch_uid='common.models.create_admin')