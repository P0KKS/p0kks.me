import unittest
import os

class TestSite(unittest.TestCase):
    def test_index_title(self):
        with open('docs/index.html', 'r') as f:
            content = f.read()
            self.assertIn('<title>P0KKS - Portfolio</title>', content)

    def test_about_name(self):
        with open('docs/about.md', 'r') as f:
            content = f.read()
            self.assertIn("<h1 class=\"title\">Hi I'm p0kks!</h1>", content)

if __name__ == '__main__':
    unittest.main()

