import streamlit as st

# Set the logged_in state to True automatically
st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/016_Kemas Veriandra Ramadhan.py",
    title="016 - Kemas Veriandra Ramadhan",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/066_Cintya Bella.py",
    title="066 - Cintya Bella",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/094_Rian Bintang Wijaya.py",
    title="094 - Rian Bintang Wijaya",
    icon=":material/person:",
)

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

# Automatically navigate to the dashboard if logged in
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3],
            "Try Me !!": [search, history],
        }
    )
else:
    st.write("You are not logged in.")  # Optional: message if not logged in


pg.run()
