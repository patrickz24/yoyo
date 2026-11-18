# Étape 5 — L'offre concierge : l'audit tiers payant

**Le principe :** avant d'écrire une ligne de code, tu fais le travail **à la main** pour 3 à 5 centres qui te paient.
Tu prouves ainsi trois choses : qu'ils paient, que l'argent perdu existe, et quelles étapes il faudra automatiser en premier.

---

## 1. L'offre en une phrase

> En 5 jours ouvrés, je vous dis combien la Sécu, les mutuelles et vos patients doivent à votre centre, payeur par payeur et par ancienneté, avec les courriers de réclamation prêts à envoyer. **390 € HT, remboursés si je trouve moins de 1 500 €.**

| Élément | Choix | Pourquoi |
|---|---|---|
| Prix | **390 € HT**, une fois | Égal à un mois du futur abonnement : le client découvre le prix de l'abonnement sans l'avoir signé. |
| Garantie | Remboursé si moins de **1 500 €** sont identifiés | C'est environ 4 fois le prix. Elle retire au client le risque de payer pour rien. |
| Paiement | À la remise du rapport, sous 30 jours | Aucun frein au démarrage. |
| Groupes | 390 € pour le 1er centre, puis 290 € par centre supplémentaire | Pousse à auditer tous les centres d'un coup. |
| Suite | Rapprochement mensuel à 390 € HT par mois et par centre, sans engagement | Transforme l'audit ponctuel en abonnement. |

---

## 2. Déroulé détaillé

### Avant le jour 0, dès l'accord du client
1. Envoyer le **bon de commande** (`05-bon-de-commande-et-facture.md`) et l'**accord de confidentialité** (`04-accord-confidentialite.md`).
2. Envoyer la **liste des exports à préparer** (section 3 ci-dessous).
3. Caler les 2 rendez-vous : le démarrage (45 min) et la remise du rapport (30 min, à J+5).

### Jour 0 : visio de 45 minutes
- Le client partage son écran. Vous ouvrez ensemble les exports et les relevés bancaires.
- Tu notes les **totaux par payeur et par mois**. Si le client accepte, tu récupères les exports **sans identité des patients** (section 3).
- Tu demandes les 10 derniers rejets avec leur motif, en lisant à l'écran.

### Jours 1 à 4 : le rapprochement (chronomètre chaque étape)
| Étape | Ce que tu fais | Temps passé (à noter) |
|---|---|---|
| a | Nettoyer les exports : colonnes, formats de date, montants | … |
| b | Rapprocher factures et paiements par n° de lot ou de facture, puis par montant et date | … |
| c | Classer chaque écart : rejet, paiement partiel, paiement absent, retard | … |
| d | Regrouper par payeur et par ancienneté (0–30, 31–90, plus de 90 jours) | … |
| e | Traduire les motifs de rejet et choisir l'action pour chacun | … |
| f | Rédiger les courriers à partir des modèles de `03-courriers-reclamation.md` | … |
| g | Mettre en forme le rapport (`02-modele-rapport.md`) | … |

> **Ces chronos sont la matière première de l'étape 6.** Les 2 étapes les plus longues seront les premières que le produit automatisera.

### Jour 5 : remise du rapport (30 minutes)
1. Le chiffre clé d'abord : « Vous avez **X €** en attente, dont **Y €** depuis plus de 90 jours. »
2. Les 3 payeurs prioritaires et les courriers à envoyer cette semaine.
3. Les 3 causes de rejet à corriger à la saisie.
4. **La question qui compte :** « Vous voulez que je refasse ce travail chaque mois ? C'est 390 € HT par mois, sans engagement. »
5. Envoyer la facture, ou le remboursement si la garantie s'applique.

---

## 3. Exports à demander au client (sans identité des patients)

Le client garde les noms. Tu ne reçois que des numéros et des montants.

**Fichier 1 : factures émises (3 derniers mois)**
`n° facture` · `n° lot` · `date de l'acte` · `date d'envoi` · `payeur` (Assurance maladie, nom de la mutuelle ou de l'organisme, patient) · `montant facturé` · `statut` (payé / rejeté / en attente) · `motif de rejet`

**Fichier 2 : paiements reçus (3 derniers mois)**
Les relevés bancaires du compte qui reçoit le tiers payant (CSV, Excel ou OFX), ou les relevés de paiement des organismes s'ils sont disponibles.

**À ne jamais recevoir :** les noms et prénoms des patients, le numéro de Sécurité sociale, la date de naissance, les actes en clair ou toute donnée médicale.
Si un fichier en contient, **supprime-le immédiatement** et demande une nouvelle version. L'hébergement de données de santé exige un hébergeur certifié HDS, et tu n'en as pas encore.

---

## 4. Ce que tu ne fais PAS (cadre légal, à faire valider par un avocat)

- **Tu n'envoies pas les réclamations à la place du centre.** Le recouvrement de créances pour le compte d'autrui est une activité réglementée en France. Le centre envoie lui-même les courriers que tu as préparés.
- **Tu ne contactes jamais les patients.**
- **Tu ne télétransmets rien et tu ne corriges aucune facture dans le logiciel du centre.**
- **Tu ne stockes aucune donnée de santé.** Voir la section 3.
- **Point à valider avec l'avocat** (budget 1 à 2 k€) : l'accès d'un prestataire extérieur, même à l'écran, à des données de facturation nominatives au regard du secret professionnel (article L1110-4 du Code de la santé publique). C'est pour cette raison que l'offre privilégie les exports sans identité.

---

## 5. Critères pour passer à l'étape 6 (MVP)

| Critère | Seuil | Si ce n'est pas atteint |
|---|---|---|
| Audits vendus et livrés en 5 jours ouvrés au plus | ≥ 3 | 0 audit vendu après 30 entretiens → **plan B** |
| Audits qui identifient au moins 1 500 € | ≥ 2 sur 3 | La perte d'argent est trop faible : retravailler la promesse sur le temps gagné, sinon plan B |
| Clients qui demandent le suivi mensuel à 390 € | ≥ 1 | Revoir le prix ou la forme du suivi avant de coder |
| Temps passé par audit | Mesuré étape par étape | Définit le périmètre du MVP |

**Si les critères sont remplis :** étape 6. Le MVP automatise d'abord les 2 étapes les plus longues de l'audit, à partir des formats d'export réels que tu auras vus chez tes 3 premiers clients.
