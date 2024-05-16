#!/usr/bin/python3
"""Module contenant la classe Square."""


class Square:
    """Classe représentant un carré."""

    def __init__(self, size=0):
        """Initialise un carré avec une taille optionnelle."""
        self.size = size  # Définit la taille du carré

    @property
    def size(self):
        """Obtient la taille du carré."""
        return self._size  # Retourne la taille du carré

    @size.setter
    def size(self, value):
        """Définit la taille du carré avec des vérifications."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")  # Vérifie si la taille
        if value < 0:
            raise ValueError("size must be >= 0")  # Vérifie si la taille negat
        self._size = value  # Définit la taille du carré

    def area(self):
        """Calcule et retourne l'aire du carré."""
        return self._size ** 2  # Retourne l'aire du carré

    def my_print(self):
        """imprimer la valeur de la taille"""
        if self._size == 0:
            print("")
        else:
            for _ in range(self._size):
                print("#" * self._size)
