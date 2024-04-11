class Utilisateur:
    def __init__(self, nom, age, poids, taille, objectifs):
        self.nom = nom
        self.age = age
        self.poids = poids
        self.taille = taille
        self.objectifs = objectifs

    def definir_objectifs(self, nouveaux_objectifs):
        self.objectifs = nouveaux_objectifs

class Activite:
    def __init__(self, type_activite, duree, calories_brulees, intensite):
        self.type_activite = type_activite
        self.duree = duree
        self.calories_brulees = calories_brulees
        self.intensite = intensite

class ObjectifSante:
    def __init__(self, poids_cible, objectifs_hebdomadaires, depense_calorique_journaliere):
        self.poids_cible = poids_cible
        self.objectifs_hebdomadaires = objectifs_hebdomadaires
        self.depense_calorique_journaliere = depense_calorique_journaliere

    def suivre_progression(self, progression):
        pass

    def ajuster_objectifs(self, nouveaux_objectifs):
        pass

class ApplicationRemiseEnForme:
    def __init__(self):
        self.utilisateurs = []

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def enregistrer_activite(self, utilisateur, activite):
        pass

    def mettre_a_jour_objectifs(self, utilisateur, nouveaux_objectifs):
        utilisateur.definir_objectifs(nouveaux_objectifs)

    def suivre_progression_utilisateur(self, utilisateur):
        pass

# Code pour tester les fonctionnalités
if __name__ == "__main__":
    application = ApplicationRemiseEnForme()

    utilisateur1 = Utilisateur("RAKOTO", 30, 65, 170, {"poids_cible": 60, "objectifs_hebdomadaires": 3, "depense_calorique_journaliere": 2000})
    print("Utilisateur créé :", utilisateur1.nom)

    application.ajouter_utilisateur(utilisateur1)
    print("Utilisateur ajouté à l'application")

    activite1 = Activite("Course à pied", 30, 300, "Intense")
    application.enregistrer_activite(utilisateur1, activite1)
    print("Activité enregistrée :", activite1.type_activite)

    nouveaux_objectifs = {"poids_cible": 55, "objectifs_hebdomadaires": 5, "depense_calorique_journaliere": 2500}
    application.mettre_a_jour_objectifs(utilisateur1, nouveaux_objectifs)
    print("Objectifs mis à jour :", utilisateur1.objectifs)

    application.suivre_progression_utilisateur(utilisateur1)
    print("Progression suivie avec succès.")
