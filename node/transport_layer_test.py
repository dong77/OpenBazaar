import unittest

from p2p import TransportLayer

# Test the callback features of the TransportLayer class
class TestTransportLayerCallbacks(unittest.TestCase):
    one_called = False
    two_called = False
    three_called = False

    def _callback_one(self, arg):
        self.assertFalse(self.one_called)
        self.one_called = True

    def _callback_two(self, arg):
        self.assertFalse(self.two_called)
        self.two_called = True

    def _callback_three(self, arg):
        self.assertFalse(self.three_called)
        self.three_called = True

    def setUp(self):
        self.tl = TransportLayer(1, 'localhost', None, 1)
        self.tl.add_callback('section_one', self._callback_one)
        self.tl.add_callback('section_one', self._callback_two)
        self.tl.add_callback('all', self._callback_three)

    def _assert_called(self, one, two, three):
        self.assertEqual(self.one_called, one)
        self.assertEqual(self.two_called, two)
        self.assertEqual(self.three_called, three)

    def test_fixture(self):
        self._assert_called(False, False, False)

    def test_callbacks(self):
        self.tl.trigger_callbacks('section_one', None)
        self._assert_called(True, True, True)

    def test_all_callback(self):
        self.tl.trigger_callbacks('section_with_no_register', None)
        self._assert_called(False, False, True)

    def test_explicit_all_section(self):
        self.tl.trigger_callbacks('all', None)
        self._assert_called(False, False, True)
