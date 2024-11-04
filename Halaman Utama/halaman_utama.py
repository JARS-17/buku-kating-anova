import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">ANOVA, yang merupakan singkatan dari "Analysis of Variance," adalah nama
                    kelompok yang menonjolkan semangat eksplorasi, analisis, dan ketepatan dalam sebuah kompetisi. Secara statistik,
                    ANOVA adalah metode yang digunakan untuk menguji perbedaan rata-rata antar beberapa kelompok. Dalam konteks 
                    kelompok ini, ANOVA mencerminkan semangat dalam mengidentifikasi kekuatan unik dari setiap anggota dan menyatukannya
                    menjadi keunggulan bersama.
                    .</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1ygUy8u7fPUpqIAmDgxpz_l_QWkw6yu15"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Seperti konsep statistiknya, ANOVA berfokus pada tiga prinsip utama: analisis mendalam, kerja sama yang solid, dan 
                    pembuktian keterampilan melalui data dan hasil nyata. Kelompok ANOVA terdiri dari anggota-anggota yang ahli dalam 
                    berkolaborasi, berpikir kritis, dan menghadapi tantangan dengan strategi yang matang. ANOVA siap mengatasi berbagai 
                    tantangan dengan menggabungkan kreativitas, logika, dan ketelitian untuk mencapai tujuan akhir. Filosofi ANOVA adalah 
                    bahwa keberhasilan sebuah tim tercapai melalui penggabungan perbedaan, di mana setiap anggota berkontribusi untuk menciptakan 
                    hasil yang lebih kuat dan berimbang.
                    .</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JXqN42MkMcxDevd7qpfGZAlgX73R5dSi",
            "https://drive.google.com/uc?export=view&id=1JCUYSnIYQwjzbN4CuF6CE3zuga0ON06k",
            "https://drive.google.com/uc?export=view&id=1JMVb_ynrnsH-v3pDjlQDe0a4iQFhqkPz",
            "https://drive.google.com/uc?export=view&id=1JnO8S5NYgv_NYqNywFPNd4I6QGoGoDLl",
            "https://drive.google.com/uc?export=view&id=1LeXWG5AKCWFA-9lIj-kZgRYM4-OEJihI",
            "https://drive.google.com/uc?export=view&id=1JNgCGQ-ie8mdrfiUfDDNVVOMkZkYeX2t",
            "https://drive.google.com/uc?export=view&id=1JaHctj_DJvmiBAZJVJFgnrx_Bzqxpny-",
            "https://drive.google.com/uc?export=view&id=1JdEwqhP0SSZ2HiKRqi32FOu-gY7Y9o0G",
            "https://drive.google.com/uc?export=view&id=1JNf2ZYh2iU3vmBHLto-nQVdSlJK8N-kP",
            "https://drive.google.com/uc?export=view&id=1Jz4UJoX-8BWJJmDwzdiIcjoWkFi_1vqm",
            "https://drive.google.com/uc?export=view&id=1LeWQEBSKX_2EbmxE43X1TYFst6i22IQt",
            "https://drive.google.com/uc?export=view&id=1JnpLFaKQZcxPwV21tZ2fCw0JetBrRqBx",
            "https://drive.google.com/uc?export=view&id=1J_F7BKkHq5PPOKBBOpUHePemXPlziIyy",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "sebagai": "Pak Lurah",
                "nim": "123450103",
                "fun_fact": "suka matcha",
                "motto_hidup": "hidup di momen saat ini dan berinvestasi buat masa depan",
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "sebagai": "Bu Lurah",
                "nim": "123450012",
                "fun_fact": "suka mint choco",
                "motto_hidup": "jangan pernah takut sama bayangan",
            },
            {
                "nama": "Citra Agustin",
                "sebagai": "Bendahara",
                "nim": "123450108",
                "fun_fact": "cannot life without pinterest",
                "motto_hidup": "just living",
            },
            {
                "nama": "Tanty Widiyastuti",
                "sebagai": "Anggota",
                "nim": "123450094",
                "fun_fact": "kalau tidur harus pakai sarung bapak",
                "motto_hidup": "hiduplah seperti larry",
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "sebagai": "Anggota",
                "nim": "123450054",
                "fun_fact": "Bisa makan menu yang sama dalam 1 bulan",
                "motto_hidup": "Don't say you can't before you try",
            },
            {
                "nama": "Donna Maya Puspita",
                "sebagai": "Anggota",
                "nim": "123450028",
                "fun_fact": "Tidak bisa menahan ketawa",
                "motto_hidup": "It costs zero to be kind",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "sebagai": "Anggota",
                "nim": "123450085",
                "fun_fact": "Gak suka kucing",
                "motto_hidup": "When it doubt, just add a little glitter and strut!",
            },
            {
        
                "nama": "AHMAD FARHAN GHANI",
                "sebagai": "Anggota",
                "nim": "123450121",
                "fun_fact": "Suka Berolahraga",
                "motto_hidup": "Believe In Yourself",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "sebagai": "Anggota",
                "nim": "123450023",
                "fun_fact": "anak 06",
                "motto_hidup": "menjalani takdir tuhan",
            },
            {
                "nama": "Cindy Laura Manik",
                "sebagai": "Anggota",
                "nim": "123450112",
                "fun_fact": "gabisa makan pedas",
                "motto_hidup": "hidup itu gabisa ditebak ya",
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "sebagai": "Anggota",
                "nim": "123450092",
                "fun_fact": "suka ghibli",
                "motto_hidup": "Just because it's hard, doesn't mean it's impossible",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "sebagai": "Anggota",
                "nim": "123450073",
                "fun_fact": "sangat tidak suka cicak",
                "motto_hidup": "True success is becoming true self",
            },
            {
                "nama": "Rakha Rabani",
                "sebagai": "Anggota",
                "nim": "123450098",
                "fun_fact": "3 periode",
                "motto_hidup": "Dikatakan benar juga tidak salah",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
