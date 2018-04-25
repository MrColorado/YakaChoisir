import csv
import os


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
            res += "{asso} - {statut} : {nom} {prenom} est {fonction} ({mail}) ({mailPerso})".format(
                asso=line[self.asso],
                statut=line[self.statut],
                nom=line[self.nom],
                prenom=line[self.prenom],
                fonction=line[self.fonction],
                mail=line[self.mailIonis],
                mailPerso=line[self.mailIonis]
            )
            res += os.linesep
        return res

    def ToDataBase(self):
        """
        Fills up Django database with provided association and members.
        """
        with open(self.filename) as csvfile:
            reader = csv.DictReader(csvfile, dialect='excel')
