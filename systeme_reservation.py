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

# Code pour tester les fonctionnalités
if __name__ == "__main__":

    systeme = SystemeReservation()


    evenement1 = systeme.creer_evenement("Concert", "2024-04-20", "Salle de concert A", 100)
    evenement2 = systeme.creer_evenement("Conférence", "2024-05-10", "Salle de conférence B", 50)


    utilisateur1 = systeme.ajouter_utilisateur("Bob", "alice@gmail.com", "123456789")
    utilisateur2 = systeme.ajouter_utilisateur("Marley", "bob@gmail.com", "987654321")


    systeme.effectuer_reservation(utilisateur1, evenement1, 2)
    systeme.effectuer_reservation(utilisateur2, evenement2, 3)


    systeme.afficher_reservations()
