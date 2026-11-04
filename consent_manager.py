"""Deal 001 consent records. Missing or incomplete consent is never approved."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ConsentRecord:
    person_id: str
    consent_scope: str
    evidence: str
    verified_by_human: bool


def consent_is_valid(record: ConsentRecord | None) -> bool:
    """Return True only when documented AI voice-call consent is verified."""

    if record is None:
        return False

    return all((
        bool(record.person_id.strip()),
        record.consent_scope.strip().lower() == "ai voice call",
        bool(record.evidence.strip()),
        record.verified_by_human is True,
    ))
