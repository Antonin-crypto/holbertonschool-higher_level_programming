#!/usr/bin/env python3

from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Subclass Dog
class Dog(Animal):

    def sound(self):
        return "Bark"

# Subclass Cat
class Cat(Animal):

    def sound(self):
        return "Meow"
