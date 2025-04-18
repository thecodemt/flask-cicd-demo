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
        # Check header
        self.assertIn(b'<header>', response.data)
        self.assertIn(b'Welcome to Flask Demo', response.data)
        # Check navigation
        self.assertIn(b'<nav>', response.data)
        self.assertIn(b'Home', response.data)
        self.assertIn(b'About', response.data)
        self.assertIn(b'Contact', response.data)
        # Check main content
        self.assertIn(b'<main>', response.data)
        self.assertIn(b'Flask Framework Introduction', response.data)
        # Check footer
        self.assertIn(b'<footer>', response.data)
        self.assertIn(b'&copy; 2024', response.data)

    def test_css_classes(self):
        # Test CSS classes
        response = self.app.get('/')
        self.assertIn(b'container', response.data)
        self.assertIn(b'card', response.data)
        self.assertIn(b'button', response.data)
        self.assertIn(b'feature-grid', response.data)

    def test_buttons(self):
        # Test button classes
        response = self.app.get('/')
        self.assertIn(b'button success', response.data)
        self.assertIn(b'button secondary', response.data)

    def test_icons(self):
        # Test Font Awesome icons
        response = self.app.get('/')
        self.assertIn(b'fa-home', response.data)
        self.assertIn(b'fa-info-circle', response.data)
        self.assertIn(b'fa-envelope', response.data)
        self.assertIn(b'fa-github', response.data)
        self.assertIn(b'fa-twitter', response.data)
        self.assertIn(b'fa-linkedin', response.data)

    def test_feature_cards(self):
        # Test feature cards content
        response = self.app.get('/')
        self.assertIn(b'Easy to Use', response.data)
        self.assertIn(b'Highly Extensible', response.data)
        self.assertIn(b'Rapid Development', response.data)
        self.assertIn(b'fa-code', response.data)
        self.assertIn(b'fa-puzzle-piece', response.data)
        self.assertIn(b'fa-rocket', response.data)

if __name__ == '__main__':
    unittest.main() 