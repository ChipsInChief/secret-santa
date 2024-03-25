# Définition de quelques participants
# Utilisation de variables pour stocker des informations simples
player1_name = input("Saisissez le prénom du premier participant : ")
player1_email = input("Saisissez l'adresse mail du premier participant : ")
player1_email = player1_email.lower()
player1_age = int(input("Quel est l'âge du premier participant ? "))

player2_name = input("Saisissez le prénom du second participant : ")
player2_email = input("Saisissez l'adresse mail du second participant : ")
player2_email = player2_email.lower()
player2_age = int(input("Quel est l'âge du second participant ? "))

# Calcul simple pour montrer l'utilisation des types numériques
number_of_players = 2
print(f"Nombre de participants : {number_of_players}")

# Affichage des informations des participants
print("--------------- PARTICIPANTS ---------------")
print(f"\t- {player1_name} ({player1_age} ans) : {player1_email}")
print(f"\t- {player2_name} ({player2_age} ans) : {player2_email}")
print("--------------------------------------------")

# Assignation manuelle
player1_result = player2_name  # Alice offre un cadeau à Bob
player2_result = player1_name  # Bob offre un cadeau à Alice

# Affichage des paires Secret Santa
print("Résultat du tirage :")
print(f"{player1_name} offre un cadeau à {player1_result}")
print(f"{player2_name} offre un cadeau à {player2_result}")
