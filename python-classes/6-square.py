#!/usr/bin/python3
"""Module contenant la classe Square."""


class Square:
    """Classe représentant un carré."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec une taille optionnelle."""
        self.size = size  # Définit la taille du carré
        self.position = position

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

    @property
    def position(self):
        """definir la position actuelle"""
        return self._position

    @position.setter
    def position(self, value):
        """definit la position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calcule et retourne l'aire du carré."""
        return (self._size * self._size)  # Retourne l'aire du carré

    def my_print(self):
        """imprimer la valeur de la taille"""
        if self._size == 0:
            print("")

        for _ in range(self._position[1]):
            print("")

        for _ in range(self._size):
            print("_" * self._position[0] + "#" * self._size)
