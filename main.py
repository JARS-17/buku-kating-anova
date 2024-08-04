import streamlit as st
# session state agar ketika pindah page tidak berubah data yang tersedia

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
    "Buku Kating/094_Rian Bintang Wijaya.py",
    title="094 - Rian Bintang Wijaya",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/001_Eksanty Febriana.py",
    title="001 - Eksanty Febriana",
    icon=":material/person:",
)

#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa4],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :()")  # Optional: message if not logged in
pg.run()
