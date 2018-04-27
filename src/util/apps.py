import csv
import os

from django.apps import AppConfig
from django.contrib.auth.models import User

from database.models import Association, myUser, Members


class UtilConfig(AppConfig):
    name = 'util'


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
        current_asso = None
        for line in self.entries:
            # Association line
            if line[self.asso] != "":
                current_asso = Association()
                current_asso.name = line[self.asso]
                # TODO tutelle ?
                current_asso.statut = line[self.statut]
                current_asso.mail = line[self.mailIonis] if line[self.mailIonis] != "" else line[self.mailPerso]

                current_asso.save()
            # Member with an email address line
            if line[self.nom] != "" and line[self.mailIonis] != "":
                # Check if the user has already been added
                select = User.objects.filter(email=line[self.mailIonis])
                if select.count() > 0:
                    continue

                # Create Django User entry
                user = User.objects.create_user(line[self.mailIonis])
                user.first_name = line[self.prenom]
                user.last_name = line[self.nom]
                user.email = line[self.mailIonis]
                user.is_staff = False
                # create MyUser entry
                my_user = myUser.objects.get(user=user)
                my_user.mail_secondary = line[self.mailPerso]

                user.save()

                # Add to Members table
                AssoMemberEntry = Members()
                AssoMemberEntry.association_id = current_asso
                AssoMemberEntry.user_id = my_user
                AssoMemberEntry.role = line[self.fonction]

                AssoMemberEntry.save()
