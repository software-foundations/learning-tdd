from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

	def test_create_blog(self):

		b = Blog("Test Tittle", "Test Author")

		self.assertEqual("Test Tittle", b.title)

		self.assertEqual("Test Author", b.author)

		self.assertListEqual([], b.posts)		
