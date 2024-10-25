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
            "https://drive.google.com/uc?export=view&id=1K-Mb7QcEJtdmADdy7bnIKzhGlOA-Rrpb",
            "https://drive.google.com/uc?export=view&id=1MfzFXfPq9zzp09IdOQudezhyy0iAw5LG",
            "https://drive.google.com/uc?export=view&id=1PH9FaszLQyoeiIz4qVk0CJ1vrB5Mf9p-",
            "https://drive.google.com/uc?export=view&id=1mTyqFWwLfoOlWMax2zeB22mS6AX_36vV",
            "https://drive.google.com/uc?export=view&id=13B6154zsrRX419a0nZM3y8P__3tpVfzR",
            "https://drive.google.com/uc?export=view&id=1O49loCksGwswHL9JpiR8rDpHPh1RCHdx",
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
                "kesan": "Berkharisma dan Energetic",  
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
                "kesan": "Kece abiezzz dan funny",  
                "pesan":"Selalu ganteng bang"# 1
            },
            {   
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Jl.Pagar Alam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Positive energy dan good listener",  
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
                "kesan": "Cantik dan rendah hati ",  
                "pesan":"Semoga selalu baik hati kak"# 1
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
                "pesan":"Semangat ngurus duitnya kak"# 1
            },
        
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Metro",
                "hobbi": "Belajar",
                "sosmed": "@nadilaandr26",
                "kesan": "",  
                "pesan":"Semangat ngasprak strukdatnya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":

    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Tanya sama GPT",
                "sosmed": "@trimurniaa",
                "kesan": "Kakaknya cantik, ramah, baik",
                "pesan": "semangat kuliahnya kakak, tetap jadi orang baik",
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Puasa Senin Kamis",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Baik banget kakaknya, sgt humble",
                "pesan": "Semangat kuliahnya kak", 
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton film",
                "sosmed": "wlsbn0",
                "kesan": "Ramah banget kakanya, baikk pula",
                "pesan": "semangat ya kak, tetap ramahh", 
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450021",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": " @anisadini10",
                "kesan": "Kakaknya ramahh, asik,baik",
                "pesan": "semangat terus kuliahnya kakak, jangan mudah menyerah", 
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kalianda",
                "hobbi": "Membaca Al waqiah setiap magrib",
                "sosmed": " @ansftynn_",
                "kesan": "Manis banget kakaknya, ramah juga",
                "pesan": "semangat kuliahnya kak, tetap baik hati kak", 
            },
            {
                 "nama": "Feryadi Yulius ",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya sepertinya famous yah",
                "pesan": "semangat kuliahnya kak, semoga lulus tepat waktu", 
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-Qur'an",
                "sosmed": "@fleurnsh",
                "kesan": "MasyaAllah kak pertahankan hobinya",
                "pesan": "Semangat kuliahnya, semoga semakin rajin mengerjakan tugas",
            },
            {
                "nama": "Claudhia Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": " @dylebee",
                "kesan": "Bagus sekali kak namanya, orangnya juga cantik",
                "pesan": "semangat ya kuliahnya jangan putus asa kak", 
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya baik, kalem, dan ramah",
                "pesan": "Semangat kuliahnya bang, jangan lupa belajar tiap hari", 
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20 tahun",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": " @_.dheamelia",
                "kesan": "Kakaknya kelihatan aktif organisasi bangettt",
                "pesan": "Ramahh banget kak Dheaa", 
            },
            {
                "nama": "Muhammad Fachrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Sholat Malam",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
            },
             {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Bilabong",
                "hobbi": "Cerita",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya keren banget",
                "pesan": "semangat kuliahnya bang, jangan lupa belajar tiap hari", 
            }, 
            {
                "nama": " Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "sosmed": "",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Manis bangett kakk, NIM nya sama kayak aku hihi",
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
                "kesan": "",
                "pesan": "", 
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": " 121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": " @dino_kiper",
                "kesan": "",
                "pesan": "", 
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "",
                "pesan": "", 
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
                "pesan": "", 
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " 122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "",
                "pesan": "", 
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "",
                "pesan": "", 
            },
            {
                "nama": "Patricia Leondra Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "",
                "pesan": "", 
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "",
                "pesan": "", 
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "",
                "pesan": "", 
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "",
                "pesan": "Ramahh banget kak Dheaa", 
            },
            {
                "nama": "Nasywa Nur Afifah ",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "",
                "pesan": "", 
            },
             {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "",
                "pesan": "", 
            },
             {
                "nama": "Hermawan Manurung ",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani) ",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "",
                "pesan": "", 
            },
             {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "",
                "pesan": "", 
            },
             {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "",
                "pesan": "", 
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
    Internal()
elif menu == "DEPARTEMEN SSD ":
    def Ssd():
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
    Ssd()

# Tambahkan menu lainnya sesuai kebutuhan
