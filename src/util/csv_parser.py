import csv
import os


class CSVParser:
    """
    Excel CSV file parser.
    Extracts association and members from provided CSV file
    """

    def __init__(self, filename):
        self.filename = filename
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

    def __str__(self):
        str = ""
        with open(self.filename, "r") as csvfile:
            reader = csv.DictReader(csvfile, dialect='excel')
            for line in reader:
                str += "{asso} - {statut} : {nom} {prenom} est {fonction} ({mail}) ({mailPerso})".format(
                    asso=line[self.asso],
                    statut=line[self.statut],
                    nom=line[self.nom],
                    prenom=line[self.prenom],
                    fonction=line[self.fonction],
                    mail=line[self.mailIonis],
                    mailPerso=line[self.mailIonis]
                )
                str += os.linesep
        return str
