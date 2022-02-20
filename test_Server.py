import unittest
from Server import client_message

class TestServer(unittest.TestCase):
    def test_server_message(self):
        client_message = {
            'action': 'presence',
            "time": 1,
            "type": "status",
        }

        server_info = client_message(client_message)
        server_info = client_message['time'] = 1
        self.assertEqual(server_info, {
            'time': 1,
            'response':200,
            "alert": 'OK'
        }
        )

if __name__ == '__main__':
    unittest.main()