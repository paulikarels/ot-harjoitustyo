import unittest
from unittest.mock import Mock
from services.appservice import AppService

class TestAppService(unittest.TestCase):
    def setUp(self):
        self.root = Mock()
        self.app_service = AppService(self.root)

    def test_start(self):
        self.app_service._ui.start = Mock()

        self.app_service.start()

        self.assertTrue(self.app_service._ui.start.called)

if __name__ == '__main__':
    unittest.main()