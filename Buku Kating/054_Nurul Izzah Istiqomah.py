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
            "Departemen MEDCRAF",
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

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal": "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi": "Dengerin bintang nyanyi",
                "sosmed": "@anissalutfi_",
                "kesan": "kakaknya keren banget",
                "pesan": "Semangat kuliahnya kak, jangan lupa belajar tiap hari", 
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "DEPARTEMEN PSDA":
    def Psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandr99",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari", 
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Owen Kost",
                "hobbi": "Bernafas",
                "sosmed": "",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450123",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Menonton",
                "sosmed": "",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            },
            {
                "nama": "",
                "nim": "122450123",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Owen Kost",
                "hobbi": "Bernafas",
                "sosmed": "",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            },
            {
                "nama": "",
                "nim": "122450123",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Owen Kost",
                "hobbi": "Bernafas",
                "sosmed": "",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            },
            {
                "nama": "",
                "nim": "122450123",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Owen Kost",
                "hobbi": "Bernafas",
                "sosmed": "",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            },
            {
                "nama": "",
                "nim": "122450123",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Owen Kost",
                "hobbi": "Bernafas",
                "sosmed": "",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            },
            {
                "nama": "",
                "nim": "122450123",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Owen Kost",
                "hobbi": "Bernafas",
                "sosmed": "",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            },
            {
                "nama": "",
                "nim": "122450123",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Owen Kost",
                "hobbi": "Bernafas",
                "sosmed": "",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Psda()

elif menu == "Departemen MedKraf":

    def Medkraf():
        gambar_urls = [
         
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "wayylaja",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang",
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Manis bangett kakk",
                "pesan": "Semangat ya kak, tetap ramah", 
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "Senang bisa belajar dari kakak",
                "pesan": "Semangat kuliahnya kak", 
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": " 121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": " @dino_kiper",
                "kesan": "Sangat menyenangkan dan bermanfaat",
                "pesan": "Semangat fotonya bang", 
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "terimakasih atas insightnya bang",
                "pesan": "Semangat desainnya bang", 
            },
            {
                "nama": "Cintya  Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Suka banget sama outfit kakak, cocok banget di divisi media & konten",
                "pesan": "semangat kuliahnya kak", 
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " 122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "senang bisa belajar dari kakak",
                "pesan": "Sampai ketemu lagi di kampus ya,kak", 
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "kakak keren banget",
                "pesan": "terimakasih atas sharing nya", 
            },
            {
                "nama": "Patricia Leondra Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "kakaknya cantik banget",
                "pesan": "Makasih ya kak, sudah mau berbagi ilmu", 
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Terimakasih sharing ilmunya kak",
                "pesan": "Semangat kuliahnya kak", 
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Terimakasih atas insightnya kak",
                "pesan": "semangat kuliahnya kak", 
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Senang bisa belajar dari abang",
                "pesan": "Semangat kuliahnya bang", 
            },
            {
                "nama": "Nasywa Nur Afifah ",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Wawancaranya sangat menginspirasi",
                "pesan": "semangat kuliahnya kak", 
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Terimakasih bang, saya belajar banyak",
                "pesan": "semangat kuliahnya bang", 
            },
             {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "abangnya ramah banget",
                "pesan": "semangat ngaspraknya bang", 
            },
             {
                "nama": "Hermawan Manurung ",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani) ",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Lucu banget bang",
                "pesan": "semangat kuliahnya bang", 
            },
             {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Sharing ilmunya keren banget kak",
                "pesan": "Semangat kuliahnya kak", 
            },
             {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "kakaknya ramah banget",
                "pesan": "Semangat kuliahnya kak", 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen MIKFES":

    def Mikfes():
        gambar_urls = [
        ] 
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21 Tahun",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21 Tahun",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": " Memasak",
                "sosmed": "@anovavona",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": " Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": " 20",
                "asal": "Tulang Bawang",
                "alamat": " Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20 Tahun",
                "asal": "Bekasi",
                "alamat": "Teluk Betung ",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": " 122450031",
                "umur": "19 Tahun",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame  ",
                "hobbi": "Main Game",
                "sosmed": "@mregiiii_",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21 Tahun",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira ",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing ",
                "nim": "121450107",
                "umur": "20 Tahun",
                "asal": "Jakarta",
                "alamat": "Kemiling ",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21 Tahun",
                "asal": "Bukittinggi",
                "alamat": "Korpri ",
                "hobbi": " ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21 Tahun",
                "asal": " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20 Tahun",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Main Game",
                "sosmed": "@dindanababan_",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20 Tahun",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20 Tahun",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": " 122450072",
                "umur": "20 Tahun",
                "asal": "Palembang",
                "alamat": "Belwis ",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": " Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": " Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20 Tahun",
                "asal": " Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20 Tahun",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr ",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20 Tahun",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama ",
                "sosmed": "@pratiwifebiya",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20 Tahun",
                "asal": "Lampung",
                "alamat": "Karang Anyar ",
                "hobbi": " Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21 Tahun",
                "asal": "Banten",
                "alamat": " Sukarame",
                "hobbi": " Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "-",
                "pesan": "-",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Mikfes()

elif menu == "DEPARTEMEN EKSTERNAL ":
    def Eksternal():
        gambar_urls = [
         
        ]
        data_list = [
            {
                "nama": "Yusuf Fikri",
                "nim": "121450010",
                "umur": "22",
                "asal": "Jakarta",
                "alamat": "Jakarta",
                "hobbi": "Baca",
                "sosmed": "@yusuf_fikri",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari", 
            },
            {
                "nama": "Yusuf Fikri",
                "nim": "121450010",
                "umur": "22",
                "asal": "Jakarta",
                "alamat": "Jakarta",
                "hobbi": "Baca",
                "sosmed": "@yusuf_fikri",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Eksternal()
elif menu == "DEPARTEMEN INTERNAL ":
    def Internal():
        gambar_urls = [
         
        ]
        data_list = [
             {
                "nama": "Dimas rizky ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal": "Pamulang",
                "alamat": "Way kandis",
                "hobbi": "Manjat tower sutet",
                "sosmed": "@dimzrky",
                "kesan": "Berkharisma banget",
                "pesan": "Semangat nyusun TA nya bang dimas", 
            },
            {
                "nama": "Catherine firdhasari maulina sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@chatherine.sinaga",
                "kesan": "kakanya ramah bintang 100",
                "pesan": "Semangat berproses kak",
            },    
            {
                "nama": "M. Akbar resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Memelihara dino",
                "sosmed": "@akbar_resdika",
                "kesan": "Kelihatannya baik (emot senyum)",
                "pesan": "Semangat nyusun TA bang",
            },
            {
                "nama": "Rani puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@ranipu",
                "kesan": "Kakak baik",
                "pesan": "Selalu bermanfaat untuk orang sekitar ya kak",
            },
            {
                "nama": "Rendra eka prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan lapas raya",
                "hobbi": "nulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Ramah bintang 1000",
                "pesan": "Semoga jadi pribadi yang lebih baik lagi ",
            },
            {
                "nama": "Salwa farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan raya",
                "hobbi": "ngeliat cogan",
                "sosmed": "@slwfhn_694",
                "kesan": "Cantik bangett",
                "pesan": "semangat kuliahnya kak",
            },
            {
                "nama": "Ari sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung barat",
                "alamat": "Labuhan ratu",
                "hobbi": "Main futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "keren banget abangnya",
                "pesan": "semangat kuliahnya bang ari",
            },
            {
                "nama": "Azizah kusumah putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Ramah bangett",
                "pesan": "Semangkaaa semangat kakak!!!",
            },
            {
                "nama": "Meira listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan raya",
                "hobbi": "Menghalu",
                "sosmed": "@meiraln",
                "kesan": "Baik bangett",
                "pesan": "Semangat kakk!!!",
            },
            {
                "nama": "Rendi alexander hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost gunawan",
                "hobbi": "Menyanyi",
                "sosmed": "@alexanderr",
                "kesan": "Baik bangett",
                "pesan": "jangan pentang menyerah,selalu berusaha",
            },
            {
                "nama": "Renta siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera utara",
                "alamat": "Gerbang barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Keren banget",
                "pesan": "selalu semangat kakak ",
            },
            {
                "nama": "Yosia lehare banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Dairi, Sumatera utara",
                "alamat": "Perum griya indah",
                "hobbi": "Bawa motor pakai kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Baik bangett",
                "pesan": "semangat kakak!!!",
            },
            {
                "nama": "Josua panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal": "Pematang siantar",
                "alamat": "Gya kost",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "sangat soft spoken",
                "pesan": "semangat kuliah bang",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Internal()
elif menu == "DEPARTEMEN SSD ":
    def Ssd():
        gambar_urls = [
         
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "17 +",
                "asal": "Sidikalang",
                "alamat": "Lapas",
                "hobbi": "Nyari Hobi",
                "sosmed": "@andrialgaol",
                "kesan": "Public speakingnya bagus bangett",
                "pesan": "Semangat cari duitnya bang", 
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Metro",
                "hobbi": "Nonton film",
                "sosmed": "@adistisa_",
                "kesan": "Keren banget kak",
                "pesan": "Semangat kuliahnya kak",
            }
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung",
                "sosmed": "@zhjung",
                "kesan": "seru banget kakaknya",
                "pesan": "Menjadi pribadi yang lebih baik kedepannya",
            }
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "TB 3 Asrama",
                "hobbi": "Belajar",
                "sosmed": "@dananghk_",
                "kesan": "abangnya keren banget menginsprirasi",
                "pesan": "Semangat ngaspraknya bang",
            }
            {
                "nama": "Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel__julio",
                "kesan": "Abangnya ramah banget",
                "pesan": "Semangat abang kapo",
            }
            {
                "nama": "Nabilah Andika Fitriani",
                "nim": "121450129",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilaafrn",
                "kesan": "Sharing ilmunya keren banget",
                "pesan": "Semangat kuliahnya kak",
            }
            {
                "nama": "Alvia Asrinda Br.Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": "Terimakasih insightnya kak",
                "pesan": "Semangat kuliahnya kak",
            }
            {
                "nama": "Dhafin Razaka Luthfia",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jalan nangka 1",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqri3",
                "kesan": "Terimakasih ilmunya kak",
                "pesan": "Semangat kuliahnya kak",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Ssd()

# Tambahkan menu lainnya sesuai kebutuhan
