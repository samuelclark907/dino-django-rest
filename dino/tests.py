from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Dino

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_dino = Dino.objects.create(
            creator = testuser1,
            name = 'Green Eggs and Ham',
            description = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_dino.save()

    def test_blog_content(self):
        dino = Dino.objects.get(id=1)
        actual_creator = str(dino.creator)
        actual_name = str(dino.name)
        actual_description = str(dino.description)
        self.assertEqual(actual_creator, 'testuser1')
        self.assertEqual(actual_name, 'Green Eggs and Ham')
        self.assertEqual(actual_description, 'I do not like green eggs and ham, Sam I  am.')
