#!/usr/bin/env python3
"""Extrait les centres de santé du fichier FINESS (open data) pour construire une liste d'appels.

1. Télécharger sur data.gouv.fr le jeu « FINESS Extraction du Fichier des établissements »
   (fichier etalab-cs1100507-stock-AAAAMMJJ-HHMM.csv, séparateur ';').
2. python3 validation/finess_centres_sante.py <fichier_finess.csv> [--dept 69,75,92] [--sortie centres.csv]

Le format FINESS « structureet » est supposé être celui publié par Etalab (32 colonnes).
Si le format a changé, le script le signale et propose --brut pour sortir les lignes telles quelles.
"""
import argparse
import csv
import re
import sys

COLONNES = [
    "section", "nofinesset", "nofinessej", "rs", "rslongue", "complrs", "compldistrib",
    "numvoie", "typvoie", "voie", "compvoie", "lieuditbp", "commune", "departement",
    "libdepartement", "ligneacheminement", "telephone", "telecopie", "categetab",
    "libcategetab", "categagretab", "libcategagretab", "siret", "codeape", "codemft",
    "libmft", "codesph", "libsph", "dateouv", "dateautor", "datemaj", "numuai",
]
IDX = {nom: i for i, nom in enumerate(COLONNES)}
MOTIF = re.compile(r"centre\s+de\s+sant", re.IGNORECASE)
SORTIE = ["finess", "nom", "adresse", "code_postal_ville", "departement", "telephone",
          "categorie", "siret", "statut", "date_contact", "notes"]


def lire_lignes(chemin):
    for encodage in ("utf-8-sig", "latin-1"):
        try:
            with open(chemin, newline="", encoding=encodage) as f:
                return list(csv.reader(f, delimiter=";"))
        except UnicodeDecodeError:
            continue
    sys.exit("Impossible de lire le fichier (encodage inconnu).")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("fichier")
    p.add_argument("--dept", help="Départements à garder, ex. 69,75,92 (défaut : tous)")
    p.add_argument("--sortie", default="centres_de_sante.csv")
    p.add_argument("--brut", action="store_true", help="Sortir les lignes brutes si le format diffère")
    args = p.parse_args()

    depts = {d.strip().zfill(2) for d in args.dept.split(",")} if args.dept else None
    structures = [l for l in lire_lignes(args.fichier) if l and l[0] == "structureet"]
    if not structures:
        sys.exit("Aucune ligne 'structureet' trouvée : ce n'est pas l'extraction FINESS attendue.")

    format_ok = len(structures[0]) >= len(COLONNES) - 1
    if not format_ok and not args.brut:
        sys.exit(f"Format inattendu ({len(structures[0])} colonnes au lieu de {len(COLONNES)}). "
                 "Relance avec --brut pour obtenir les lignes contenant « centre de santé ».")

    retenus = []
    for l in structures:
        if args.brut or not format_ok:
            if any(MOTIF.search(c or "") for c in l):
                retenus.append(l)
            continue
        get = lambda nom: l[IDX[nom]].strip() if IDX[nom] < len(l) else ""
        if not MOTIF.search(get("libcategetab")):
            continue
        if depts and get("departement").zfill(2) not in depts:
            continue
        adresse = " ".join(x for x in (get("numvoie"), get("typvoie"), get("voie"), get("compvoie")) if x)
        retenus.append([
            get("nofinesset"), get("rslongue") or get("rs"), adresse, get("ligneacheminement"),
            get("libdepartement") or get("departement"), get("telephone"),
            get("libcategetab"), get("siret"), "a_contacter", "", "",
        ])

    with open(args.sortie, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        if not (args.brut or not format_ok):
            w.writerow(SORTIE)
        w.writerows(retenus)

    print(f"{len(structures)} établissements lus, {len(retenus)} centres de santé retenus -> {args.sortie}")
    if not (args.brut or not format_ok):
        par_cat = {}
        for r in retenus:
            par_cat[r[6]] = par_cat.get(r[6], 0) + 1
        for cat, n in sorted(par_cat.items(), key=lambda x: -x[1]):
            print(f"  {n:>5}  {cat}")


if __name__ == "__main__":
    main()
