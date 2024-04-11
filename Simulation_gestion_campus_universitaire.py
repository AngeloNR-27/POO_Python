# Exercice 03 : Simulation d'un systeme de gestion de campus universitaire

class Etudiant:
    def __init__(self, nom, prenom, age, adresse, niveau):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.niveau = niveau
        self.cours_suivis = []

    def enregistrer_cours(self, cours):
        self.cours_suivis.append(cours)

    def afficher_cours_suivis(self):
        for cours in self.cours_suivis:
            print(cours.nom)

class Cours:
    def __init__(self, nom, enseignant):
        self.nom = nom
        self.enseignant = enseignant
        self.etudiants_inscrits = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants_inscrits.append(etudiant)

    def afficher_etudiants_inscrits(self):
        for etudiant in self.etudiants_inscrits:
            print(etudiant.nom)

class Enseignant:
    def __init__(self, nom):
        self.nom = nom
        self.cours_enseignes = []

    def ajouter_cours(self, cours):
        self.cours_enseignes.append(cours)

    def afficher_cours_enseignes(self):
        for cours in self.cours_enseignes:
            print(cours.nom)

class GestionCampus:
    def __init__(self):
        self.etudiants = []
        self.cours = []
        self.enseignants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def ajouter_cours(self, cours):
        self.cours.append(cours)

    def ajouter_enseignant(self, enseignant):
        self.enseignants.append(enseignant)

    def inscrire_etudiant_cours(self, etudiant, cours):
        etudiant.enregistrer_cours(cours)
        cours.ajouter_etudiant(etudiant)

    def affichage(self):
        n=0
        print("######################\nListe des étudiants:")
        for etudiant in self.etudiants:
            print("Nom complet:",etudiant.nom, etudiant.prenom,"\nAge :", etudiant.age,"\nAdresse :", etudiant.adresse, "\nNiveau :", etudiant.niveau)
            print("Liste de cours suivi par l'etudiant:  ")
            Etudiant.afficher_cours_suivis(etudiant)
            print("--------------------------\n")
            
        print("\n######################\nListe des cours:")
        for cours in self.cours:
            print(cours.nom, cours.enseignant.nom)
        print("\n######################\nListe des enseignants:")
        for enseignant in self.enseignants:
            print(enseignant.nom)

# Ajout de données 
etudiant1 = Etudiant("RAKOTO","Bary", 20, "Lot IV 45 Bis Anatiala", "Licence 2")
etudiant2 = Etudiant("RASOLO","Koto", 22, "Lot 365 B Betafo","Licence 2")
cours1 = Cours("Programmation Orientée Objet", None)
cours2 = Cours("Algorithmique", None)
cours3 = Cours("Angular", None)
cours4 = Cours("Node", None)
cours5 = Cours("Symfony", None)
cours6 = Cours("Python", None)
enseignant1 = Enseignant("Mr. RABE")
enseignant2 = Enseignant("Mme. Rasoa")
enseignant3 = Enseignant("Mme. Lala")
enseignant4 = Enseignant("Mr. Solo")
enseignant5 = Enseignant("Mr. Benja")
enseignant6 = Enseignant("Mr. Koto")

cours1.enseignant = enseignant1
cours2.enseignant = enseignant2
cours3.enseignant = enseignant3
cours4.enseignant = enseignant4
cours5.enseignant = enseignant5
cours6.enseignant = enseignant6

enseignant1.ajouter_cours(cours1)
enseignant2.ajouter_cours(cours2)
enseignant3.ajouter_cours(cours3)
enseignant4.ajouter_cours(cours4)
enseignant5.ajouter_cours(cours5)
enseignant6.ajouter_cours(cours6)

gestion_campus = GestionCampus()

gestion_campus.ajouter_etudiant(etudiant1)
gestion_campus.ajouter_etudiant(etudiant2)
gestion_campus.ajouter_cours(cours1)
gestion_campus.ajouter_cours(cours2)
gestion_campus.ajouter_cours(cours3)
gestion_campus.ajouter_cours(cours4)
gestion_campus.ajouter_cours(cours5)
gestion_campus.ajouter_cours(cours6)
gestion_campus.ajouter_enseignant(enseignant1)
gestion_campus.ajouter_enseignant(enseignant2)
gestion_campus.ajouter_enseignant(enseignant3)
gestion_campus.ajouter_enseignant(enseignant4)
gestion_campus.ajouter_enseignant(enseignant5)
gestion_campus.ajouter_enseignant(enseignant6)

gestion_campus.inscrire_etudiant_cours(etudiant1, cours1)
gestion_campus.inscrire_etudiant_cours(etudiant2, cours2)
gestion_campus.inscrire_etudiant_cours(etudiant2, cours3)
gestion_campus.inscrire_etudiant_cours(etudiant1, cours4)
gestion_campus.inscrire_etudiant_cours(etudiant1, cours5)
gestion_campus.inscrire_etudiant_cours(etudiant2, cours6)

gestion_campus.affichage()
