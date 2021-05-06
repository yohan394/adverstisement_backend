from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import index


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_(self):
        pass




