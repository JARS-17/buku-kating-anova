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
            "https://drive.google.com/uc?export=view&id=1_u-IKsluakgB0pT6x8w8_-ZdmLosCqYw",
            "https://drive.google.com/uc?export=view&id=1I6bGV0pG7Xq4bpM0_1ll26fY-KedU5V4",
            "https://drive.google.com/uc?export=view&id=1iU4ZuyVV3aqoge15vG7Jnayp9oVBrNNA",
            "https://drive.google.com/uc?export=view&id=1I65lwz6BRweI9H4sjxOgE_x6FDg1XQsT",
            "https://drive.google.com/uc?export=view&id=1iTKlTZFbEQCk5x98Ri5vTXt6SpVsKBae",
            "https://drive.google.com/uc?export=view&id=1I4B1hMrN_jFf3fb5qocDVl83cIlVMKiW",
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
                "kesan": "Cakep dan Berkarisma",
                "pesan":"Semangat buat TA nya, sukses selalu!"# 1
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
                "pesan":"Tetap semangat dan sukses selalu bang!"# 1
            },
            {   
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Jl.Pagar Alam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "keren, pendengar yang baik",  
                "pesan":"semangat terus kakak!!!"# 1
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
                "pesan":"Semangat untuk ngurus TA dan sukses selalu!! "# 1
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
                "pesan":"Semangat ngurus cuan dan persiapan TA nya!!"# 1
            },
        
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Metro",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nadilaandr26",
                "kesan": "vibes bendahara bgt",  
                "pesan":"Semangat ngasprak dan persiapan TA nya!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "1214500038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Nanya ke Gpt",
                "sosmed": "@trimurniaa_",
                "kesan": "Asik, murah senyum, pendengar yang baik",  
                "pesan":"semangat untuk menjalani hari hari dan persiapan TA nya!!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Membaca dan Menonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Asik, murah senyum",  
                "pesan":"Semangat menjalani hari-hari dan persiapan TA nya!!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Belajar, Nonton film, Tidur",
                "sosmed": "@wlsbn0",
                "kesan": "asik saat mengobrol",  
                "pesan":"semangat menjalani hari-hari dan persiapan TA nya!!"# 1
            },
             {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Drama China",
                "sosmed": "@anisadini10",
                "kesan": "seru dan asik ",  
                "pesan":"semangat menjalani hari-hari dan pesiapan TA nya!!"# 1
            },
             {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Baca Buku",
                "sosmed": "@fer-yulius",
                "kesan": "asik dan baik",  
                "pesan":"semangat terus menjalani hari-harinya dan kuliahnya!!"# 1
            },
             {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Jualan Pancing",
                "sosmed": "@pleurnsh",
                "kesan": "asik dan baik",  
                "pesan":"semangat terus menjalani hari-hari dan kuliahnya !!"# 1
            },
             {
                "nama": "Claudhia Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Tidur",
                "sosmed": "@dylldbee",
                "kesan": "asik dan baik",  
                "pesan":"semangat terus menjalani hari-harinya dan persiapan TA nya !!"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450110",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama dan main kucing",
                "sosmed": "@myrrinn",
                "kesan": "asik dan baik",  
                "pesan":"semangat terus menjalani hari-harinya dan kuliahnya !!"# 1
            },
             {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta,Jawa Tengah",
                "alamat": "Sukarame",
                "hobbi": "Melukis dan Olahraga",
                "sosmed": "@fhrul.pdf",
                "kesan": "asik dan baik",  
                "pesan":"semangat terus menjalani hari-harinya dan persiapan TA nya !!"# 1
            },
             {
                "nama": "Jeremi Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bengong",
                "sosmed": "@jeremi_s_",
                "kesan": "keren banget kak!!",  
                "pesan":"semangat terus menjelani hari-hari dan kuliahnya kakak !!"# 1
            },
             {
                "nama": "Berlinda Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "MDuduk di tepi pantai dambil galauin bintang yang tinggal satu",
                "sosmed": "@berlyynda",
                "kesan": "asik,lucu dan seru",  
                "pesan":"semangat terus menjalani hari-hari dan kuliahnya kakak !!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
