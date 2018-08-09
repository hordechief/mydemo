
# from comments.models import MPTTComment
# from comments.forms import MPTTCommentForm

# def get_model():
#     return MPTTComment

# def get_form():
#     return MPTTCommentForm


from django.utils.module_loading import import_string



def get_model():
    return import_string('comments.models.MPTTComment')
    try:
        from comments.models import MPTTComment
        return MPTTComment
    except:
        import comments
        return comments.models.MPTTComment

def get_form():
    return import_string('comments.forms.MPTTCommentForm')
    try:
        from comments.forms import MPTTCommentForm
        return MPTTCommentForm
    except:
        # python manage.py runserver
        import comments
        return comments.forms.MPTTCommentForm
    