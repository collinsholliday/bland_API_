import unittest

from consent_manager import ConsentRecord, consent_is_valid


class ConsentManagerTests(unittest.TestCase):

    def test_missing_record_is_rejected(self):
        self.assertFalse(consent_is_valid(None))

    def test_valid_documented_consent_is_accepted(self):
        record = ConsentRecord(
            person_id="seller-001",
            consent_scope="AI voice call",
            evidence="Permission documented",
            verified_by_human=True,
        )
        self.assertTrue(consent_is_valid(record))

    def test_wrong_scope_is_rejected(self):
        record = ConsentRecord(
            person_id="seller-001",
            consent_scope="text message",
            evidence="Permission documented",
            verified_by_human=True,
        )
        self.assertFalse(consent_is_valid(record))

    def test_unverified_consent_is_rejected(self):
        record = ConsentRecord(
            person_id="seller-001",
            consent_scope="AI voice call",
            evidence="Permission documented",
            verified_by_human=False,
        )
        self.assertFalse(consent_is_valid(record))


if __name__ == "__main__":
    unittest.main()
