#!/usr/bin/python3
def roman_to_int(roman_string):
    # Vérifie si la chaîne donnée est nulle
    if roman_string is None:
        return 0
    # Vérifie si la chaîne donnée est une chaîne de caractères
    if type(roman_string) is not str:
        return 0
    # les correspondances entre les chiffres romains et leurs valeurs décimales
    roman_v = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # Initialisation de la somme totale
    total = 0
    # Initialisation de la valeur précédente
    prev_value = 0
    # Parcours de la chaîne romaine à l'envers
    for numeral in reversed(roman_string):
        # Récupération de la valeur décimale du chiffre romain actuel
        value = roman_v[numeral]
        # Si la v est inférieure à la v précédente,soustraire cette v au total
        if value < prev_value:
            total -= value
            # Sinon, ajouter cette valeur au total
        else:
            total += value
            # Mettre à jour la valeur précédente pour la prochaine itération
        prev_value = value
        # Retourner la somme totale convertie
    return total
