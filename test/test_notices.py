"""Tests for Polyglot notice message helpers."""

from utils.notices import connecting_notice_message, success_notice_message


def test_success_notice_singular():
    msg = success_notice_message("unifi.local", 1, 1)
    assert msg == (
        "Connected to UniFi Protect at unifi.local. "
        "Discovered 1 camera and 1 sensor."
    )


def test_success_notice_plural():
    msg = success_notice_message("192.168.1.10", 3, 2)
    assert "3 cameras" in msg
    assert "2 sensors" in msg


def test_connecting_notice():
    msg = connecting_notice_message("unifi.local", 15)
    assert msg == (
        "Connecting to UniFi Protect at unifi.local (retry in 15s)..."
    )
