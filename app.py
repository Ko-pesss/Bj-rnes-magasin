import streamlit as st
import pandas as pd

# Ladda data
DATA_FILE = "data.csv"

try:
    data = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    data = pd.DataFrame(columns=["Datum", "Linje", "Maskin", "Värde1", "Värde2"])

st.title("Maskinjournal SPINN")

# Filter
st.sidebar.header("Filter")
linje = st.sidebar.multiselect("Linje", options=data["Linje"].unique(), default=data["Linje"].unique())
maskin = st.sidebar.multiselect("Maskin", options=data["Maskin"].unique(), default=data["Maskin"].unique())

# Filtrera data
filtered_data = data[(data["Linje"].isin(linje)) & (data["Maskin"].isin(maskin))]
st.write("Filtrerad Data", filtered_data)

# Lägg till ny data
st.header("Lägg till ny rad")
with st.form("Lägg till rad"):
    datum = st.date_input("Datum")
    linje = st.text_input("Linje")
    maskin = st.text_input("Maskin")
    värde1 = st.number_input("Värde1", step=0.1)
    värde2 = st.number_input("Värde2", step=0.1)
    submitted = st.form_submit_button("Lägg till")

    if submitted:
        new_row = {"Datum": datum, "Linje": linje, "Maskin": maskin, "Värde1": värde1, "Värde2": värde2}
        data = data.append(new_row, ignore_index=True)
        data.to_csv(DATA_FILE, index=False)
        st.success("Ny rad tillagd!")
