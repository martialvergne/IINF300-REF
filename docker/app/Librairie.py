class Librairie:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.liste_livres = []

    # Accesseurs
    def get_nom(self):
        return self.nom

    def get_adresse(self):
        return self.adresse

    def get_livre(self):
        return self.liste_livres

    # Mutateurs
    def set_nom(self, nom):
        self.nom = nom

    def set_adresse(self, adresse):
        self.adresse = adresse

    def set_livre(self, liste_livres):
        self.liste_livres = liste_livres

    # Méthodes pour ajouter et supprimer des livres
    def ajouter_livre(self, livre):
        if not isinstance(livre, list):
            print("Erreur, element non conforme")
            return False
        # Vérifie si la liste a exactement deux éléments
        if len(livre) != 2:
            print("Erreur, element non conforme")
            return False
        # Vérifie si les deux éléments sont des chaînes de caractères
        if not all(isinstance(element, str) for element in livre):
            print("Erreur, element non conforme")
            return False
        self.liste_livres.append(livre)
        print("Element ajoute avec succes")
        return True

    def supprimer_livre(self, titre):
        for livre in self.liste_livres:
            if livre[0] == titre:
                self.liste_livres.remove(livre)
                print("livre: ", titre, ", bien supprimé")
                return
        print("Le livre", titre, "n'est pas dans la bibliothèque.")

    def __repr__(self):
        return [self.nom, self.adresse, self.liste_livres]
