# Définition de quelques participants
# Utilisation de variables pour stocker des informations simples
player1_name = input("Saisissez le prénom du premier participant : ")
player1_age = int(input("Quel est l'âge du premier participant ? "))

# Collecte et vérification de l'autorisation parentale pour les mineurs
if player1_age < 18:
    player1_autorisation_parentale = (
        input(
            "Le premier participant a-t-il une autorisation parentale (oui/non) ? "
        ).lower()
        == "oui"
    )
    player1_email = input(
        "Saisissez l'adresse mail du représentant légal du premier participant : "
    ).lower()
else:
    player1_autorisation_parentale = (
        True  # Considéré comme ayant une autorisation par défaut
    )
    player1_email = input("Saisissez l'adresse mail du premier participant : ").lower()

player2_name = input("Saisissez le prénom du second participant : ")
player2_age = int(input("Quel est l'âge du second participant ? "))

# Collecte et vérification de l'autorisation parentale pour les mineurs
if player2_age < 18:
    player2_autorisation_parentale = (
        input(
            "Le second participant a-t-il une autorisation parentale (oui/non) ? "
        ).lower()
        == "oui"
    )
    player2_email = input(
        "Saisissez l'adresse mail du représentant légal du second participant : "
    ).lower()
else:
    player2_autorisation_parentale = (
        True  # Considéré comme ayant une autorisation par défaut
    )
    player2_email = input("Saisissez l'adresse mail du second participant : ").lower()

# Vérification que les e-mails sont différents
if player1_email == player2_email:
    print("Erreur : Les participants ne peuvent pas avoir le même e-mail.")
else:
    # Calcul simple pour montrer l'utilisation des types numériques
    number_of_players = 2
    print(f"Nombre de participants : {number_of_players}")

    # Affichage des informations des participants avec vérification de l'âge
    print("--------------- PARTICIPANTS ---------------")
    if player1_age < 18:
        print(
            f"\t- {player1_name} ({player1_age} ans) : {player1_email} [Mineur] - Autorisation parentale: {'Oui' if player1_autorisation_parentale else 'Non'}"
        )
    else:
        print(f"\t- {player1_name} ({player1_age} ans) : {player1_email} [Majeur]")

    if player2_age < 18:
        print(
            f"\t- {player2_name} ({player2_age} ans) : {player2_email} [Mineur] - Autorisation parentale: {'Oui' if player2_autorisation_parentale else 'Non'}"
        )
    else:
        print(f"\t- {player2_name} ({player2_age} ans) : {player2_email} [Majeur]")
    print("--------------------------------------------")

    # Assignation des paires avec vérification
    if (player1_age >= 18 or player1_autorisation_parentale) and (
        player2_age >= 18 or player2_autorisation_parentale
    ):
        player1_result = player2_name  # Player 1 offre un cadeau à Player 2
        player2_result = player1_name  # Player 2 offre un cadeau à Player 1
    else:
        print(
            "Erreur : Les participants mineurs doivent avoir une autorisation parentale."
        )

    # Affichage des paires Secret Santa
    print("Résultat du tirage :")
    print(f"{player1_name} offre un cadeau à {player1_result}")
    print(f"{player2_name} offre un cadeau à {player2_result}")
