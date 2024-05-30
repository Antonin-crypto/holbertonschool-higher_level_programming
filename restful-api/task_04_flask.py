#!/usr/bin/python3
"""Développer une API simple en utilisant Python avec Flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)


# Dictionnaire des utilisateurs
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """Route de la page d'accueil"""
    return "Bienvenue dans l'API Flask !"


@app.route('/data')
def get_data():
    """Route pour obtenir tous les noms d'utilisateur"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Route de statut"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Route pour obtenir les informations d'un utilis par nom d'utilisateur"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Utilisateur non trouvé"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Route pour ajouter un nouvel utilisateur"""
    user_data = request.json
    username = user_data.get('username')
    if username and username not in users:
        users[username] = {
            "name": user_data.get('name'),
            "age": user_data.get('age'),
            "city": user_data.get('city')
        }
        return jsonify({"message": "Utilisat ajouté", "user": users[username]})
    else:
        return jsonify({"error": "Données invalides ou utilisa exi déjà"}), 400


if __name__ == '__main__':
    # Démarrer le serveur de développement Flask
    app.run(debug=True)
