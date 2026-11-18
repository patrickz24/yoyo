# yoyo — SaaS de récupération du tiers payant pour les centres de santé

**Idée retenue** (étape 3 du comité) : un copilote qui retrouve l'argent du tiers payant que perdent les centres de santé. Il rapproche ce qui a été facturé de ce qui est arrivé sur le compte, payeur par payeur, et prépare les réclamations.

**Objectif :** 1 M€ de revenu annuel récurrent, soit environ 215 centres à 390 €/mois, sans lever de fonds.

## Où on en est

| Étape | Statut |
|---|---|
| 1. 15 idées notées → top 3 | ✅ |
| 2. Recherche sur le top 3 | ✅ |
| 3. Verdict des experts → une seule idée | ✅ |
| 4. Validation sur 14 jours (30 entretiens) | ⏳ en cours, voir [`validation/`](validation/) |
| 5. Offre concierge payante + landing page | ✅ prêtes, voir [`offre/`](offre/) et [`site/`](site/) |
| 6. MVP | — |
| 7. Machine d'acquisition | — |

## Dossier `validation/`

- [`01-plan-14-jours.md`](validation/01-plan-14-jours.md) : les 30 profils, où les trouver, le calendrier et les seuils de décision.
- [`02-script-entretien.md`](validation/02-script-entretien.md) : le script d'entretien de 25 minutes et ses variantes par segment.
- [`03-messages.md`](validation/03-messages.md) : les messages LinkedIn, e-mail et téléphone, la relance, la confirmation d'audit.
- [`suivi-entretiens.csv`](validation/suivi-entretiens.csv) : le fichier de suivi, avec `;` comme séparateur (s'ouvre dans Excel).
- `score_seuils.py` : `python3 validation/score_seuils.py` calcule les 5 seuils et donne la décision.
- `finess_centres_sante.py` : extrait du fichier FINESS (open data) la liste des centres de santé, avec leur téléphone.

## Dossier `offre/` (étape 5)

- [`01-offre-audit.md`](offre/01-offre-audit.md) : l'offre, le déroulé jour par jour, les exports à demander, le cadre légal, les critères pour passer à l'étape 6.
- [`02-modele-rapport.md`](offre/02-modele-rapport.md) : le modèle du rapport remis au client.
- [`03-courriers-reclamation.md`](offre/03-courriers-reclamation.md) : les courriers pour une mutuelle, l'Assurance maladie et un patient.
- [`04-accord-confidentialite.md`](offre/04-accord-confidentialite.md) : l'accord de confidentialité, à faire relire par un avocat.
- [`05-bon-de-commande-et-facture.md`](offre/05-bon-de-commande-et-facture.md) : le bon de commande et les mentions obligatoires de la facture.

## Dossier `site/`

- [`index.html`](site/index.html) : la landing page « Encaissé ». Configuration et mise en ligne dans [`site/README.md`](site/README.md).
