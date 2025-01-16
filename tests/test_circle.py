import pytest
import math

import source.shapes as shapes

class TestCircle:
    def setup_method(self, method):
        print(f'SETUP {method}')
        self.circle = shapes.Circle(10)


    def teardown_method(self, method):
        print(f'TEARDOWN {method}')
        del self.circle


    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2


    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    
    def test_one(self):
        assert True
