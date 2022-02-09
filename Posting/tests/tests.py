from django.test import TestCase
from Posting.models import Post
from UserAuth.models import User
# Create your tests here.
class PostTestMehods(TestCase):
    def setUp(self):
        Post.objects.create(Post_Name="New Post for Testing4",Description="New Description")
        Post.objects.create(Post_Name="New Post for Testing5",Description="New Description")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Post.objects.get(Post_Name="New Post for Testing4")
        cat = Post.objects.get(Post_Name="New Post for Testing5")
        self.assertEqual(lion.Post_Name, 'New Post for Testing4')
        self.assertEqual(cat.Post_Name, 'New Post for Testing5')

    def description_check(self):
        lion = Post.objects.get(Post_Name="New Post for Testing4")
        cat = Post.objects.get(Post_Name="New Post for Testing5")
        self.assertEqual(lion.Description, 'New Description')
        self.assertEqual(cat.Description, 'New Description')
