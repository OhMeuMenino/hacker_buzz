import settings

def save_image(request):
    """
    Save image to filesystem
    """
    upload = request.files.get('image')
    if upload is None:
        raise Exception('missing image file')
    upload.save(settings.UPLOADS, True)
    return upload
