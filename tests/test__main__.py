import unittest
from src import connections

class testBossSpy(unittest):
    def test_getEmails(self):
        self.assertEqual(connections.get_unread_count(), 5, "Should be 5")

