from django.core.exceptions import PermissionDenied


def user_is_teacher_or_current_student(function):
    def wrap(request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if request.user.is_teacher or int(pk) == request.user.pk or request.user.is_social:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def teacher_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_teacher:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def social_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_social:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

