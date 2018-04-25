import csv
import sys

with open(sys.argv[1], "r") as csvfile:
    reader = csv.DictReader(csvfile, dialect='excel')

    print(reader.fieldnames)

    asso = reader.fieldnames[0];
    statut = reader.fieldnames[1];
    tutelle = reader.fieldnames[2];
    nom = reader.fieldnames[3];
    prenom = reader.fieldnames[4];
    fonction = reader.fieldnames[5];
    mailPerso = reader.fieldnames[6];
    mailIonis = reader.fieldnames[7];

    for line in reader:
        print("{asso} - {statut} : {nom} {prenom} est {fonction} ({mail}) ({mailPerso})"
              .format(
            asso=line[asso],
            statut=line[statut],
            nom=line[nom],
            prenom=line[prenom],
            fonction=line[fonction],
            mail=line[mailIonis],
            mailPerso=line[mailIonis]
        ))
