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
            "https://drive.google.com/uc?export=view&id=1nJNzJ4_GnFKh-f09CLh_VfvTn0_rryV-",
            "https://drive.google.com/uc?export=view&id=1_aFB_x-ut6-CObYMTcPQ9k8veEE1gDS2",
            "https://drive.google.com/uc?export=view&id=1xZ1E67k3eMQEynERjYg0W9RkFZiYBZ_y",
            "https://drive.google.com/uc?export=view&id=1Oc5-DLSDOJiuWDHRiezyRBUk7GoUrkyR",
            "https://drive.google.com/uc?export=view&id=18zzttrggsfHBAYENQC_So7LTwpQSuReU",
            "https://drive.google.com/uc?export=view&id=1S4f4xnM-VRHVF0gJ96ohCjp5v8cg7GII",
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
                "kesan": "ramah dan asik",  
                "pesan":"Semangat buat TA nya bang, sehat selalu!"
            },
            {  
                "nama": "Pandra Insani Putra Anwar",
                "nim": "121450147",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main Gitar",
                "sosmed": "@pandrainsani27",
                "kesan": "Keren dan teladan",  
                "pesan":"Jangan lupa istirahat bang!"
            },
            {   

                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Jl.Pagar Alam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Asyik diajak diskusi",  
                "pesan":"semangat ngasprak strukdatnya kak !!!"# 1
            },

            {  

                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Nangka 4",
                "hobbi": "Dengerin Bg Pandra Main Gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Keliatan care sama kita",  
                "pesan":"Terimakasih kak udah support kami"# 1
            },
        
            {   
               
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@htrpdla",
                "kesan": "Banyak ilmu dari kakak",  
                "pesan":"Semangat ngurus cuannya kak"# 1
            },
        
            {

                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Metro",
                "hobbi": "Membaca",
                "sosmed": "@nadilaandr26",
                "kesan": "Publick speakingnya bagus",  
                "pesan":"Keep shining, Kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cL7f55Y1_mpzYFYqq4QUUkFGo3B2b91C",
            "https://drive.google.com/uc?export=view&id=1WfZZYzJCWBKmR2j0ZeNYWV2Cv7Rm0Urj",
            "https://drive.google.com/uc?export=view&id=1jOKb6GNNiBINL630Ez1_Sm4KCZ4cGygj",
            "https://drive.google.com/uc?export=view&id=1Lvwy1euenQlOBd5cmpi2EiDEbHLVeZIL",
            "https://drive.google.com/uc?export=view&id=1uj-IYjN0eGDigoYiirJVpL3ibxrKP7V2",
            "https://drive.google.com/uc?export=view&id=1D41SHxei-b0WfC1iibFLdf0WDuc9RCwD",
            "https://drive.google.com/uc?export=view&id=1uj9aGRXq2PvR7x5wgUvfCesc1nm50JMr",
            "https://drive.google.com/uc?export=view&id=1HuSDiShE4HKvQQJDw7GL07PaLtqDre4z",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1AbtZGCJznjghZTF5WDBdJpDUHY0llCvN",
            "https://drive.google.com/uc?export=view&id=1eM9b3Dcyz-KFUHvWABw90ITgTvbuZhQu",
        ]
        data_list = [
            {
               "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Nanya ke gpt",
                "sosmed": "@trimurniaa_",
                "kesan": "Seru diajak sharing",  
                "pesan":"semoga selalu diberi keberuntungan kak"
            },
            {
                 "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Way Hui",
                "hobbi": "Membaca, menonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Selalu kasih solusi.",  
                "pesan":"semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Belajar, nonton film, tidur",
                "sosmed": "@wlsbn0",
                "kesan": "ga ekspect kakanya pembisnis",  
                "pesan":"Lancar terus usahanya kak"# 1
            },
             {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Drachin",
                "sosmed": "@anisadini10",
                "kesan": "lucuu",  
                "pesan":"semangat kuliahnya kak"# 1
            },
             {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Ngajar alpronya asik!",  
                "pesan":"Semoga semakin sukses terus bang!"
            },
             {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Jualan pancing",
                "sosmed": "@fleurnsh",
                "kesan": "Banyak ilmu dari kakak.",  
                "pesan":"Jaga kesehatan, ya kak!"# 1
            },
            {
                "nama": "Claudhia Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Tidur",
                "sosmed": "@dylebee",
                "kesan": "baik banget",  
                "pesan":"Tetap rendah hati, Kak!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450110",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama, main kucing",
                "sosmed": "@myrrinn",
                "kesan": "orangnya easy going",  
                "pesan":"Makasih banyak ilmunya bang!"
            },
            {
               "nama": "Muhammad fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis, olahraga",
                "sosmed": "@fhrul.pdf",
                "kesan": "kece abis",  
                "pesan":"Semangat buat semua impiannya bang!"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "baik, mau ngajarin codingan saya hehe",  
                "pesan":"kece terus kak, semangat aspraknya!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Duduk di tepi pantai sambil galauin bintang ynag tinggal satu",
                "sosmed": "@berlyyanda",
                "kesan": "seru ga ngebosenin",  
                "pesan":"Semoga makin sukses!"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18uKYtQCwwbnWeBOxWAu1Ns1S_m7Fmg3T",
            "https://drive.google.com/uc?export=view&id=1GzwKsjYbArlBYVL4TnJGa5TK-sZ8_H-R",
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
                "kesan": "Suka vibes positif dari kakak.",
                "pesan": "Harapan terbaik untuk masa depan kakak!", 
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bikin kita lebih percaya diri.",
                "pesan": "Terus berkarya dan berprestasi!",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
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

elif menu == "Departemen MEDKRAF":

    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GDdCSYZhy4uhFPRDIAGpNBZH_-J0QXm0",
            "https://drive.google.com/uc?export=view&id=1G9rSMVCcfNxeUbCGis8smTNNtb1NZB13",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1GnW7Sj7syeyp6b-Qlh3QYTOXMgTaWPUg",
            "https://drive.google.com/uc?export=view&id=1GM7Ao-eXNwqnpHtDh9Osi3CN-0k5wFrX",
            "https://drive.google.com/uc?export=view&id=1GC1Jy9kgcQUvW0sgtebbeJDOaOgzhkv7",
            "https://drive.google.com/uc?export=view&id=1G_KJOYg23GvmfO199WO_ym--skHSBN3R",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1F8ibL_vkAhbDZeQXyyzS1bnC1yvksDeV",
            "https://drive.google.com/uc?export=view&id=1GqJ1bB5h_0owgsrg1OA6nyHg-4tTrInm",
            "https://drive.google.com/uc?export=view&id=1GOiKy6vysquRmW8jcoAqYgq3mbXbC6-l",
            "https://drive.google.com/uc?export=view&id=1GoWvpPOItmyqzs7UJLwGw-jd1elydarZ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1GFyuQwrO7OSMObJeBroo8qgf7HDnDzhk",
            "https://drive.google.com/uc?export=view&id=1GO6jXESXoXY2yxCMrJ3N0r-sQXJtQF4u",
            "https://drive.google.com/uc?export=view&id=1GEtS0Du3x5BVhh6fSwSsa0o0XlUg3IN4",
            "https://drive.google.com/uc?export=view&id=1GCSbsiHdEcfGd8b3wDBq0HQOti_GTxjm",
            "https://drive.google.com/uc?export=view&id=1GanTtXCKwhlo1PLN18BTRd84_lV4UX3J",
         
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "",
                "kesan": "penuh semangat",
                "pesan": "semoga apa yang diimpikan tercapai bangg",
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "cakep bangett kakk",
                "pesan": "terima kasih sudah membagikan ilmu!", 
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Nugas",
                "sosmed": "@arsyiah._",
                "kesan": "asikkkk",
                "pesan": "semangat terus kak", 
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": " 121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": " @dino_kiper",
                "kesan": "vibes orang pinter",
                "pesan": "semangat untuk TAnya", 
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "ramah",
                "pesan": "semangat menjalani hari hari di semester2 akhir bang", 
            },
            {
                "nama": "Cintya  Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "vibesnya cocok banget di divisi media & konten",
                "pesan": "semangat ngonten kak", 
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " 122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "menginspirasi",
                "pesan": "jangan lupa istirahat dan tidur kak", 
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "ga pelit ilmu",
                "pesan": "keep going", 
            },
            {
                "nama": "Patricia Leondra Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak bikin topik serius jadi fun.",
                "pesan": "ayo kita ngajar anak kelas 4 lagi", 
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "asikk orangnyaa ternyata asik beneran",
                "pesan": "maaf sempet salah nyebut nama kak hehe", 
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "easy going!",
                "pesan": "keep spirit", 
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "gaya fotonya keren",
                "pesan": "keep sharing your experiences ", 
            },
            {
                "nama": "Nasywa Nur Afifah ",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "ramah dan menyenangkan",
                "pesan": "semoga impian nya segera tercapai", 
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "approachable!",
                "pesan": "terus berbagi ilmu dan inspirasi!", 
            },
             {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": " enak diajak diskusi",
                "pesan": " keep being awesome", 
            },
             {
                "nama": "Hermawan Manurung ",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani) ",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "fresh dan energik",
                "pesan": "semangat menjadi pdd bang", 
            },
             {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "kreatif dalam menjelaskan.",
                "pesan": "makasi materi tentang Rnya kakk", 
            },
             {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "kak baca novel tereliye gaa",
                "pesan": "jaga kesehatan kak!", 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen MIKFES":

    def Mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lWdu9PD3xm8spfuTto6x1yOaskkY1tLH",
            "https://drive.google.com/uc?export=view&id=1436EDcyIy1neMMGiS2i_CwSVcOb2c4b5",
            "https://drive.google.com/uc?export=view&id=12svBq_2H8kuFFoTRMT8evNpudd8WJlx4",
            "https://drive.google.com/uc?export=view&id=14eRGQSZOsw8z3h_3f9vLJs2c7g7OsL8v",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=10JKTN1r3e4h81eYwukQU3mbrA9VuvFH0",
            "https://drive.google.com/uc?export=view&id=1mLBLjztG03vFGRnLO0VGxFJs5mzwz2Rx",
            "https://drive.google.com/uc?export=view&id=1f2f1CZA4Ui8oEsgn1pb05yDNyb8vDsGu",
            "https://drive.google.com/uc?export=view&id=1XT3d755N6mHdcEy4oAaCaUIJWeXnSXyL",
            "https://drive.google.com/uc?export=view&id=1BHxhT3DncbE6IvhbUoXBrYsXH3phFUlw",
            "https://drive.google.com/uc?export=view&id=1ZVhhLE6CQNUKaNsRILottaElvNXrJjt_",
            "https://drive.google.com/uc?export=view&id=1YGtvvDBP8s1LIMpUlUFeVrehZIrAfzCw",
            "https://drive.google.com/uc?export=view&id=1tWbVuoUWRHwx07rVb8ZdTfDM7hRGZ_Qc",
            "https://drive.google.com/uc?export=view&id=1wBGl4p4zGn1jh4N66PLqaRB99u1g1vCb",
            "https://drive.google.com/uc?export=view&id=1EU1eKosOx9XR2yT8UtFBv0nvoVRzMR0H",
            "https://drive.google.com/uc?export=view&id=1ABClOGf9ehcxOLj5w41vV0i1vQ6kJ4ns",
            "https://drive.google.com/uc?export=view&id=168N19tWhf7CduhQ4f9iPz0ZjeNy0Fy3-",
            "https://drive.google.com/uc?export=view&id=1ZOwOb4BCU456TyWmb0minpk3iuhGLUE_",

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
                "pesan": "mangats kak",
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

elif menu == "Departemen Eksternal":
    def Eksternal():
        gambar_urls = [

            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "Yogy Sea Tama",
                "nim": "121450041",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "Ngisi Bensin",
                "sosmed": "@yogyyyyyyy",
                "kesan": "-",
                "pesan": "-", 
            },
            {
                "nama": "Ramadhita Asifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Rajabasa",
                "alamat": "Rajabasa",
                "hobbi": "Belajar",
                "sosmed": "@Ramadhitaasifa",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450112",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Belajar dengan Rajin",
                "sosmed": "@nazwanbilla",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Bikin Surat",
                "sosmed": "@deaa.rsn",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliadinda",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Ratu Keisha Jasmin Deonova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Ngerjain ADW",
                "sosmed": "@jasminednva",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Tobias David Monogari",
                "nim": "121450081",
                "umur": "20",
                "asal": "Jakarta Barat",
                "alamat": "Pemda",
                "hobbi": "Bikin Puisi",
                "sosmed": "@tobiassiagian",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Buat Portopolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "12245022",
                "umur": "20",
                "asal": "Jogja, Depok",
                "alamat": "Way Huwi",
                "hobbi": "menghafal al-quran",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara",
                "alamat": "Korpri",
                "hobbi": "cuci baju",
                "sosmed": "@u_yippy",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "sukarame",
                "hobbi": "Quality Time",
                "sosmed": "@chipawww",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Jakarta",
                "hobbi": "Nonton Youtube dan main ML",
                "sosmed": "@Alfaritziirfan",
                "kesan": "-",
                "pesan": "-",

            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "main vollly",
                "sosmed": "@izzalutfiaa",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Khaalishah Zuhrah ALyaa Valefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Nyanyi",
                "sosmed": "@alyaavalefi",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ngeresume Seminar",
                "sosmed": "@rayHis_",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Jakarta",
                "hobbi": "Baca",
                "sosmed": "@tria_y062",
                "kesan": "-",
                "pesan": "-",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Eksternal()
elif menu == "Departemen Internal":
    def Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "-",
                "pesan": "-", 
            },
            {
                "nama": "Catherine firdhasari maulina sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@chatherine.sinaga",
                "kesan": "-",
                "pesan": "-",
            },    
            {
                "nama": "M. Akbar resdika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Memelihara dino",
                "sosmed": "@akbar_resdika",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Rani puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@ranipu",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Rendra eka prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan lapas raya",
                "hobbi": "nulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Salwa farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan raya",
                "hobbi": "ngeliat cogan",
                "sosmed": "@slwfhn_694",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Ari sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung barat",
                "alamat": "Labuhan ratu",
                "hobbi": "Main futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Azizah kusumah putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Meira listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan raya",
                "hobbi": "Menghalu",
                "sosmed": "@meiraln",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Rendi alexander hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost gunawan",
                "hobbi": "Menyanyi",
                "sosmed": "@alexanderr",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Renta siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera utara",
                "alamat": "Gerbang barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Yosia lehare banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Dairi, Sumatera utara",
                "alamat": "Perum griya indah",
                "hobbi": "Bawa motor pakai kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Josua panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal": "Pematang siantar",
                "alamat": "Gya kost",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "-",
                "pesan": "-",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Internal()
elif menu == "Departemen SSD":
    def Ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "-",
                "pesan": "-", 
            },
            {

                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Metro",
                "hobbi": "Nonton film",
                "sosmed": "@adistisa_",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung",
                "sosmed": "@zhjung",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "TB 3 Asrama",
                "hobbi": "Belajar",
                "sosmed": "@dananghk_",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel__julio",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Nabilah Andika Fitriani",
                "nim": "121450129",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilaafrn",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Alvia Asrinda Br.Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobbi": "Nonton Windah",
                "sosmed": "@alviaginting",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Dhafin Razaka Luthfia",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jalan nangka 1",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqri3",
                "kesan": "-",
                "pesan": "-",
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    Ssd()

# Tambahkan menu lainnya sesuai kebutuhan
