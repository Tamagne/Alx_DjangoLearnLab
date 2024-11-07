# relationship_app/decorators.py

from django.contrib.auth.decorators import user_passes_test

def role_required(role):
    def decorator(view_func):
        return user_passes_test(lambda u: u.userprofile.role == role)(view_func)
    return decorator
