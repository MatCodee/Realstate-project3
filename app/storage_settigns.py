from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media_cdn'
    default_acl = 'public-read'
    file_overwrite = False
    
    
# podemos especificar un modelo mas complejo para la subida de archivos a  la nube aqui
