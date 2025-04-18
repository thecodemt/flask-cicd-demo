import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Create test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test home page route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_about_page(self):
        # Test about page route
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_nonexistent_page(self):
        # Test non-existent page
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_static_files(self):
        # Test static files
        response = self.app.get('/static/css/style.css')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/css; charset=utf-8')

    def test_response_headers(self):
        # Test response headers
        response = self.app.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')
        self.assertTrue('Content-Length' in response.headers)

    def test_template_content(self):
        # Test template content
        response = self.app.get('/')
        # Check navigation
        self.assertIn(b'<nav>', response.data)
        self.assertIn(b'Home', response.data)
        self.assertIn(b'About', response.data)
        # Check footer
        self.assertIn(b'footer', response.data)
        self.assertIn(b'&copy; 2024', response.data)

    def test_about_page_content(self):
        # Test about page specific content
        response = self.app.get('/about')
        self.assertIn(b'Python 3.9', response.data)
        self.assertIn(b'Flask 2.3.3', response.data)
        self.assertIn(b'HTML5 & CSS3', response.data)

    def test_home_page_features(self):
        # Test home page features
        response = self.app.get('/')
        self.assertIn(b'Easy to Use', response.data)
        self.assertIn(b'Highly Extensible', response.data)
        self.assertIn(b'Rapid Development', response.data)

    def test_social_links(self):
        # Test social media links
        response = self.app.get('/')
        self.assertIn(b'social-links', response.data)
        self.assertIn(b'fab fa-github', response.data)
        self.assertIn(b'fab fa-twitter', response.data)
        self.assertIn(b'fab fa-linkedin', response.data)

    def test_css_classes(self):
        # Test CSS classes
        response = self.app.get('/')
        self.assertIn(b'card', response.data)
        self.assertIn(b'feature-grid', response.data)
        self.assertIn(b'feature-item', response.data)

if __name__ == '__main__':
    unittest.main() 