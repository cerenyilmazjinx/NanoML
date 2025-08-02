# test_nanoml.py
"""
Tests for NanoML module.
"""

import unittest
from nanoml import NanoML

class TestNanoML(unittest.TestCase):
    """Test cases for NanoML class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NanoML()
        self.assertIsInstance(instance, NanoML)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NanoML()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
