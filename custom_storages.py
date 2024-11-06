from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Custom storage class for handling static files on S3.

    Sets the storage location for static files using the configured
    `STATICFILES_LOCATION` in settings.
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Custom storage class for handling media files on S3.

    Sets the storage location for media files using the configured
    `MEDIAFILES_LOCATION` in settings.
    """
    location = settings.MEDIAFILES_LOCATION
