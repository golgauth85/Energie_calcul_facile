# 📌 À propos du projet

Ce projet est une application web développée avec **Streamlit** qui permet aux utilisateurs de :
- **Lister** leurs appareils électriques par catégorie.
- **Estimer** la consommation en kWh de chaque appareil.
- **Visualiser** l'impact de chaque appareil sur la facture d'électricité.
- **Optimiser** leur consommation en identifiant les appareils les plus énergivores.

🔗 **Lien vers l'application** : [À déployer](https://share.streamlit.io/) (à remplacer par ton lien une fois déployé).

---

## 🛠 Fonctionnalités

✅ **Base de données intégrée** : Puissance moyenne de plus de 100 appareils courants.
✅ **Interface intuitive** : Sélection par catégorie et appareil.
✅ **Calcul automatique** : Consommation en kWh/jour, kWh/mois, kWh/an.
✅ **Personnalisation** : Ajout manuel d'appareils et de leur puissance.
✅ **Simulations** : Estimation du coût en fonction du prix du kWh.
✅ **Conseils** : Recommandations pour réduire la consommation.

---

## 📦 Installation

### Prérequis
- Python 3.8 ou supérieur
- Pip (gestionnaire de paquets Python)
- Streamlite

### Étapes

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/golgauth85/Energie_calcul_facile.git
   cd Energie_calcul_facile
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application** :
   ```bash
   streamlit run app.py
   ```

4. **Accéder à l'application** :
   Ouvrir [http://localhost:8501](http://localhost:8501) dans ton navigateur.

---

## 📂 Structure du projet

```
Energie_calcul_facile/
├── Home.py                # Page d'accueil et calculateur principal
├── requirements.txt       # Dépendances Python
├── README.md              # Ce fichier
└── data/                  # (Optionnel) Fichiers de données supplémentaires
```

---

## 💡 Utilisation

1. **Sélectionner un type d'appareil** (ex : Électroménager de cuisine).
2. **Choisir un appareil** dans la liste proposée.
3. **Indiquer la durée d'utilisation** quotidienne (en heures).
4. **Visualiser la consommation** en kWh et le coût estimé.
5. **(Optionnel)** Ajouter un appareil personnalisé.

---
## 📊 Exemple de sortie

| Appareil         | Puissance (W) | Durée (h/jour) | Consommation (kWh/mois) | Coût mensuel (€) |
|------------------|---------------|----------------|-------------------------|------------------|
| Réfrigérateur    | 150           | 24             | 108                     | 16,20            |
| Four             | 2500          | 1              | 75                      | 11,25            |
| **Total**        | -             | -              | **183**                 | **27,45**        |

---

## 🔧 Personnalisation

- **Modifier les puissances** : Éditer le dictionnaire `puissance_appareils` dans `Home.py`.
- **Ajouter des catégories** : Mettre à jour la liste `types_appareils` et le dictionnaire `appareils_par_type`.
- **Changer le prix du kWh** : Modifier la variable `prix_kwh` dans le code (par défaut : 0,15 €/kWh).

---

## 📈 Données techniques

- **Source des puissances** : Moyennes basées sur des données constructeurs et des études de consommation (ADEME, ENEDIS).
- **Formule de calcul** :
  ```
  Consommation (kWh) = (Puissance (W) × Durée (h)) / 1000
  Coût (€) = Consommation (kWh) × Prix du kWh
  ```

---

## 🚀 Déploiement

Pour déployer l'application en ligne (ex : Streamlit Cloud) :
1. Créer un compte sur [Streamlit Community Cloud](https://share.streamlit.io/).
2. Lier ton dépôt GitHub.
3. Configurer le déploiement depuis la branche `main`.

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Pour participer :
1. Fork le projet.
2. Créer une branche (`git checkout -b feature/ma-nouvelle-fonctionnalité`).
3. Commit tes changements (`git commit -m "Ajout d'une nouvelle fonctionnalité"`).
4. Push vers la branche (`git push origin feature/ma-nouvelle-fonctionnalité`).
5. Ouvrir une Pull Request.

---
## 📜 Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENCE](LICENCE) pour plus de détails.

---
## 🙌 Remerciements

- [Streamlit](https://streamlit.io/) pour le framework.
- [ADEME](https://www.ademe.fr/) pour les données de référence.
- La communauté open-source pour les outils et bibliothèques utilisés.

---
## 📧 Contact

Pour toute question ou suggestion, contactez-moi via :
- **GitHub** : [@golgauth85](https://github.com/golgauth85)

---
⚡ **Réduisez votre empreinte énergétique, un kWh à la fois !** ⚡