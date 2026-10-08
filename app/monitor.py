"""
Core DevOps System & Service Monitor.
Runs system checks and mock service status verification.
"""
import os
import sys
import json
import shutil
import time
from app.utils import get_timestamp, format_status, save_report

def load_config(config_path: str = "config/config.json") -> dict:
    """Loads configuration settings from a JSON file."""
    if not os.path.exists(config_path):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        alt_path = os.path.join(base_dir, config_path)
        if os.path.exists(alt_path):
            config_path = alt_path
        else:
            raise FileNotFoundError(f"Configuration file not found at: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def diagnose_disk_usage(used_percent: float, threshold_percent: float = 85.0) -> str:
    """Enhanced diagnostics: Evaluates disk usage percentage against threshold and returns HEALTHY or WARNING."""
    if used_percent >= threshold_percent:
        return "WARNING"
    return "HEALTHY"

def check_disk_space(path: str = ".", threshold_percent: float = 85.0) -> dict:
    """Checks disk space usage for the current volume."""
    total, used, free = shutil.disk_usage(path)
    used_percent = round((used / total) * 100, 2)
    status = diagnose_disk_usage(used_percent, threshold_percent)
    
    return {
        "metric": "Disk Space",
        "total_gb": round(total / (1024**3), 2),
        "used_gb": round(used / (1024**3), 2),
        "free_gb": round(free / (1024**3), 2),
        "usage_percent": used_percent,
        "threshold_percent": threshold_percent,
        "status": status
    }

def check_services(endpoints: list) -> list:
    """Simulates/verifies configured microservices health."""
    results = []
    for endpoint in endpoints:
        results.append({
            "name": endpoint.get("name"),
            "url": endpoint.get("url"),
            "expected_status": endpoint.get("expected_status", 200),
            "actual_status": 200,
            "latency_ms": 42.5,
            "status": "HEALTHY"
        })
    return results

def run_health_check(config_path: str = "config/config.json", export_report: bool = False) -> dict:
    """Executes all health checks and prints summary report."""
    print("=" * 60)
    print("          DEVOPS SYSTEM HEALTH MONITOR          ")
    print("=" * 60)
    print(f"Execution Timestamp : {get_timestamp()}")

    config = load_config(config_path)
    print(f"Service Name        : {config.get('service_name')}")
    print(f"Environment         : {config.get('environment')}")
    print("-" * 60)

    # 1. System checks
    disk_check = check_disk_space(".", config.get("thresholds", {}).get("disk_usage_percent", 85.0))
    print(f"Disk Status         : {format_status(disk_check['status'])}")
    print(f"Disk Usage          : {disk_check['used_gb']} GB / {disk_check['total_gb']} GB ({disk_check['usage_percent']}%)")
    print("-" * 60)

    # 2. Endpoint checks
    print("Microservices Health Checks:")
    service_results = check_services(config.get("endpoints", []))
    for res in service_results:
        print(f"  - {res['name']:<22} {format_status(res['status'])} ({res['latency_ms']} ms)")

    report = {
        "timestamp": get_timestamp(),
        "service_name": config.get("service_name"),
        "version": config.get("version"),
        "environment": config.get("environment"),
        "disk_check": disk_check,
        "services": service_results
    }

    if export_report:
        report_path = save_report(report)
        print("-" * 60)
        print(f"Report exported to : {report_path}")

    print("=" * 60)
    print("Health check completed successfully.")
    return report

if __name__ == "__main__":
    export = "--export" in sys.argv
    run_health_check(export_report=export)
