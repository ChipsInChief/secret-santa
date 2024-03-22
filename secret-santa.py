# Définition de quelques participants
# Utilisation de variables pour stocker des informations simples
player1_name = "Alice"
player1_email = "alice@example.com"

player2_name = "Bob"
player2_email = "bob@example.com"

# Calcul simple pour montrer l'utilisation des types numériques
number_of_players = 2
print("Nombre de participants :")
print(number_of_players)

# Affichage des informations des participants
print("--------------- PARTICIPANTS ---------------")
print(player1_name)
print(player1_email)

print(player2_name)
print(player2_email)
print("--------------------------------------------")

# Assignation manuelle
player1_result = player2_name  # Alice offre un cadeau à Bob
player2_result = player1_name  # Bob offre un cadeau à Alice

# Affichage des paires Secret Santa
print("Résultat du tirage :")
print(player1_name, "offre un cadeau à", player1_result)
print(player2_name, "offre un cadeau à", player2_result)
