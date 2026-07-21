import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report() -> dict:
    """Read report.json and return it as a Python dict."""
    assert REPORT_PATH.exists(), "no report.json found"
    assert REPORT_PATH.stat().st_size > 0, "report.json is empty"
    with REPORT_PATH.open(encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json must be a JSON object"
    return data


def test_total_requests():
    """How many log lines / requests were there?"""
    report = _load_report()
    assert "total_requests" in report, "missing key: total_requests"
    assert report["total_requests"] == 6


def test_unique_ips():
    """How many distinct client IPs?"""
    report = _load_report()
    assert "unique_ips" in report, "missing key: unique_ips"
    assert report["unique_ips"] == 3


def test_top_path():
    """Which path was requested most often?"""
    report = _load_report()
    assert "top_path" in report, "missing key: top_path"
    assert report["top_path"] == "/index.html"


def test_200_code_count():
    """How many responses had HTTP status 200?"""
    report = _load_report()
    assert "200_code_times" in report, "missing key: 200_code_times"
    assert report["200_code_times"] == 5
