# test_cresttorch.py
"""
Tests for CrestTorch module.
"""

import unittest
from cresttorch import CrestTorch

class TestCrestTorch(unittest.TestCase):
    """Test cases for CrestTorch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrestTorch()
        self.assertIsInstance(instance, CrestTorch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrestTorch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
