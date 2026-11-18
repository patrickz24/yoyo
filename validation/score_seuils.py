#!/usr/bin/env python3
"""Calcule les 5 seuils de décision de l'étape 4 à partir de suivi-entretiens.csv.

Usage : python3 validation/score_seuils.py [chemin/vers/suivi-entretiens.csv]
"""
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

STRUCTURES = {"A", "B", "C", "D", "E"}  # centres + groupes : base des seuils
SEUILS = [
    # (code, libellé, test sur une ligne, minimum requis)
    ("S1", "Pointage >= 2 jours/mois",
     lambda r: num(r["jours_pointage_mois"]) >= 2, 11),
    ("S2", "Plus de 5 000 EUR dus depuis > 90 jours",
     lambda r: num(r["montant_plus_90j_eur"]) > 5000, 7),
    ("S3", "Outil actuel jugé insuffisant",
     lambda r: oui(r["outil_actuel_insuffisant"]), 11),
    ("S4", "Export Excel/CSV possible",
     lambda r: oui(r["export_possible"]), 15),
]
SEUIL_AUDITS = 3


def num(valeur):
    """Convertit '12 000', '12000,5' ou '' en nombre (0 si vide ou illisible)."""
    v = (valeur or "").replace(" ", "").replace(" ", "").replace("€", "").replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return 0.0


def oui(valeur):
    return (valeur or "").strip().lower() in {"oui", "o", "yes", "y", "1", "x"}


def charger(chemin):
    with open(chemin, newline="", encoding="utf-8-sig") as f:
        lignes = list(csv.DictReader(f, delimiter=";"))
    return [r for r in lignes if (r.get("segment") or "").strip().upper() != "EXEMPLE"]


def main():
    chemin = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("suivi-entretiens.csv")
    lignes = charger(chemin)
    faits = [r for r in lignes if (r.get("statut") or "").strip().lower() == "fait"]
    structures = [r for r in faits if (r.get("segment") or "").strip().upper() in STRUCTURES]

    print(f"Fichier : {chemin}")
    print(f"Contacts : {len(lignes)} | entretiens faits : {len(faits)} | dont structures A-E : {len(structures)}\n")

    # Entonnoir par canal
    contacts = Counter((r.get("canal") or "?").strip().lower() for r in lignes)
    rdv = Counter((r.get("canal") or "?").strip().lower() for r in lignes
                  if (r.get("statut") or "").strip().lower() in {"rdv", "fait"})
    print("Entonnoir par canal (contacts -> RDV/faits) :")
    for canal, n in contacts.most_common():
        taux = 100 * rdv[canal] / n if n else 0
        print(f"  {canal:<12} {n:>4} -> {rdv[canal]:>3}  ({taux:.0f} %)")
    print()

    # Seuils
    atteints = 0
    print("Seuils (base : structures A-E avec entretien fait) :")
    for code, libelle, test, minimum in SEUILS:
        n = sum(1 for r in structures if test(r))
        ok = n >= minimum
        atteints += ok
        print(f"  {'✅' if ok else '❌'} {code} {libelle:<42} {n:>3} / {len(structures)}  (minimum {minimum})")
    audits = sum(1 for r in faits if oui(r.get("audit_paye")))
    ok = audits >= SEUIL_AUDITS
    atteints += ok
    print(f"  {'✅' if ok else '❌'} S5 {'Audits payants acceptés (tous segments)':<42} {audits:>3}        (minimum {SEUIL_AUDITS})\n")

    # Bonus F / G
    par_seg = defaultdict(list)
    for r in faits:
        par_seg[(r.get("segment") or "").strip().upper()].append(r)
    ec_prescripteurs = sum(1 for r in par_seg["F"] if num(r["intros_obtenues"]) >= 2)
    facturieres_douleur = sum(1 for r in par_seg["G"] if oui(r["outil_actuel_insuffisant"])
                              and (num(r["jours_pointage_mois"]) >= 2 or num(r["montant_plus_90j_eur"]) > 5000))
    print("Bonus (n'entre pas dans la décision) :")
    print(f"  Experts-comptables prêts à présenter >= 2 clients : {ec_prescripteurs} (canal prioritaire si >= 2)")
    print(f"  Facturières avec douleur forte                   : {facturieres_douleur} (segment B2B à creuser si >= 2)\n")

    # Décision
    if atteints == 5:
        verdict = "GO -> étape 5 (offre concierge + landing page)"
    elif atteints == 4:
        verdict = "PRESQUE -> 1 semaine de plus sur le seuil manquant"
    else:
        verdict = "STOP -> plan B (conformité LCB-FT pour agences immobilières)"
    print(f"Seuils atteints : {atteints}/5  =>  {verdict}")
    if len(structures) < 22:
        print(f"(Attention : seulement {len(structures)} structures interviewées sur 22 prévues, verdict provisoire.)")


if __name__ == "__main__":
    main()
