# Landing page « Encaissé »

`index.html` est la page complète. Elle n'a aucune dépendance en dehors des polices Google Fonts. Un aperçu est publié en privé sur claude.ai.

## 1. À personnaliser (bloc `CONFIG` en bas du fichier)

| Clé | À remplir avec |
|---|---|
| `fondateur`, `bio` | Ton nom et 2 phrases sur ton parcours (banque, santé) |
| `email`, `telephone` | Ton contact professionnel |
| `endpoint` | L'URL d'un service de formulaire qui accepte un POST JSON (par exemple un formulaire Formspree, ou ta future API). **Si ce champ est vide**, le visiteur obtient sa demande sous forme de texte à copier et à t'envoyer par e-mail. |
| `calendrier` | Ton lien de prise de rendez-vous (Cal.com, Calendly…). Vide : le bouton reste masqué. |
| `editeur`, `hebergeur` | **Mentions légales obligatoires** (loi LCEN) : raison sociale, SIREN, adresse, directeur de la publication, hébergeur |

## 2. Avant la mise en ligne

- **Le nom « Encaissé » est provisoire.** Vérifie qu'il est disponible sur la base de marques de l'INPI (data.inpi.fr), ainsi que le nom de domaine, avant d'acheter quoi que ce soit.
- Remplace toutes les mentions « À compléter ».
- Les 3 chiffres de la section « Le constat » citent leur source. Garde ces sources si tu modifies les chiffres.
- **N'ajoute jamais de faux témoignages ni de faux logos de clients.** Ajoute de vrais témoignages après tes premiers audits, avec l'accord écrit des personnes.

## 3. Mettre en ligne gratuitement (au choix)

- **Netlify Drop** : glisse le dossier `site/` sur app.netlify.com/drop. Tu obtiens une URL en 30 secondes, et tu peux brancher ton domaine ensuite.
- **Cloudflare Pages** : crée un projet relié à ce dépôt GitHub, avec `site` comme dossier de sortie.
- **GitHub Pages** : GitHub Pages ne sert que la racine du dépôt ou un dossier `docs/`. Copie `site/index.html` dans `docs/`, puis active Pages dans les paramètres du dépôt.

## 4. Comment l'utiliser à l'étape 4

La page sert surtout de **preuve de sérieux** dans tes messages. Ajoute son lien en signature de tes e-mails et dans ton profil LinkedIn. Pendant la phase de validation, **ne la mets pas en avant dans le message d'approche** : on demande 20 minutes d'échange, pas un achat.
