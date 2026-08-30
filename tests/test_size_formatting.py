import unittest

from linuxmonitor.linuxmonitor import LinuxMonitor


class SizeFormattingTests(unittest.TestCase):
    def test_formats_large_values_in_tb(self):
        self.assertEqual(LinuxMonitor._format_size_in_gb_or_tb(1024), "1.02TB")
        self.assertEqual(LinuxMonitor._format_size_in_gb_or_tb(1500), "1.50TB")

    def test_keeps_medium_values_in_gb(self):
        self.assertEqual(LinuxMonitor._format_size_in_gb_or_tb(512), "512.00GB")
        self.assertEqual(LinuxMonitor._format_size_in_gb_or_tb(23.5), "23.50GB")


if __name__ == "__main__":
    unittest.main()
