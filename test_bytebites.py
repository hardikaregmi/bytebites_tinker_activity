import pytest
from models import FoodItem, Menu, Transaction, Customer

def test_calculate_total_with_multiple_items():
    """Verify that adding multiple items calculates the correct total cost."""
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.25, "Drinks", 4.2)
    
    order = Transaction()
    order.addItem(burger)
    order.addItem(soda)
    
    assert order.computeTotalCost() == 11.24

def test_order_total_is_zero_when_empty():
    """Verify that a brand new or empty transaction returns a total cost of 0.0."""
    order = Transaction()
    assert order.computeTotalCost() == 0.0

def test_filter_menu_items_by_category():
    """Verify that filtering by a specific category only returns items matching it."""
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.25, "Drinks", 4.2)
    shake = FoodItem("Vanilla Shake", 4.50, "Drinks", 4.7)
    
    menu = Menu([burger, soda, shake])
    drinks = menu.filterByCategory("Drinks")
    
    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)