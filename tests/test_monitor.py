"""
Automated unit tests for DevOps Health Monitor.
Runs using Python standard library unittest.
"""
import unittest
import os
from app.monitor import load_config, check_disk_space, check_services, diagnose_disk_usage
from app.utils import format_status, get_timestamp

class TestDevOpsMonitor(unittest.TestCase):

    def test_config_loading(self):
        """Test configuration file is loaded properly."""
        config = load_config("config/config.json")
        self.assertIn("service_name", config)
        self.assertIn("endpoints", config)
        self.assertIsInstance(config["endpoints"], list)

    def test_disk_space_check(self):
        """Test disk usage calculation returns valid keys and values."""
        result = check_disk_space(".", threshold_percent=99.0)
        self.assertIn("metric", result)
        self.assertIn("usage_percent", result)
        self.assertIn("status", result)
        self.assertIn(result["status"], ["HEALTHY", "WARNING", "CRITICAL"])

    def test_service_checks(self):
        """Test endpoint evaluation."""
        endpoints = [{"name": "Mock Test Service", "url": "https://example.com", "expected_status": 200}]
        results = check_services(endpoints)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["status"], "HEALTHY")

    def test_status_formatting(self):
        """Test string formatting helper."""
        self.assertIn("PASS", format_status("HEALTHY"))
        self.assertIn("WARN", format_status("WARNING"))
        self.assertIn("FAIL", format_status("CRITICAL"))

    def test_timestamp_format(self):
        """Test timestamp formatting validity."""
        ts = get_timestamp()
        self.assertTrue(ts.endswith("Z"))

    def test_diagnose_disk_usage(self):
        """Test enhanced diagnostics for disk usage threshold evaluation."""
        self.assertEqual(diagnose_disk_usage(50.0, threshold_percent=85.0), "HEALTHY")
        self.assertEqual(diagnose_disk_usage(85.0, threshold_percent=85.0), "WARNING")
        self.assertEqual(diagnose_disk_usage(92.5, threshold_percent=85.0), "WARNING")

if __name__ == "__main__":
    unittest.main()
