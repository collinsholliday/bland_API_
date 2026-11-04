"""Safe Bland AI client. Dry-run only; never places a call."""

import os


def prepare_call(phone_number: str, task: str) -> dict:
    """Prepare a call request without sending it."""
    if not phone_number or not task:
        raise ValueError("Phone number and task are required.")

    return {
        "phone_number": phone_number,
        "task": task,
        "dry_run": True,
        "live_call_sent": False,
    }


def send_call(*args, **kwargs):
    """Live calling is intentionally disabled in this setup."""
    raise PermissionError(
        "Live calling is disabled. Human review and verified consent "
        "must be implemented before any call can be placed."
    )
