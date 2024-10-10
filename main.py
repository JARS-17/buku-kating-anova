import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/012_Anggi Puspita Ningrum.py",
    title="012 - Anggi Puspita Ningrum",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/023_Dharu Cahyoaji Sasongko.py",
    title="023 - Dharu Cahyoaji Sasongko",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/028_Donna Maya Puspita.py",
    title="028 - Donna Maya Puspita",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/054_Nurul Izzah Istiqomah.py",
    title="054 - Nurul Izzah Istiqomah",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/073_Monica Patricia Tanjung.py",
    title="073 - Monica Patricia Tanjung",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/085_Juesi Apridelia Saragih.py",
    title="085 - Juesi Apridelia Saragih",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/092_Nadia Faraj Alyafaatin Simbolon.py",
    title="092 - Nadia Faraj Alyafaatin Simbolon",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/094_Tanty Widiyastuti.py",
    title="094 - Tanty Widiyastuti",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/098_Rakha Rabbani.py",
    title="098 - Rakha Rabbani",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/103_Ginda Fajar Riadi Marpaung.py",
    title="103 - Ginda Fajar Riadi Marpaung",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/108_Citra Agustin.py",
    title="108 - Citra Agustin",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/112_Cindy Laura Manik.py",
    title="112 - Cindy Laura Manik",
    icon=":material/person:",
)
Mahasiswa13 = st.Page(
    "Buku Kating/121_Ahmad Farhan Ghani.py",
    title="121 - Ahmad Farhan Ghani",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12, Mahasiswa13],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

