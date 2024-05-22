#!/usr/bin/env python3

# Define the SwimMixin with swim method
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Define the FlyMixin with fly method
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Create the Dragon class inheriting from both mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Instantiate a Dragon object
draco = Dragon()

# Demonstrate abilities
draco.swim()
draco.fly()
draco.roar()
