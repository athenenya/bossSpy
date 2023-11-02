import unittest
from src import connections

class testBossSpy(unittest.TestCase):
    def test_getEmails(self):
        self.assertEqual(connections.get_unread_count(), 5)


if __name__ == '__main__':
    unittest.main()

