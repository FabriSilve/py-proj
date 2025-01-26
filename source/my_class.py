"""Example class for saving list data"""

class MyList:
    """Class to save list data"""

    def __init__(self, name):
        """Initialize the list"""
        self.__name = name
        self.__list = []

    @property
    def name(self):
        """Return the name"""
        return self.__name

    def add(self, item):
        """Add an item to the list"""
        self.__list.append(item)

    def __str__(self):
        """Return the list as a string"""
        return f"{self.__name}: {self.__list}"
