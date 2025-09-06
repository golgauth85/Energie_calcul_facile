import streamlit as st


st.title("Home Page")
st.write("Bienvenue sur la page d'accueil !")
with st.expander("Concept"):
    st.write("Cette page vous permet de calculer la consommation de vos appareils électriques.")

types_appareils = [
    "Électroménager de cuisine", 
    "Gros électroménager (hors cuisine)", 
    "Petit électroménager", 
    "Appareils de bureautique et informatique",
    "Appareils audiovisuels et multimédia", 
    "Éclairage",
    "Appareils de loisirs et bien-être",
    "Outillage électrique",
    "Appareils de sécurité",
    "Appareils connectés (IoT)",
    "Autres"
]

# Dictionnaire associant chaque appareil à sa puissance moyenne en watts (W)
puissance_appareils = {
    # Électroménager de cuisine
    "Réfrigérateur": 150,
    "Congélateur": 200,
    "Four": 2500,
    "Plaque de cuisson (induction, vitrocéramique, gaz)": 2000,
    "Micro-ondes": 1000,
    "Lave-vaisselle": 1200,
    "Hotte aspirante": 100,
    "Grille-pain": 1000,
    "Bouilloire": 2000,
    "Robot de cuisine": 500,
    "Mixeur/Blender": 400,
    "Cafetière": 1000,
    "Machine à expresso": 1200,
    "Cuiseur vapeur": 800,
    "Friteuse": 1800,
    "Rice cooker": 500,
    "Sorbetière": 150,
    "Yaourtière": 20,
    "Moulin à café": 150,
    "Balance de cuisine électronique": 5,
    "Ouvre-boîte électrique": 100,
    "Presse-agrumes": 50,
    "Centrifugeuse": 300,
    "Wok électrique": 1500,
    "Barbecue électrique": 2000,
    "Plancha": 2000,

    # Gros électroménager (hors cuisine)
    "Machine à laver": 2000,
    "Sèche-linge": 2500,
    "Lave-linge séchant": 2500,
    "Chauffage électrique": 2000,
    "Climatiseur": 1500,
    "Chauffe-eau": 2000,
    "Pompe à chaleur": 3000,
    "Radiateur à inertie": 1500,
    "Convecteur": 1500,
    "VMC (Ventilation mécanique contrôlée)": 30,

    # Petit électroménager
    "Aspirateur": 800,
    "Aspirateur robot": 30,
    "Fer à repasser": 2000,
    "Central vapeur": 2400,
    "Sèche-cheveux": 2000,
    "Lisseur": 50,
    "Boucleur": 50,
    "Rasoir électrique": 15,
    "Tondeuse à barbe": 10,
    "Brosse à dents électrique": 5,
    "Ventilateur": 50,
    "Purificateur d’air": 50,
    "Humidificateur": 40,
    "Déshumidificateur": 300,
    "Nettoyeur vapeur": 1500,
    "Repasseur vapeur": 1000,
    "Epurileur": 20,
    "Friteuse sans huile": 1500,
    "Machine à pain": 600,
    "Machine à pâtes": 200,
    "Machine à glace pilée": 200,

    # Appareils audiovisuels et multimédia
    "Téléviseur": 150,
    "Box internet": 15,
    "Enceinte connectée": 20,
    "Console de jeu": 200,
    "Lecteur DVD/Blu-ray": 20,
    "Projecteur": 250,
    "Amplificateur audio": 100,
    "Casque audio": 1,
    "Écouteurs sans fil": 5,
    "Caméra numérique": 5,
    "Caméscope": 10,
    "Disque dur externe": 10,
    "Clé USB": 1,
    "Enregistreur numérique": 10,
    "Home cinéma": 300,

    # Appareils de bureautique et informatique
    "Ordinateur fixe": 300,
    "Ordinateur portable": 60,
    "Tablette": 10,
    "Imprimante": 50,
    "Scanner": 20,
    "Photocopieuse": 500,
    "Routeur": 10,
    "Modem": 10,
    "Clavier": 2,
    "Souris": 2,
    "Webcam": 2,
    "Moniteur": 30,
    "Disque dur externe": 10,
    "SSD externe": 5,
    "Onduleur": 500,
    "Chargeur portable": 10,
    "Lampe de bureau LED": 10,

    # Éclairage
    "Lampe LED": 10,
    "Lampe halogène": 60,
    "Lampe fluocompacte": 15,
    "Lustre": 60,
    "Applique murale": 20,
    "Plafonnier": 30,
    "Spot encastrable": 10,
    "Lampe sur pied": 20,
    "Lampe de chevet": 10,
    "Veilleuse": 2,
    "Guirlande lumineuse": 5,
    "Néons": 40,
    "Lampe solaire extérieure": 5,
    "Lampe de bureau": 10,
    "Lampe connectée": 10,

    # Appareils de loisirs et bien-être
    "Téléphone portable": 5,
    "Smartwatch": 1,
    "Bracelet connecté": 1,
    "Liseuse": 2,
    "Appareil photo": 5,
    "Caméra d’action": 5,
    "Drone": 50,
    "Casque VR": 10,
    "Massageur électrique": 30,
    "Sauna infrarouge": 1500,
    "Tapis de course": 500,
    "Vélo d’appartement": 150,
    "Machine à coussin d’air": 100,
    "Appareil de musculation électrique": 200,
    "Jacuzzi": 3000,
    "Diffuseur d’huiles essentielles": 5,
    "Réveil simulateur d’aube": 5,
    "Lampe de luminothérapie": 30,

    # Outillage électrique
    "Perceuse": 500,
    "Visseuse": 200,
    "Ponceuse": 300,
    "Scie électrique": 1000,
    "Scie sauteuse": 500,
    "Scie circulaire": 1200,
    "Tondeuse à gazon": 1500,
    "Taille-haie": 500,
    "Débroussailleuse": 1000,
    "Souffleur de feuilles": 800,
    "Nettoyeur haute pression": 2000,
    "Ponceuse à bande": 500,
    "Rabot électrique": 600,
    "Meuleuse": 800,
    "Cloueuse électrique": 300,
    "Agrafeuse électrique": 100,
    "Pistolet à peinture": 300,
    "Compresseur": 1500,
    "Poste à souder": 2000,
    "Tournevis électrique": 100,
    "Lampe de chantier": 50,

    # Appareils de sécurité
    "Détecteur de fumée": 5,
    "Alarme anti-intrusion": 10,
    "Caméra de surveillance": 10,
    "Interphone": 5,
    "Visiophone": 10,
    "Détecteur de mouvement": 5,
    "Détecteur de monoxyde de carbone": 5,
    "Détecteur de gaz": 5,
    "Serrure connectée": 5,
    "Vidéophone": 10,
    "Clavier codé": 2,
    "Sirène d’alarme": 20,
    "Éclairage de sécurité": 10,
    "Kit de vidéosurveillance": 20,

    # Appareils connectés (IoT)
    "Enceinte intelligente": 10,
    "Thermostat connecté": 5,
    "Ampoule connectée": 10,
    "Prise connectée": 2,
    "Caméra connectée": 10,
    "Sonette connectée": 5,
    "Store connecté": 30,
    "Robot tondeuse": 50,
    "Aspirateur robot": 30,
    "Frigo connecté": 150,
    "Four connecté": 2500,
    "Machine à café connectée": 1200,
    "Station météo connectée": 5,
    "Pèse-personne connecté": 5,
    "Traqueur d’activité": 1,
    "Capteur de porte/fenêtre": 1,
    "Purificateur d’air connecté": 50,
    "Arrosage automatique connecté": 10,

    # Autres
    "Chargeur de téléphone": 10,
    "Chargeur sans fil": 10,
    "Batterie externe": 15,
    "Adaptateur secteur": 5,
    "Multiprise": 0,  # Ne consomme pas en elle-même
    "Pile rechargeable": 1,  # Puissance de charge
    "Chargeur de piles": 5,
    "Transformateur": 5,
    "Alimentation PC": 500,
    "Câbles électriques": 0,  # Ne consomme pas
    "Rallonge": 0,  # Ne consomme pas
    "Paratonnerre": 0,  # Ne consomme pas
    "Testeur électrique": 2,
    "Minuteur programmable": 2,
    "Programmateur de chauffage": 5,
}

appareils_par_type = {
    "Électroménager de cuisine": [
        "Réfrigérateur", "Congélateur", "Four", "Plaque de cuisson (induction, vitrocéramique, gaz)",
        "Micro-ondes", "Lave-vaisselle", "Hotte aspirante", "Grille-pain", "Bouilloire", "Robot de cuisine",
        "Mixeur/Blender", "Cafetière", "Machine à expresso", "Cuiseur vapeur", "Friteuse", "Rice cooker",
        "Sorbetière", "Yaourtière", "Moulin à café", "Balance de cuisine électronique", "Ouvre-boîte électrique",
        "Presse-agrumes", "Centrifugeuse", "Wok électrique", "Barbecue électrique", "Plancha"
    ],
    "Gros électroménager (hors cuisine)": [
        "Machine à laver", "Sèche-linge", "Lave-linge séchant", "Chauffage électrique", "Climatiseur",
        "Chauffe-eau", "Pompe à chaleur", "Radiateur à inertie", "Convecteur", "VMC (Ventilation mécanique contrôlée)"
    ],
    "Petit électroménager": [
        "Aspirateur", "Aspirateur robot", "Fer à repasser", "Central vapeur", "Sèche-cheveux", "Lisseur",
        "Boucleur", "Rasoir électrique", "Tondeuse à barbe", "Brosse à dents électrique", "Ventilateur",
        "Purificateur d’air", "Humidificateur", "Déshumidificateur", "Nettoyeur vapeur", "Repasseur vapeur",
        "Epurileur", "Friteuse sans huile", "Machine à pain", "Machine à pâtes", "Machine à glace pilée"
    ],
    "Appareils audiovisuels et multimédia": [
        "Téléviseur", "Box internet", "Enceinte connectée", "Console de jeu", "Lecteur DVD/Blu-ray",
        "Projecteur", "Amplificateur audio", "Casque audio", "Écouteurs sans fil", "Caméra numérique",
        "Caméscope", "Disque dur externe", "Clé USB", "Enregistreur numérique", "Home cinéma"
    ],
    "Appareils de bureautique et informatique": [
        "Ordinateur fixe", "Ordinateur portable", "Tablette", "Imprimante", "Scanner", "Photocopieuse",
        "Routeur", "Modem", "Clavier", "Souris", "Webcam", "Moniteur", "Disque dur externe", "SSD externe",
        "Onduleur", "Chargeur portable", "Lampe de bureau LED"
    ],
    "Éclairage": [
        "Lampe LED", "Lampe halogène", "Lampe fluocompacte", "Lustre", "Applique murale", "Plafonnier",
        "Spot encastrable", "Lampe sur pied", "Lampe de chevet", "Veilleuse", "Guirlande lumineuse",
        "Néons", "Lampe solaire extérieure", "Lampe de bureau", "Lampe connectée"
    ],
    "Appareils de loisirs et bien-être": [
        "Téléphone portable", "Smartwatch", "Bracelet connecté", "Liseuse", "Appareil photo",
        "Caméra d’action", "Drone", "Casque VR", "Massageur électrique", "Sauna infrarouge",
        "Tapis de course", "Vélo d’appartement", "Machine à coussin d’air", "Appareil de musculation électrique",
        "Jacuzzi", "Diffuseur d’huiles essentielles", "Réveil simulateur d’aube", "Lampe de luminothérapie"
    ],
    "Outillage électrique": [
        "Perceuse", "Visseuse", "Ponceuse", "Scie électrique", "Scie sauteuse", "Scie circulaire",
        "Tondeuse à gazon", "Taille-haie", "Débroussailleuse", "Souffleur de feuilles", "Nettoyeur haute pression",
        "Ponceuse à bande", "Rabot électrique", "Meuleuse", "Cloueuse électrique", "Agrafeuse électrique",
        "Pistolet à peinture", "Compresseur", "Poste à souder", "Tournevis électrique", "Lampe de chantier"
    ],
    "Appareils de sécurité": [
        "Détecteur de fumée", "Alarme anti-intrusion", "Caméra de surveillance", "Interphone", "Visiophone",
        "Détecteur de mouvement", "Détecteur de monoxyde de carbone", "Détecteur de gaz", "Serrure connectée",
        "Vidéophone", "Clavier codé", "Sirène d’alarme", "Éclairage de sécurité", "Kit de vidéosurveillance"
    ],
    "Appareils connectés (IoT)": [
        "Enceinte intelligente", "Thermostat connecté", "Ampoule connectée", "Prise connectée", "Caméra connectée",
        "Sonette connectée", "Store connecté", "Robot tondeuse", "Aspirateur robot", "Frigo connecté",
        "Four connecté", "Machine à café connectée", "Station météo connectée", "Pèse-personne connecté",
        "Traqueur d’activité", "Capteur de porte/fenêtre", "Purificateur d’air connecté", "Arrosage automatique connecté"
    ],
    "Autres": [
    "Chargeur de téléphone", "Chargeur sans fil", "Batterie externe", "Adaptateur secteur", "Multiprise",
    "Pile rechargeable", "Chargeur de piles", "Transformateur", "Alimentation PC", "Câbles électriques",
    "Rallonge", "Paratonnerre", "Testeur électrique", "Minuteur programmable", "Programmateur de chauffage"
    ]
}

liste_appareils = []

col_gauche, col_droite = st.columns(2)
with col_droite:
    with st.expander("Ajouter un appareil manuellement"):
        nom_appareil = st.text_input(
            "Nom de l'appareil", 
            key="manuel_appareil_nom"
        )
        type_appareil = st.selectbox(
            "Type de l'appareil", 
            options= types_appareils
        ) 

        # Sélection dynamique des appareils en fonction du type choisi
        appareils_disponibles = appareils_par_type.get(type_appareil, [])
        appareil = st.selectbox(
            "Appareil",
            options=appareils_disponibles,
            key="appareil"
        )
        
        # Puissance de cet appareil
        puissance_propose = puissance_appareils[appareil]
        pussance = st.number_input(
            "Puissance (W)",
            value= puissance_propose
        )
        st.button(
            "Ajouter l'appareil dans ma maison",
                     icon=":material/check:"
        )

prix_kwh = st.number_input("Prix électricité (€/kWh)", value= 0.15 )