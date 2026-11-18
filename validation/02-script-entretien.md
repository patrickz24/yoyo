# Script d'entretien (25 minutes)

**Principe :** tu poses des questions sur ce qui **s'est déjà passé**, tu demandes des **chiffres précis**, et tu ne parles jamais de ton idée avant la fin.
Les marqueurs **[S1]** à **[S5]** renvoient aux 5 seuils de décision. Chaque réponse se reporte dans la colonne indiquée de `suivi-entretiens.csv`.

---

## 0. Ouverture (1 minute)

> « Merci pour votre temps. Je fais une étude sur la façon dont les centres de santé gèrent les paiements du tiers payant, en particulier les rejets et les retards. Je ne vends rien aujourd'hui. Je cherche à comprendre comment ça se passe vraiment. Est-ce que je peux prendre des notes ? À la fin, je vous enverrai la synthèse anonymisée de mes entretiens, si ça vous intéresse. »

## 1. Contexte (3 minutes)

- « Quel est votre rôle exactement ? »
- « Combien de praticiens, combien de sites ? À peu près combien d'actes par mois ? » → `nb_praticiens`, `nb_sites`
- « Quel logiciel utilisez-vous pour la facturation ? Et quelle banque ? » → `logiciel`, `banque`
- « Quelle part de votre chiffre d'affaires passe par le tiers payant ? » → `part_tiers_payant_pct`

## 2. Le dernier problème vécu (5 minutes)

- « **Racontez-moi la dernière fois** qu'un paiement de la Sécu ou d'une mutuelle n'est pas arrivé. »
- Relances possibles :
  - « Comment vous en êtes-vous rendu compte ? »
  - « Qu'avez-vous fait ensuite ? »
  - « Combien de temps ça a pris ? »
  - « Est-ce que l'argent a fini par arriver ? »
- Note **mot pour mot** la phrase la plus forte → `citation_cle`

## 3. Le temps passé [S1] (4 minutes)

- « Qui s'occupe du pointage, c'est-à-dire vérifier ce qui a été payé ? »
- « **Combien d'heures par semaine** ou par mois ? » Convertis en jours par mois (7 h = 1 jour) → `jours_pointage_mois`
- « Pouvez-vous me montrer comment vous faites ? » Un partage d'écran, c'est une mine d'or.

## 4. L'argent en jeu [S2] (4 minutes)

- « Aujourd'hui, **combien d'argent est dû depuis plus de 90 jours** ? Vous pouvez regarder dans votre logiciel ? » → `montant_plus_90j_eur`
- « Sur une année, combien finit par passer en perte ? »
- « Quelles mutuelles ou quels organismes posent le plus de problèmes ? »

> Si la personne répond « je ne sais pas », c'est une information en soi : personne ne pilote ce sujet. Note-le dans `notes`.

## 5. Les outils actuels [S3] (3 minutes)

- « Qu'utilisez-vous pour suivre tout ça : le logiciel, l'outil de la banque, l'expert-comptable, une société de facturation, Excel ? »
- « **Qu'est-ce qui vous agace** le plus dans ce que vous utilisez ? »
- « Avez-vous déjà **payé** pour essayer de régler ce problème ? Combien ? » C'est la preuve qu'il existe un budget.
- Réponse « oui » si la personne décrit des manques concrets → `outil_actuel_insuffisant` (oui/non)

## 6. Les données [S4] (2 minutes)

- « Savez-vous **exporter** la liste des factures et des retours de paiement en Excel ou en CSV ? Qui sait le faire ? »
- « Recevez-vous les relevés bancaires en fichier ? » → `export_possible` (oui/non)

## 7. Engagement [S5] (2 minutes)

N'aborde ce point **que si** les seuils S1 ou S2 sont atteints.

> « Merci, c'est très clair. Je propose un **audit tiers payant**. On regarde ensemble, en visio sur votre écran ou sur des exports **sans noms de patients**, vos 3 derniers mois de factures et de paiements. Sous 5 jours ouvrés, je vous dis combien d'argent vous attend, chez quels payeurs, et je vous prépare les courriers de réclamation. C'est 390 € HT, **remboursés si je trouve moins de 1 500 €** à récupérer. Est-ce qu'on le cale ? »

- Si c'est oui : fixe la date tout de suite → `audit_paye` = oui.
- Si c'est « je dois en parler à… » : demande « Avec qui ? Est-ce qu'on peut faire un point à trois ? »

## 8. Recommandations (1 minute)

- « **Qui d'autre** devrais-je appeler ? Un confrère, un autre centre, votre expert-comptable ? Vous pouvez me présenter ? » → `intros_obtenues` (nombre)

## Clôture

> « Merci. Je vous envoie la synthèse dans 15 jours. »

Dans l'heure qui suit, remplis le CSV et passe la ligne en `statut` = `fait`.

---

## Variantes selon le segment

### E. Groupes de plusieurs centres (DAF, contrôleur de gestion)
- « Comment consolidez-vous le suivi du tiers payant entre vos centres ? Qui le fait, et combien de temps ça prend ? »
- « Quel indicateur suivez-vous ? Délai moyen de paiement ? Taux de rejet ? »
- « Qui décide de l'achat d'un outil de ce type, et sur quel budget ? »

### F. Experts-comptables spécialisés santé
- « Combien de centres de santé ou de professionnels de santé comptez-vous parmi vos clients ? »
- « Qui fait le rapprochement des paiements du tiers payant : vous ou le client ? Combien d'heures par mois et par client ? »
- « Ce temps est-il facturé ? Combien ? »
- « Si un outil faisait gagner ce temps, le recommanderiez-vous ? Le revendriez-vous ? »
- **Demande à la fin : 2 présentations à des clients.**

### G. Sociétés de facturation (facturières)
- « Pour combien de soignants travaillez-vous ? Comment facturez-vous : au forfait ou en pourcentage du chiffre d'affaires ? »
- « Combien de temps passez-vous sur les rejets par client et par mois ? Avec quels outils ? »
- « Qu'est-ce qui vous empêche de prendre plus de clients ? »

### D. Centres de soins infirmiers et ton cousin
- Reprends le script principal, sans le bloc 7 si ton cousin est salarié.
- Insiste sur la question 8 : qui gère la facturation dans sa structure ou dans son réseau ?

---

## Ce qu'il ne faut pas faire

- ❌ « Est-ce que vous utiliseriez un outil qui… ? » Une hypothèse n'engage à rien.
- ❌ Présenter ton idée avant le bloc 7.
- ❌ Répondre aux objections. Note-les, ce sont des données.
- ❌ Récupérer un fichier contenant des noms de patients ou des numéros de Sécurité sociale.
