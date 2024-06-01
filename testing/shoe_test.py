# testing/shoe_test.py
import pytest
from lib.shoe import Shoe

def test_shoe_creation():
    shoe = Shoe("Nike", 42)
    assert shoe.brand == "Nike"
    assert shoe.size == 42

def test_shoe_size_positive_integer():
    shoe = Shoe("Adidas", 38)
    with pytest.raises(ValueError):
        shoe.size = -1
    with pytest.raises(ValueError):
        shoe.size = "large"

def test_shoe_compare_size():
    shoe1 = Shoe("Puma", 40)
    shoe2 = Shoe("Reebok", 42)
    assert shoe1.compare_size(shoe2) == "This shoe is smaller."
    assert shoe2.compare_size(shoe1) == "This shoe is larger."
    shoe3 = Shoe("Asics", 40)
    assert shoe1.compare_size(shoe3) == "Sizes are the same."
