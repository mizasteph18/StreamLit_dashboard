import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mon App Dashboard", layout="wide")

# Initialisation
if 'filters' not in st.session_state:
    st.session_state.filters = {'cpty': 'gran1', 'overall': 'group1', 'underlying': 'undl1'}

# Sidebar
with st.sidebar:
    st.title("🏠 Navigation")
    page = st.radio("Pages:", ["Accueil", "Process", "Reporting", "Analytics"])
    
    st.title("🎛️ Filtres")
    st.session_state.filters['cpty'] = st.selectbox("Cpty:", ["gran1", "gran2", "gran3"])
    st.session_state.filters['overall'] = st.selectbox("Overall:", ["group1", "group2", "group3"])
    st.session_state.filters['underlying'] = st.selectbox("Underlying:", ["undl1", "undl2", "undl3"])

# Pages
if page == "Accueil":
    st.title("📊 Tableau de Bord")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Performance", "87%", "5%")
    with col2: st.metric("Taux Réussite", "92%", "2%")
    with col3: st.metric("Volume", "1,234", "-3%")
    with col4: st.metric("Efficacité", "78%", "8%")
    
    st.dataframe(pd.DataFrame({
        'Métrique': ['Ventes', 'Profits', 'Clients', 'Conversion'],
        'Valeur': [120, 45, 890, 0.15]
    }))

elif page == "Process":
    st.title("⚙️ Process Management")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("État des Processus")
        st.write("- Validation: ✅ Terminé")
        st.write("- Traitement: 🔄 En cours")
        st.write("- Contrôle: ⏸️ En pause")
    with col2:
        st.subheader("Actions")
        if st.button("🔄 Lancer Processus"): st.success("Démarré!")
        if st.button("📊 Générer Rapport"): st.info("En cours...")

elif page == "Reporting":
    st.title("📈 Reporting")
    fig = px.line(x=[1,2,3,4], y=[10,11,12,13], title="Évolution")
    st.plotly_chart(fig)

st.markdown("---")
st.markdown("*Créé avec Streamlit*")
