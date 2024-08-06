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
    "Buku Kating/020_Try Yani Rizki Nur Rohmah.py",
    title="020 - Try Yani Rizki Nur Rohmah",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/001_Eksanty Febriana.py",
    title="001 - Eksanty Febriana",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/117_Anwar Muslim.py",
    title="117 - Anwar Muslim",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/014_Deva Anjani Khayyuninafsyah.py",
    title="014 - Deva Anjani Khayyuninafsyah",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/103_Rut Junita Sari Siburian.py",
    title="103 - Rut Junita Sari Siburian",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

