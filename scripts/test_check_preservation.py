#!/usr/bin/env python3
"""Tests for check_preservation.py."""

from __future__ import annotations

import unittest

from check_preservation import compare, extract_tokens


class PreservationTests(unittest.TestCase):
    def test_identical_text_passes(self) -> None:
        text = "In 128 patients, 37 events occurred (HR 1.42, 95% CI 1.08-1.86) [1]."
        self.assertEqual(compare(text, text)["status"], "pass")

    def test_missing_number_is_flagged(self) -> None:
        result = compare("The cohort included 128 patients.", "The cohort included patients.")
        self.assertEqual(result["status"], "review-required")
        self.assertEqual(result["differences"]["numbers"]["missing"], {"128": 1})

    def test_added_number_is_flagged(self) -> None:
        result = compare("AUC was 0.81.", "AUC was 0.91.")
        self.assertEqual(result["differences"]["numbers"]["missing"], {"0.81": 1})
        self.assertEqual(result["differences"]["numbers"]["added"], {"0.91": 1})

    def test_citation_removal_is_flagged(self) -> None:
        result = compare("The association was consistent with prior work [3].", "The association was consistent with prior work.")
        self.assertEqual(result["differences"]["citations"]["missing"], {"[3]": 1})

    def test_numbers_inside_citations_are_not_double_counted(self) -> None:
        tokens = extract_tokens("Prior work reached the same conclusion [2024].")
        self.assertEqual(tokens["numbers"], {})
        self.assertEqual(tokens["citations"], {"[2024]": 1})

    def test_author_year_citation_is_preserved(self) -> None:
        result = compare("Prior work agrees (Smith et al., 2024).", "Prior work agrees.")
        self.assertEqual(result["differences"]["citations"]["missing"], {"(Smith et al., 2024)": 1})


if __name__ == "__main__":
    unittest.main()
