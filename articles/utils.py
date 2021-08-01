def generate_upload_image_path(instance, filename):
    """
    This function generate upload path for image which consist of app name,
    model name and value field slug
    """
    return "images/{app}/{model}/{instance_slug}/{file}".format(
        app=instance._meta.app_label,
        model=instance._meta.model_name,
        instance_slug=instance.atricle.slug,
        file=filename
    )

def generate_upload_script_path(instance, filename):
    """
    This function generate upload path for script's file which consist of
    app name, model name and value field slug
    """
    return "scripts/{app}/{model}/{instance_slug}/{file}".format(
        app=instance._meta.app_label,
        model=instance._meta.model_name,
        instance_slug=instance.atricle.slug,
        file=filename
    )
