import unittest
from Client import client_message

class TestClient(unittest.TestCase):
    def test_create_message_presence(self):
        message = client_message()
        message['time'] = 1
        self.assertEqual(message, {
            "action": "presence",
            "time": 1,
            "type": "status"
        }
        )

if __name__ == '__main__':
    unittest.main()