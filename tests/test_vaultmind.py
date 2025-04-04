# Unit tests for VaultMind
import unittest
from src.vaultmind.storage import store_thought, get_all_thoughts

class TestVaultMind(unittest.TestCase):
    def test_store_and_retrieve(self):
        store_thought("Test thought", 0.0, "test")
        thoughts = get_all_thoughts()
        self.assertTrue(any("Test thought" in t for t in thoughts))

if __name__ == "__main__":
    unittest.main()