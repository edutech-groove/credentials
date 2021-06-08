
from social_core.exceptions import AuthAlreadyAssociated

def social_user(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            msg = 'This account is already in use.'
            backend.strategy.storage.user.changed(social.user)
            #raise AuthAlreadyAssociated(backend, msg)
        elif not user:
            user = social.user

    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': social is None}