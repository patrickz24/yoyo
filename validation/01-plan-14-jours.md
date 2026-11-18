# Étape 4 — Plan de validation sur 14 jours

**Idée testée :** le copilote qui retrouve l'argent du tiers payant perdu par les centres de santé.
Il rapproche ce qui a été facturé de ce qui est arrivé sur le compte, payeur par payeur, puis prépare les réclamations.

**Objectif :** réaliser 30 entretiens et décrocher au moins 3 audits payants en 14 jours, pour décider si on continue ou si on arrête.

---

## 1. Les 30 profils à interviewer, plus ton cousin (entretien n° 0)

| Segment | Nb | Qui exactement | Pourquoi |
|---|---|---|---|
| **A. Centres dentaires** | 8 | Gestionnaire, directeur administratif, responsable facturation ou tiers payant | Cœur de cible : gros volumes de paiements mutuelles |
| **B. Centres d'ophtalmologie** | 4 | Mêmes fonctions | Deuxième cœur de cible, gros volumes |
| **C. Centres médicaux ou polyvalents** | 4 | Mêmes fonctions, souvent dans des centres associatifs ou municipaux | Tester un segment plus « public » |
| **D. Centres de soins infirmiers** | 2 | Directeur ou coordinateur | Segment lié au réseau de ton cousin |
| **E. Groupes de plusieurs centres** | 4 | DAF, contrôleur de gestion, directeur des opérations | Un seul contrat couvre 5 à 30 centres |
| **F. Experts-comptables spécialisés santé** | 4 | Associé ou chef de mission | Ils voient le problème chez plus de 10 clients et peuvent te recommander |
| **G. Sociétés de facturation (« facturières »)** | 4 | Gérant | Segment B2B à tester |
| **Total** | **30** | | |

**L'entretien n° 0 avec ton cousin** ne compte pas dans les 30. Il te sert à roder le script et à obtenir 2 ou 3 présentations à d'autres personnes.

---

## 2. Seuils de décision

Les seuils sont calculés sur les **22 structures des segments A à E**.

| # | Seuil | Pour continuer |
|---|---|---|
| 1 | **Temps** : la structure passe au moins 2 jours par mois au pointage et au rapprochement | ≥ 11 sur 22 |
| 2 | **Argent** : plus de 5 000 € dus depuis plus de 90 jours | ≥ 7 sur 22 |
| 3 | **Outils** : l'outil actuel (logiciel, banque, comptable) est jugé insuffisant | ≥ 11 sur 22 |
| 4 | **Données** : la structure peut exporter ses factures et ses paiements en Excel ou CSV | ≥ 15 sur 22 |
| 5 | **Engagement** : la structure accepte un audit payant (tous segments confondus) | ≥ 3 |

**Bonus F et G** (sans effet sur la décision) :
- au moins 2 experts-comptables prêts à te présenter des clients, et ce canal devient prioritaire ;
- au moins 2 facturières avec une douleur forte, et ce segment B2B mérite d'être creusé.

**Décision au jour 14**, avec `python3 validation/score_seuils.py` :
- **5 seuils sur 5** : on passe à l'étape 5 (offre concierge et landing page).
- **4 sur 5** : on consacre une semaine de plus au seuil manquant.
- **3 ou moins** : on arrête et on passe au **plan B** (conformité anti-blanchiment pour les agences immobilières).

---

## 3. Où trouver les contacts

1. **Ton cousin** : 2 ou 3 présentations dès le jour 1. Ce sont les contacts les plus chauds.
2. **FINESS**, le fichier national des établissements, en open data. Il liste tous les centres de santé avec leur adresse et leur téléphone.
   - Télécharge l'extraction « FINESS Extraction du Fichier des établissements » sur data.gouv.fr.
   - Lance `python3 validation/finess_centres_sante.py <fichier.csv> --dept 75,92,93,94`.
   - Tu obtiens un CSV de centres à appeler, triés par département.
3. **Google Maps** : cherche « centre dentaire » ou « centre ophtalmologique » suivi d'une ville, pour trouver le téléphone et le nom du gestionnaire.
4. **LinkedIn** : recherche par intitulé de poste.
   - `gestionnaire centre de santé`
   - `directeur centre dentaire`
   - `responsable facturation tiers payant`
   - `coordinatrice centre de santé`
   - `DAF groupe centres dentaires`
   - `contrôleur de gestion centres de santé`
5. **Experts-comptables** : recherche Google `expert-comptable centre de santé` ou `expert-comptable centre dentaire`.
6. **Facturières** : recherche Google `société de facturation infirmier libéral` ou `facturière IDEL`.

**Hypothèse d'entonnoir, à mesurer** : environ 180 contacts pour obtenir environ 30 entretiens (1 sur 6).
- Répartition : 60 appels, 60 invitations LinkedIn, 60 e-mails.
- Le script affiche la conversion réelle de chaque canal.

---

## 4. Calendrier

| Jour | Actions |
|---|---|
| **J1** | Entretien n° 0 avec ton cousin, pour roder le script. Construire la liste de 180 contacts dans `suivi-entretiens.csv` (statut `a_contacter`). |
| **J2 à J5** | Chaque jour : 15 appels (entre 9 h et 11 h 30, en évitant le lundi matin), 12 invitations LinkedIn, 12 e-mails. Relancer chaque contact au bout de 3 jours. Premiers entretiens dès J3. |
| **J6 et J7** | Mettre au propre les notes, mettre à jour le CSV, lancer `score_seuils.py`. |
| **J8** | **Point à mi-parcours.** Si moins de 10 entretiens sont faits ou planifiés, doubler les appels. |
| **J8 à J12** | Entretiens (3 par jour au maximum). Proposer l'audit payant aux structures qui atteignent les seuils 1 et 2. |
| **J13** | Dernières relances, synthèse. |
| **J14** | Décision. |

**Temps à prévoir :** 25 à 30 heures par semaine.

---

## 5. Règles d'or

- **Ne vends rien** pendant l'entretien. L'audit ne se propose qu'à la toute fin, et seulement si la douleur est confirmée.
- **Des faits passés et des chiffres, pas d'avis sur l'avenir.** « Vous l'achèteriez ? » ne vaut rien. « Combien vous a coûté le dernier rejet ? » vaut de l'or.
- **Données de santé : ne récupère JAMAIS de fichier contenant des noms de patients ou des numéros de Sécurité sociale.** Pour l'audit, travaille en visio sur l'écran du client, ou sur des exports sans identité des patients (n° de facture, date, montant, payeur, statut).
- **Note chaque entretien dans le CSV le jour même.**
- **Prospection par e-mail entre professionnels** : la CNIL l'autorise sans consentement préalable si le message concerne le métier de la personne et qu'elle peut refuser facilement. Termine donc chaque e-mail par une ligne « Répondez STOP ».
