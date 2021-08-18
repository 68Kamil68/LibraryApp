from django.contrib.auth import get_user_model

import pytest

User = get_user_model()


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("admin", "admin@admin.com", "adminpassw123")
    assert User.objects.count() == 1
