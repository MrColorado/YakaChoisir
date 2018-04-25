import csv
import os


# from src.databasIe.models import Association#, Members, User


class CSVParser:
    """
    Excel CSV file parser.
    Extracts association and members from provided CSV file
    """

    def __init__(self, filename):
        """
        Create a new CSVParser object.
        :param filename: path to CSV file
        """

        self.filename = filename
        self.entries = []

        with open(self.filename, "r") as csvfile:
            reader = csv.DictReader(csvfile, dialect='excel')

            self.asso = reader.fieldnames[0]
            self.statut = reader.fieldnames[1]
            self.tutelle = reader.fieldnames[2]
            self.nom = reader.fieldnames[3]
            self.prenom = reader.fieldnames[4]
            self.fonction = reader.fieldnames[5]
            self.mailPerso = reader.fieldnames[6]
            self.mailIonis = reader.fieldnames[7]

            for line in reader:
                self.entries.append(line)

    def __str__(self):
        """
        :return: CSV file parsed as a string
        """
        res = ""
        for line in self.entries:
            res += "{asso} - {statut} : {nom} {prenom} est {fonction} ({mailIonis}) ({mailPerso})".format(
                asso=line[self.asso],
                statut=line[self.statut],
                nom=line[self.nom],
                prenom=line[self.prenom],
                fonction=line[self.fonction],
                mailIonis=line[self.mailIonis],
                mailPerso=line[self.mailPerso]
            )
            res += os.linesep
        return res

    def to_database(self):
        """
        Fills up Django database with provided association and members.
        """
        res = ""
        current_asso = None
        for line in self.entries:
            # Association line
            if line[self.asso] != "":
                current_asso = line[self.asso]

                res += "New Association {name} {statut} {mail} would have been created\n".format(
                    name=line[self.asso],
                    statut=line[self.statut],
                    mail=line[self.mailIonis] if line[self.mailIonis] != "" else line[self.mailPerso]
                )
            # Member line
            if line[self.nom] != "":
                res += "New {asso} member:\n\t{prenom} {nom} est un {role} et est joignable a {mail} ou "\
                       "{mailSecondaire}".format(
                        asso=current_asso,
                        prenom=line[self.prenom],
                        nom=line[self.nom],
                        role=line[self.fonction],
                        mail=line[self.mailIonis],
                        mailSecondaire=line[self.mailPerso]
                        )
        return res
