import unittest
from unittest.mock import patch
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    @patch('monitor.print_alert')
    def test_temperature_out_of_range(self, mock_alert):
        self.assertFalse(vitals_ok(104, 70, 98))
        mock_alert.assert_called_with("Temperature critical!")

    @patch('monitor.print_alert')
    def test_pulse_out_of_range(self, mock_alert):
        self.assertFalse(vitals_ok(98.6, 120, 98))
        mock_alert.assert_called_with("Pulse Rate is out of range!")

    @patch('monitor.print_alert')
    def test_spo2_out_of_range(self, mock_alert):
        self.assertFalse(vitals_ok(98.6, 70, 88))
        mock_alert.assert_called_with("Oxygen Saturation out of range!")

    def test_all_vitals_in_range(self):
        self.assertTrue(vitals_ok(98.6, 70, 98))

    def test_temperature_edge_cases(self):
        self.assertTrue(vitals_ok(95, 70, 98))
        self.assertTrue(vitals_ok(102, 70, 98))
        self.assertFalse(vitals_ok(94.9, 70, 98))
        self.assertFalse(vitals_ok(102.1, 70, 98))

    def test_pulse_edge_cases(self):
        self.assertTrue(vitals_ok(98.6, 60, 98))
        self.assertTrue(vitals_ok(98.6, 100, 98))
        self.assertFalse(vitals_ok(98.6, 59, 98))
        self.assertFalse(vitals_ok(98.6, 101, 98))

    def test_spo2_edge_cases(self):
        self.assertTrue(vitals_ok(98.6, 70, 90))
        self.assertFalse(vitals_ok(98.6, 70, 89))


if __name__ == '__main__':
    unittest.main()
