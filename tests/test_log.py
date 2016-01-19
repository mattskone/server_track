import time
import unittest

import log


class LogTest(unittest.TestCase):

    def test_get_average_or_none(self):
        values = [0., 1., 2., 3.]
        self.assertEqual(log._get_average_or_none(values), 1.5)

        values = []
        self.assertEqual(log._get_average_or_none(values), None)

    def test_get_averages(self):
        now = time.time()
        sample_data = [
                {'ts': now - 50, 'cpu': 4.0, 'ram': 5.0},
                {'ts': now - 15, 'cpu': 3.0, 'ram': 4.0},
                {'ts': now - 5, 'cpu': 2.0, 'ram': 3.0},
                {'ts': now, 'cpu': 1.0, 'ram': 2.0}
        ]

        expected = {'cpu': [1.5, 3.0, None], 'ram': [2.5, 4.0, None]}
        actual = log._get_averages(sample_data,
                                  interval_ticks=10,
                                  num_intervals=3)
        self.assertEqual(expected, actual)

