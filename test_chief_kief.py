#!/usr/bin/env python3
"""
Tests for Chief-kief CLI tool
"""

import unittest
from chief_kief import get_random_quote, QUOTES


class TestChiefKief(unittest.TestCase):
    """Test cases for Chief-kief functionality"""
    
    def test_get_random_quote_returns_valid_quote(self):
        """Test that get_random_quote returns a quote from the QUOTES list"""
        quote = get_random_quote()
        self.assertIn(quote, QUOTES)
    
    def test_quotes_list_not_empty(self):
        """Test that QUOTES list contains at least one quote"""
        self.assertGreater(len(QUOTES), 0)
    
    def test_all_quotes_are_strings(self):
        """Test that all quotes in QUOTES are strings"""
        for quote in QUOTES:
            self.assertIsInstance(quote, str)
    
    def test_get_random_quote_returns_string(self):
        """Test that get_random_quote returns a string"""
        quote = get_random_quote()
        self.assertIsInstance(quote, str)
    
    def test_multiple_calls_return_valid_quotes(self):
        """Test that multiple calls to get_random_quote return valid quotes"""
        for _ in range(10):
            quote = get_random_quote()
            self.assertIn(quote, QUOTES)


if __name__ == "__main__":
    unittest.main()
