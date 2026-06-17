# ByteBites Core Architecture
# Models: Customer, FoodItem, Menu, Transaction


class FoodItem:
    """
    Represents a sellable food item in the ByteBites menu.
    
    Attributes:
        name: Item name (e.g., "Spicy Burger", "Large Soda")
        price: Cost of the item in dollars
        category: Classification (e.g., "Drinks", "Desserts")
        popularityRating: Measure of item popularity (0.0 to 5.0 scale)
    """
    
    def __init__(self, name, price, category, popularityRating):
        """
        Initialize a FoodItem with all required attributes.
        
        Args:
            name: Item name (str)
            price: Cost in dollars (float)
            category: Classification category (str)
            popularityRating: Popularity rating (float)
        """
        self.name = name
        self.price = price
        self.category = category
        self.popularityRating = popularityRating


class Menu:
    """
    Manages the complete collection of available FoodItem objects.
    
    Attributes:
        items: List of FoodItem objects available for purchase
    """
    
    def __init__(self, items=None):
        """
        Initialize a Menu with an optional list of items.
        
        Args:
            items: Optional list of FoodItem objects; defaults to empty list
        """
        self.items = items if items is not None else []
    
    def addItem(self, item):
        """
        Add a FoodItem to the menu.
        
        Args:
            item: FoodItem object to add
        """
        pass
    
    def removeItem(self, item):
        """
        Remove a FoodItem from the menu.
        
        Args:
            item: FoodItem object to remove
        """
        pass
    
    def getAllItems(self):
        """
        Retrieve all items currently in the menu.
        
        Returns:
            List of all FoodItem objects
        """
        pass
    
    def filterByCategory(self, category):
        """
        Filter menu items by a specific category.
        
        Args:
            category: Category name to filter by (str)
        
        Returns:
            List of FoodItem objects matching the category
        """
        pass


class Transaction:
    """
    Represents a single purchase transaction grouping selected items.
    
    Attributes:
        selectedItems: List of FoodItem objects chosen for this purchase
        totalCost: Calculated total cost of all items in the transaction
    """
    
    def __init__(self, selectedItems=None):
        """
        Initialize a Transaction with optional selected items.
        
        Args:
            selectedItems: Optional list of FoodItem objects; defaults to empty list
        """
        self.selectedItems = selectedItems if selectedItems is not None else []
        self.totalCost = 0.0
    
    def addItem(self, item):
        """
        Add a FoodItem to this transaction.
        
        Args:
            item: FoodItem object to add
        """
        pass
    
    def removeItem(self, item):
        """
        Remove a FoodItem from this transaction.
        
        Args:
            item: FoodItem object to remove
        """
        pass
    
    def computeTotalCost(self):
        """
        Calculate the total cost of all items in the transaction.
        
        Returns:
            Total cost as a float
        """
        pass


class Customer:
    """
    Represents a customer in the ByteBites system.
    
    Attributes:
        name: Customer identifier
        purchaseHistory: List of past Transaction objects
    """
    
    def __init__(self, name, purchaseHistory=None):
        """
        Initialize a Customer with a name and optional purchase history.
        
        Args:
            name: Customer name (str)
            purchaseHistory: Optional list of Transaction objects; defaults to empty list
        """
        self.name = name
        self.purchaseHistory = purchaseHistory if purchaseHistory is not None else []
    
    def verifyUser(self):
        """
        Verify that the customer is a valid user.
        
        Returns:
            Boolean indicating user authenticity
        """
        pass