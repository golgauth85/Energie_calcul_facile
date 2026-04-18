import streamlit as st
import pandas as pd
from data import puissance_appareils, types_appareils, appareils_par_type, duree_utilisation_appareils

# Configuration de la page
st.set_page_config(page_title="Calculateur Consommation", layout="wide")

# --- INITIALISATION DES DONNÉES (Session State) ---
if 'liste_appareils' not in st.session_state:
    st.session_state.liste_appareils = []


st.title("⚡ Home Energy Calculator")
st.write("Calculez la consommation de vos appareils électriques en temps réel.")

with st.expander("ℹ️ Aide & Concept"):
    st.write("Ajoutez vos appareils pour estimer votre coût horaire.")

col_gauche, col_droite = st.columns([1, 1])

with col_gauche:
    st.subheader("Paramètres")
    prix_kwh = st.number_input("Prix électricité (€/kWh)", value=0.22, step=0.01)

with col_droite:
    with st.expander("➕ Ajouter un appareil", expanded=True):
        type_choisi = st.selectbox("Catégorie", options=types_appareils)
        
        # Filtre les appareils selon la catégorie
        appareils_dispos = appareils_par_type[type_choisi]
        appareil_nom_auto = st.selectbox("Modèle d'appareil", options=appareils_dispos)
        
        nom_perso = st.text_input("Nom personnalisé (ex: Salon, Cuisine)", value=appareil_nom_auto)
        
        # Puissance suggérée
        puissance_suggeree = puissance_appareils.get(appareil_nom_auto, 0)
        puissance_finale = st.number_input("Puissance (Watts)", value=puissance_suggeree)
    
        # Durée d'utilisation suggérée
        duree_suggeree = duree_utilisation_appareils.get(appareil_nom_auto, 0)
        duree_utilisation = st.number_input("Durée d'utilisation (heures)", value=duree_suggeree)

        if st.button("Ajouter à ma liste", type="primary"):
            nouvel_appareil = {
                "Nom": nom_perso,
                "Catégorie": type_choisi,
                "Puissance (W)": puissance_finale,
                "Durée (h)": duree_utilisation
            }
            
            st.session_state.liste_appareils.append(nouvel_appareil)
            st.toast(f"{nom_perso} ajouté !", icon="✅")

st.divider()
st.subheader("📋 Récapitulatif de la maison")

if st.session_state.liste_appareils:
    df = pd.DataFrame(st.session_state.liste_appareils)
    
    # Consommation en kWh par jour = (Puissance en W / 1000) * Durée en h 
    df["Conso / Jour (kWh)"] = (df["Puissance (W)"] / 1000) * df["Durée (h)"]
    df["Coût / Jour (€)"] = df["Conso / Jour (kWh)"] * prix_kwh
    
    st.dataframe(df, use_container_width=True)
    
    conso_totale_jour = df["Conso / Jour (kWh)"].sum()
    cout_total_jour = df["Coût / Jour (€)"].sum()
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Consommation Totale / Jour", f"{conso_totale_jour:.2f} kWh")
    m2.metric("Coût Total / Jour", f"{cout_total_jour:.2f} €")
    m3.metric("Coût Estimé / An", f"{cout_total_jour * 365:.2f} €")

    if st.button("🗑️ Vider la liste"):
        st.session_state.liste_appareils = []
        st.rerun()
else:
    st.info("Votre liste d'appareils est vide. Commencez par en ajouter un ci-dessus.")