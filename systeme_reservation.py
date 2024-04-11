class Evenement:
    def __init__(self, nom, date, lieu, places_disponibles):
        self.nom = nom
        self.date = date
        self.lieu = lieu
        self.places_disponibles = places_disponibles

    def verifier_disponibilites(self, nombre_de_places):
        return self.places_disponibles >= nombre_de_places

    def reserver_places(self, nombre_de_places):
        if self.verifier_disponibilites(nombre_de_places):
            self.places_disponibles -= nombre_de_places
            print(f"{nombre_de_places} places ont été réservées pour l'événement {self.nom}.")
        else:
            print("Désolé, il n'y a pas assez de places disponibles.")

    def annuler_reservation(self, nombre_de_places):
        self.places_disponibles += nombre_de_places
        print(f"{nombre_de_places} places ont été annulées pour l'événement {self.nom}.")

    def afficher_details(self):
        print(f"Nom de l'événement : {self.nom}")
        print(f"Date : {self.date}")
        print(f"Lieu : {self.lieu}")
        print(f"Places disponibles : {self.places_disponibles}")

class Utilisateur:
    def __init__(self, nom, email, infos_contact):
        self.nom = nom
        self.email = email
        self.infos_contact = infos_contact

    def reserver_billets(self, evenement, nombre_de_places):
        evenement.reserver_places(nombre_de_places)

    def annuler_reservation(self, evenement, nombre_de_places):
        evenement.annuler_reservation(nombre_de_places)

    def afficher_details_reservation(self, evenement, nombre_de_places):
        print(f"Utilisateur : {self.nom}")
        print(f"Événement réservé : {evenement.nom}")
        print(f"Nombre de places réservées : {nombre_de_places}")

class Reservation:
    def __init__(self, utilisateur, evenement, nombre_de_places):
        self.utilisateur = utilisateur
        self.evenement = evenement
        self.nombre_de_places = nombre_de_places

    def cout_total(self):
        pass

    def modifier_reservation(self, nouveau_nombre_de_places):
        pass

class SystemeReservation:
    def __init__(self):
        self.utilisateurs = []
        self.evenements = []
        self.reservations = []

    def creer_evenement(self, nom, date, lieu, places_disponibles):
        evenement = Evenement(nom, date, lieu, places_disponibles)
        self.evenements.append(evenement)
        return evenement

    def ajouter_utilisateur(self, nom, email, infos_contact):
        utilisateur = Utilisateur(nom, email, infos_contact)
        self.utilisateurs.append(utilisateur)
        return utilisateur

    def effectuer_reservation(self, utilisateur, evenement, nombre_de_places):
        if evenement.verifier_disponibilites(nombre_de_places):
            reservation = Reservation(utilisateur, evenement, nombre_de_places)
            self.reservations.append(reservation)
            evenement.reserver_places(nombre_de_places)
            print("Réservation effectuée avec succès.")
        else:
            print("Désolé, il n'y a pas assez de places disponibles.")

    def afficher_reservations(self):
        for reservation in self.reservations:
            print(f"Utilisateur : {reservation.utilisateur.nom}, Événement : {reservation.evenement.nom}, Places réservées : {reservation.nombre_de_places}")

# Code pour tester les fonctionnalités en utilisant les entrées utilisateur

if __name__ == "__main__":
    systeme = SystemeReservation()

    nom_evenement = input("Entrez le nom de l'événement : ")
    date_evenement = input("Entrez la date de l'événement (format YYYY-MM-DD) : ")
    lieu_evenement = input("Entrez le lieu de l'événement : ")
    places_disponibles = int(input("Entrez le nombre de places disponibles : "))

    evenement = systeme.creer_evenement(nom_evenement, date_evenement, lieu_evenement, places_disponibles)

    nom_utilisateur = input("Entrez le nom de l'utilisateur : ")
    email_utilisateur = input("Entrez l'email de l'utilisateur : ")
    infos_contact_utilisateur = input("Entrez les informations de contact de l'utilisateur : ")

    utilisateur = systeme.ajouter_utilisateur(nom_utilisateur, email_utilisateur, infos_contact_utilisateur)

    nombre_places = int(input("Entrez le nombre de places à réserver : "))

    systeme.effectuer_reservation(utilisateur, evenement, nombre_places)

    systeme.afficher_reservations()

