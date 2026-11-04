"""Default-deny safety checks for Deal 001 voice calls."""

import os


def authorize_call(*, approved: bool, consent_verified: bool, consent_scope: str) -> None:
    """Block calls unless every safety condition is satisfied."""

    if os.getenv("ENABLE_LIVE_CALLS", "false").lower() != "true":
        raise PermissionError("Live calls are disabled.")

    if not approved:
        raise PermissionError("A human must approve this specific call.")

    if not consent_verified:
        raise PermissionError("Documented consent has not been verified.")

    if consent_scope.strip().lower() != "ai voice call":
        raise PermissionError("Consent must explicitly cover an AI voice call.")
