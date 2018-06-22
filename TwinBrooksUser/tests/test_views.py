import pytest
from ..views import login_redirect, edit_profile_information, edit_profile_photo
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.http import HttpResponse
from mixer.backend.django import mixer
from django.contrib.messages.storage.fallback import FallbackStorage
pytestmark = pytest.mark.django_db


class TestLoginRedirect():
    def test_anonymous(self):
        url = reverse('login_redirect')
        req = RequestFactory().get(url)
        req.user = AnonymousUser()
        resp = login_redirect(req)
        assert 'login' in resp.url, 'Should redirect to login'

    def test_logged_in_user(self):
        url = reverse('login_redirect')
        user = mixer.blend('TwinBrooksUser.User', is_superuser=True)
        req = RequestFactory().get(url)
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = login_redirect(req)
        assert resp.status_code == 302, 'Should be redirect to home page'


class TestEditProfileInformation():
    def test_anonymous(self):
        url = reverse('TwinBrooksUser:edit_profile_information')
        req = RequestFactory().get(url)
        req.user = AnonymousUser()
        resp = login_redirect(req)
        assert 'login' in resp.url, 'Should redirect to login'

    def test_edit_profile_information(self):
        url = reverse('TwinBrooksUser:edit_profile_information')
        user = mixer.blend('TwinBrooksUser.User', is_superuser=True)
        req = RequestFactory().get(url)
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = edit_profile_information(req)
        assert resp.status_code == 200, 'Should be directed to page'

    def test_edit_profile_information_post(self):
        url = reverse('TwinBrooksUser:edit_profile_information')
        user = mixer.blend('TwinBrooksUser.User', is_superuser=True)
        data = {
            'first_name': 'Zachary',
            'last_name': 'Bedrosian',
            'email': 'zacharybedrosian@gmail.com'  # Need email or form would raise null error
        }
        req = RequestFactory().post(url, data=data)
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = edit_profile_information(req)
        assert resp.status_code == 302, 'Should redirect to success view'
        user.refresh_from_db()
        assert user.first_name == 'Zachary', 'Should update the user'


class TestEditProfilePicture():
    def test_anonymous(self):
        url = reverse('TwinBrooksUser:edit_profile_photo')
        req = RequestFactory().get(url)
        req.user = AnonymousUser()
        resp = login_redirect(req)
        assert 'login' in resp.url, 'Should redirect to login'

    def test_edit_profile_photo(self):
        url = reverse('TwinBrooksUser:edit_profile_photo')
        user = mixer.blend('TwinBrooksUser.User', is_superuser=True)
        req = RequestFactory().get(url)
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = HttpResponse(edit_profile_photo(req))
        assert resp.status_code == 200, 'Should be directed to page'

    def test_edit_profile_photo_post_and_get_profile_image(self):
        url = reverse('TwinBrooksUser:edit_profile_photo')
        user = mixer.blend('TwinBrooksUser.User', is_superuser=True)
        img = './TwinBrooksUser/tests/test.png'
        with open(img, 'rb') as infile:
            req = RequestFactory().post(
                url,
                {'profile_image': infile}
            )
        req.user = user
        setattr(req, 'session', 'session')
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)
        resp = edit_profile_photo(req)
        assert resp.status_code == 302, 'Should redirect to success view'
        user.refresh_from_db()
        assert len(user.profile_image.name) == 42, 'Should update the user image, count len of file name for test.'

        # Assert that the user get profile image call works as well with the uploaded image
        # I cut the image url at .com to ensure any AWS domain will work.
        # I also cut the signature as well to ensure compariablility
        img_url = user.get_profile_image()
        sig_place = img_url.index('?')
        com_place = img_url.index('.com')
        img_url = img_url[com_place + 4:sig_place]
        assert len(img_url) == 82, 'Should output user profile url with out aws signature and aws domain'
