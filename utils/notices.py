"""Polyglot notice message helpers."""


def success_notice_message(
    host: str, camera_count: int, sensor_count: int
) -> str:
    """Build a temporary success notice after connect and discovery."""
    cam_plural = "s" if camera_count != 1 else ""
    sen_plural = "s" if sensor_count != 1 else ""
    return (
        f"Connected to UniFi Protect at {host}. "
        f"Discovered {camera_count} camera{cam_plural} "
        f"and {sensor_count} sensor{sen_plural}."
    )


def connecting_notice_message(host: str, retry_seconds: int) -> str:
    """Build a temporary notice while retrying connection."""
    return (
        f"Connecting to UniFi Protect at {host} "
        f"(retry in {retry_seconds}s)..."
    )
