import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_create_user():
    email = 'normal@user.com'
    User = get_user_model()
    user = User.objects.create_user(email=email, password='foo')
    assert user.email == email
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    try:
        assert user.username is None
    except AttributeError:
        pass
    with pytest.raises(TypeError):
        # User needs to provide email and password
        User.objects.create_user()
    with pytest.raises(TypeError):
        # Password must be provided
        User.objects.create_user(email="")
    with pytest.raises(ValueError):
        # Email cannot be empty
        User.objects.create_user(email="", password='foo')


@pytest.mark.django_db
def test_create_superuser():
    email = 'admin@user.com'
    User = get_user_model()
    admin = User.objects.create_superuser(email=email, password='foo')
    assert admin.email == email
    assert admin.is_active
    assert admin.is_staff
    assert admin.is_superuser
    try:
        assert admin.username is None
    except AttributeError:
        pass
    with pytest.raises(ValueError):
        User.objects.create_superuser(
            email=email, password='foo', is_superuser=False
        )
        