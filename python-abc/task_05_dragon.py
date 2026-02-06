#!/usr/bin/env python3
"""Dragon module demonstrating mixins"""

class SwimMixin:
    """Mixin class to add swimming ability"""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin class to add flying ability"""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can both swim and fly"""

    def roar(self):
        print("The dragon roars!")
