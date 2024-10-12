import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
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

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KaVC9QuVfyvtaPNSoGrG19BlFjZCf2ff",
            "https://drive.google.com/uc?export=view&id=1KYsZsZvUfAY588YYhooWT3ZwWC7t-rOk",
            "https://drive.google.com/uc?export=view&id=1K4GadUDULQUp1yP8OpxSiMgobVOA_3WG",
            "https://drive.google.com/uc?export=view&id=1KXpeujwgQbVIwp6-AyUMcfi4oGv6qSii",
            "https://drive.google.com/uc?export=view&id=1KDp3BF5ygMAx6XY8Y1ELQFrGsh2Y4gO8",
            "https://drive.google.com/uc?export=view&id=1KMf2LZ6bTvrtx8H2fvlyzp2h-T_bT7hL",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450042",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Jl.Pulau Damar",
                "hobbi": "Dengerin Musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Berkharisma dan Menginspirasi",  
                "pesan":"Semangat buat TA nya, sehat selalu!"# 1
            },
            {   
                "nama": "Pandra Insani Putra Anwar",
                "nim": "121450147",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main Gitar",
                "sosmed": "@pandrainsani27",
                "kesan": "Keren banget dan Insight full",  
                "pesan":"Semangat bang !!!, tetap ganteng -juesi"# 1
            },
            {   
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Jl.Pagar Alam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "keren banget kak",  
                "pesan":"semangat ngaspraknya kak !!!"# 1
            },
        
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Nangka 4",
                "hobbi": "Dengerin Bg Pandra Main Gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Cantik, pendengar yang baik ",  
                "pesan":"Terimakasih udah support kami"# 1
            },
        
            {   
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@htrpdla",
                "kesan": "cantik",  
                "pesan":"Semangat ngurus cuannya"# 1
            },
        
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Metro",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nadilaandr26",
                "kesan": "vibes bendaharanya kerasa bgt",  
                "pesan":"Semangat ngasprak strukdatnya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1P4z6MT-y-eJwKRUTenuTee-pO0er3jXn",
            "https://drive.google.com/uc?export=view&id=1PWPFbfuRA7dlP6aouo0KL6fxf7F1KZS6",
            "https://drive.google.com/uc?export=view&id=1PpVVepegQ9-DZeWBqAfbf6OsYMNeFV0f",
            "https://drive.google.com/uc?export=view&id=1PRAwMW5swMpXvMVbESTG3Fcw6E3I9P8G",
            "https://drive.google.com/uc?export=view&id=1OyqQcdq62GWD9AcxvzESL0fUbTd6FybK",
            "https://drive.google.com/uc?export=view&id=1PDEO3RyItAtib5NX_qgZHXIQK659u59n",
            "https://drive.google.com/uc?export=view&id=1PI-VpSelYlw0OGmhov00jGyD8jINhyEe",
            "https://drive.google.com/uc?export=view&id=1P0OSys_xyA-VsgbPUC1Bmrwgz98OjghL",
            "https://drive.google.com/uc?export=view&id=1PsDPuYyc5qdyrKtPYCL-QtDh1AEpbWjB",
            "https://drive.google.com/uc?export=view&id=1Ov7RoO9jul3WxOMsC2da76V_GLO8mHMa",
            "https://drive.google.com/uc?export=view&id=1PVkwyIDeUhNUFSXj_WRey9q-ovnjkrNn",
        ]
        data_list = [
             {
                "nama": "Tri murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden saleh",
                "hobbi": "Nanya ke gpt",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak cantik asprak alpro RA",  
                "pesan":"semangat ngaspraknya kakak !!!"
            },
            {
                "nama": "Annisa cahyani surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangsel",
                "alamat": "Way huwi",
                "hobbi": "Membaca, nonton",
                "sosmed": "@anisacahyanisurya",
                "kesan": "Kakak nya cantik banget",  
                "pesan":"semoga TA nya lancar kakkk !!!"# 1
            },
            {
                "nama": "Wulan sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden saleh",
                "hobbi": "Belajar, nonton film, tidur",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak pasti orang baik kannn",  
                "pesan":"semoga dilancarkan dan dimudahkan segala urusannya ya kak!!!"# 1
            },
            {
                "nama": "Anisa dini amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati agung",
                "hobbi": "Nonton drachin",
                "sosmed": "@anisadini10",
                "kesan": "Waktu ngomongin hobinya, kakaknya keliatan seneng bgt",  
                "pesan":"semangat maraton drachinnya kak !!!"# 1
            },
            {
                "nama": "Feriyadi yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera selatan",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya keren",  
                "pesan":"semangat menjalani semester 5 bang!!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Jualan pancing",
                "sosmed": "@fleurnsh",
                "kesan": "Kakaknya lucu",  
                "pesan":" Semangat kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Claudhia Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Tidur",
                "sosmed": "@dylebee",
                "kesan": "Seru bgt ngobrol sama kakak",  
                "pesan":" Semangat berproses kak!!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450110",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama, main kucing",
                "sosmed": "@myrrinn",
                "kesan": "ucul kakaknya,tinngi lagi",  
                "pesan":"semangat berhibernasinya kak !!!"# 1
            },
            {
                "nama": "Muhammad fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis, olahraga",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakaknya keren banget",  
                "pesan":"Terus semangat bangg"# 1
            },
            {
                "nama": "Jeremia susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jere ramah bgt orangnya",  
                "pesan":"semangat kuliahnya bang !!!"# 1
            },
            {
                "nama": "Berliana enda putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera barat",
                "alamat": "Way huwi",
                "hobbi": "Duduk di tepi pantai sambil galauin bintang yang tinggal satu",
                "sosmed": "@berlyyanda",
                "kesan": " kakaknya lucuu dan seruu",  
                "pesan":"Tetap semangat, jangan menyerah!!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
