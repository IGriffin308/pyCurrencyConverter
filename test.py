from unittest import TestCase
from app import app
from flask import session


class FlaskTests(TestCase):

    def setUp(self):
        """Setup testing environment."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_html(self):
        """Checks if homepage loads correctly"""

        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_1to1_conversion(self):
        """test if 1 USD converts to 1 USD"""

        with self.client:
            data = {'incurr': 'USD', 'outcurr': 'USD', 'inval': '1'}
            response = self.client.post('/result', data=data, follow_redirects=True)
            self.assertIn(b'Is Currently Equal to<br>\n    1.0 USD<br>', response.data)


# app:
# 1:1 +
# page loads +
# api connection 
# decimals
# currency symbols

# math:
# large nums
# small nums
# sig figs
