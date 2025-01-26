"""Test the my_class module"""
import pytest
from source.my_class import MyList

class TestMyList:
    """Test the MyList class"""

    @pytest.fixture(scope="function")
    def prius(self):
        """Create a new MyList instance"""
        return MyList("test")

    def test_my_class_name(self, prius):
        """Test the name attribute"""
        assert prius.name == "test"

    def test_my_class_str(self, prius):
        """Test the __str__ method"""
        prius.add("value")
        assert str(prius) == "test: ['value']"
