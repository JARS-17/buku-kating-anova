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
            "Departemen MEDKRAF",
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
            "nav-link-selected": {"background-color": "#FEF9D9"},
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
            "https://drive.google.com/uc?export=view&id=14dY_j7LracZ7RympCjtqFsQOg3_LsSII",
            "https://drive.google.com/uc?export=view&id=19bNRn8-ACsxGD1zk5lDnG4imIQ76_cum",
            "https://drive.google.com/uc?export=view&id=1BFDlRcrPgV5_PgFYv1d16g35EH3PpP5-",        
            "https://drive.google.com/uc?export=view&id=1NuE1C3r8h3H0tp5xNAhRPtOvGuN_qVUR",
            "https://drive.google.com/uc?export=view&id=1u5FHoOGSLJ6p9_dHmMEWq9_3JhATwcr_",
            "https://drive.google.com/uc?export=view&id=1o8oDyT4ZKIuxVJQL6CaUvrsVsZHz3nBV",
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
                "kesan": "Abangnya sangat Berkharisma dan Menginspirasi",  
                "pesan":"Semoga selalu menginspirasi bang dan sukses selalu"# 1
            },

            {   
                "nama": "Pandra Insani Putra Anwar",
                "nim": "121450147",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main Gitar",
                "sosmed": "@pandrainsani27",
                "kesan": "Bang Pandra Keren banget dan Insight full",  
                "pesan":"Semangat terus bang dalam menjalani hari-harinya!"# 1
            },

            {   
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Jl.Pagar Alam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak keren banget, suka banget denger penjelasan kakak",  
                "pesan":"Semangat terus kakak!"# 1
            },
        
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Nangka 4",
                "hobbi": "Dengerin Bg Pandra Main Gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Cantik banget kakaknya, sukaaa <3 ",  
                "pesan":"Semoga ga pernah bosen dengan hobinya kak, sukses selalu ya kak!"# 1
            },
        
            {   
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@htrpdla",
                "kesan": "Keren banget kak",  
                "pesan":"Semangat terus ya kak"# 1
            },
        
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Metro",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nadilaandr26",
                "kesan": "Kakak definisi bendahara banget, kereen poll",  
                "pesan":"Sukses selalu ya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=167wCHlLHMhiUL7Fq-sU6ml2f0Smnqzu7",
            "https://drive.google.com/uc?export=view&id=16aO3fLYDl3SNkKFwZATqrFTyL-Mxxdjd",
            "https://drive.google.com/uc?export=view&id=16aFdrIXGx0z0DI0tRL4NaXpClmoFZoZp",
            "https://drive.google.com/uc?export=view&id=16I6VY9LaeSrOM95qe5XVyFD8QijB7Lyf",
            "https://drive.google.com/uc?export=view&id=1639tAESoKbZMGzqqnZHP3_nllqm9T4-3",
            "https://drive.google.com/uc?export=view&id=16I-Gvi2Vo1NE_DND9UKE-9ITYdlu1LOT",
            "https://drive.google.com/uc?export=view&id=16m3IMINY4KrmfNqFgeZPSjMITrzkLlbJ",
            "https://drive.google.com/uc?export=view&id=16YrdONWJ0JKty0idDU35IrV89JFCy0g1",
            "https://drive.google.com/uc?export=view&id=1mDP6qSMfaytFGLFQss9O6LzqH8fZhnaO",
            "https://drive.google.com/uc?export=view&id=15wXYT6Ix0BGYNN17DFhkBE3ux2u9MACt",
            "https://drive.google.com/uc?export=view&id=16cQLvWKslBh_FUFkr8am4fOy_czjwAnY",
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
                "kesan": "Kakak cantik, lucu, baik, dan sangat menginspirasi <3. Suka banget kalau ngobrol sama kakak!",  
                "pesan":"Tetap semangat kak niya dalm menjalani hari-harinya, semoga sukses dimanapun berada!"
            },

            {
                "nama": "Annisa cahyani surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangsel",
                "alamat": "Way huwi",
                "hobbi": "Membaca, nonton",
                "sosmed": "@anisacahyanisurya",
                "kesan": "Kakak nya cantik dan manis banget",  
                "pesan":"Semoga hidup kakak selalu bahagia kak!"# 1
            },

            {
                "nama": "Wulan sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden saleh",
                "hobbi": "Belajar, nonton film, tidur",
                "sosmed": "@wlsbn0",
                "kesan": "Kak Wulan vibesnya seperti kakak yang mengayomi banget, sukaa!!",  
                "pesan":"Kakak cantik semoga sehat dan sukses selalu yaa!"# 1
            },

            {
                "nama": "Anisa dini amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati agung",
                "hobbi": "Nonton drachin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak berwibawa banget, suka banget cara kakak ngejelasin sesuatu",  
                "pesan":"Semoga hidup kakak selalu bahagia (Sebahagia nonton drachin)!"# 1
            },

            {
                "nama": "Feriyadi yulius",
                "nim": "122450087",   
                "umur": "20",
                "asal":"Sumatera selatan",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya keren dan kaya orang pinter",  
                "pesan":"Semangat terus ngaspraknya bang, semoga menjadi berkah!"# 1
            },

            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Jualan pancing",
                "sosmed": "@fleurnsh",
                "kesan": "Kakaknya lucu iihh, sukaa!!",  
                "pesan":"Selamat kak jualan pancingnyaa!"# 1
            },

            {
                "nama": "Claudhia Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Tidur",
                "sosmed": "@dylebee",
                "kesan": "Kakaknya seperti orang baik, aku suka banget ngobrol sama kakak",  
                "pesan":"Semoga kakak selalu diberkati oleh Tuhan Yang Maha Esa!"# 1
            },

            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450110",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur yang lama, main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya mirip kucing, lucuu",  
                "pesan":"Semoga mimpi indah terus di sepanjang tidurnya bang!"# 1
            },

            {
                "nama": "Muhammad fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis, olahraga",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kereen banget jago ngeelukis",  
                "pesan":"Semangat dalam menjalani perkuliahannya bang"# 1
            },

            {
                "nama": "Jeremia susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Asik banget bang, okee poll",  
                "pesan":"Semangat ngaspraknya bang, semoga menjadi berkat yang melimpah!"# 1
            },

            {
                "nama": "Berliana enda putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera barat",
                "alamat": "Way huwi",
                "hobbi": "Duduk di tepi pantai sambil galauin bintang yang tinggal satu",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya lucuu begeteee",  
                "pesan":"Tetap semangat kak jangan galau galauu!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17C7BNmJre7k3F_wORgAQpWEg4bgN-P7T",
            "https://drive.google.com/uc?export=view&id=17Fk_pJ4ADFfir2dMpzKOl1HVxs_EJCy4",
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
                "kesan": "Kakaknya lucu banget, aku ngefanss. Public speakingnya 1000/10",
                "pesan": "Semangat terus kak dalam menjalani hidupnya, jangan lupa jaga kesehatan kakak!", 
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Nyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kereen bang",
                "pesan": "Tetap dan selalu bersinar bang!",
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
            "https://drive.google.com/uc?export=view&id=17sv3kcELQ3VUxJwVI4-L3-VFb8LyPSdz",
            "https://drive.google.com/uc?export=view&id=17uSCiyYz7ieHY5WLqngj_Gddb2SMjSw5",
            "https://drive.google.com/uc?export=view&id=17bCyp4JH__TiagS2m-ZXDZ8GbRgZLxe0",
            "https://drive.google.com/uc?export=view&id=17wyhqkE1ICIIyL6vFfcKnlsnqQErAFgC",
            "https://drive.google.com/uc?export=view&id=17q8-ARUiRr8xoox1d7ARdaylcwOjlVLX",
            "https://drive.google.com/uc?export=view&id=183H6RRup0fOowRfEM3PTPgK07GSyP3x7",
            "https://drive.google.com/uc?export=view&id=17m1Xqgns-nRlx0rzD2X2kowwrFK_9efP",
            "https://drive.google.com/uc?export=view&id=17PIa6F2ATUmfaRS1jdv6I2GvfSVT_pD2",
            "https://drive.google.com/uc?export=view&id=17S4Z3cFiZx_gcfLwyPYLiFODZ-ga53wZ",
            "https://drive.google.com/uc?export=view&id=188MREeHqzgyBVUUeDzrImZkZHSPOQHu0",
            "https://drive.google.com/uc?export=view&id=17aOvdUgvfwPLbnZdrSQGZPW_GnAfYvz_",
            "https://drive.google.com/uc?export=view&id=17GbSAOKHE00QJor1fB_iZgRZz1C6e6xD",
            "https://drive.google.com/uc?export=view&id=1849Xxm06N5nAWc2y5PxFXvEe477nBWCO",
            "https://drive.google.com/uc?export=view&id=17_7xcxLESY4PfRQveborGFbyUoFYjtUU",
            "https://drive.google.com/uc?export=view&id=17QcdqfSd9i6KM0tSAZvIkL5NiXSmyoQ_",
            "https://drive.google.com/uc?export=view&id=17ZAXGD4V2E6BuXboSy-9jot_eXIWiGHO",
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@wayylaja",
                "kesan": "Makasih banget buat ide-ide kreatif dan semangatnya bangg",
                "pesan": "Terus berkarya dan sukses selalu buat proyek ke depannya!",
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
                "kesan": "kontennya keren keren banget kak",
                "pesan": "Jangan berhenti kasih ide-ide gokil!", 
            },
            {
                "nama": "Muhammad Kaisar Firdaus ",
                "nim": " 121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": " @dino_kiper",
                "kesan": "gokil banget bang",
                "pesan": "tetap keren ya bang!", 
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Hasil kerja abang selalu top!",
                "pesan": "tetap semangat bang!", 
            },
            {
                "nama": "Cintya  Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Cantik dan keren banget, cocok banget di divisi media & konten",
                "pesan": "Semoga makin kreatif tiap hari!", 
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": " 122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "keren banget kak",
                "pesan": "Semoga selalu semangat dalam menyibukkan dirinya kak", 
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "kereen banget, biasanya siapa kak?",
                "pesan": "semoga hari kakak bagus terus!", 
            },
            {
                "nama": "Patricia Leondra Diajeng Putri ",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "kakak lucu, cantik, keren banget!",
                "pesan": "Keep up the awesome work kak cia!", 
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "lucu banget kak!",
                "pesan": "jangan pernah menyerah ya kakak, tetap semangat kakak cantik!", 
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah ",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Cantik dan keren banget ",
                "pesan": "Keep inspiring, kak!", 
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Keliatan banget passion-nya di media kreatif",
                "pesan": "Terus berkarya, sukses selalu bang!", 
            },
            {
                "nama": "Nasywa Nur Afifah ",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "",
                "pesan": "", 
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Abangnya keliatan soleh ya rajin sholat malam",
                "pesan": "semangat kuliahnya kak, tetap pertahankan rajin sholat malamnya", 
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Amazed banget ssama abang",
                "pesan": "Selalu semangat bang!", 
            },
            {
                "nama": "Hermawan Manurung ",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani) ",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang lucu dan keren banget!",
                "pesan": "Semoga makin kreatif bang setiap harinya", 
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakak bener bener menginspirasi",
                "pesan": "Tetap menginspirasi kita ya kak!", 
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "manis banget",
                "pesan": "Kalau butuh saran novel calling aja ya kak, tetap semangat kak!", 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen MIKFES":

    def Mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RGuAWe6OVP-Gb7uTmgNreCqUdAYSzvnm",
            "https://drive.google.com/uc?export=view&id=1dI8d5ulHBviXcyBLg7cLBFkhBg-dWMgQ",
            "https://drive.google.com/uc?export=view&id=1_EU5S1TB4AQeIYNrest6yoeWbs2vVstj",
            "https://drive.google.com/uc?export=view&id=1H6xnztMsuvV6E__eOGOzooyxP7diJ3Kj",
            "https://drive.google.com/uc?export=view&id=1MiVyeWFbmGNnG5BEsfHqm4hJ7QCWq7fY",
            "https://drive.google.com/uc?export=view&id=1eKN4OAYPOQGAhJYphpg_n-zHPj61wuL3",
            "https://drive.google.com/uc?export=view&id=1tUKdw1dMAnGi5_zPFQtr3cDe5rTMLTcS",
            "https://drive.google.com/uc?export=view&id=1zRs6L9d0AGn9IWuj4WOflfalH_opsNLh",
            "https://drive.google.com/uc?export=view&id=1k8xw3jOUGLFQuXFAUHa5XW52Fm7XJ9wJ",
            "https://drive.google.com/uc?export=view&id=1q9EK-Hqp7t-SvvCob6ZYKHa1cBSQwYMW",
            "https://drive.google.com/uc?export=view&id=1Yn9z6e1klNvUsTW05fHJ8J7QNrQxn4he",
            "https://drive.google.com/uc?export=view&id=1t2wbLMGmRuS02mBVYu5NWvaXrM3cNEvj",
            "https://drive.google.com/uc?export=view&id=1erEgoMuNXSZ9e-4U8rDzHyyzn4O4lDOJ",
            "https://drive.google.com/uc?export=view&id=1PQdlpLdtaNxtOSH5zBxKSpBAIMu2-Ehf",
            "https://drive.google.com/uc?export=view&id=1IQwbTV58TF44Srz7pVmvbR-G1p948ArH",
            "https://drive.google.com/uc?export=view&id=1D-cP2EQdpYHMVX9IeGBpBKYtEIkVaPQ4",
            "https://drive.google.com/uc?export=view&id=1mC3_4sUNVEdIXbO3ojWCDFU0YH5UzOL7",
            "https://drive.google.com/uc?export=view&id=1sCxod4wk_XQ6VVWJdBH8LKDFKDcl7685",
            "https://drive.google.com/uc?export=view&id=1srE1QJ7o_KuGp-XnGH4lZHFKj14mLulj",
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
                "kesan": "Abangnya bener bener mikfess banget (pinter dan berwibawa)",
                "pesan": "-\Sukses terus ya bang",
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21 Tahun",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": " Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak Anovaa, namanya seperti kelompokku. Pasti kakak orangnya keren dan baiik",
                "pesan": "Tetap dan selalu semangat kak anovaa!!",
            },
            {
                "nama": " Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": " 20",
                "asal": "Tulang Bawang",
                "alamat": " Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Kereen banget bang",
                "pesan": "Semoga keren terus bang",
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20 Tahun",
                "asal": "Bekasi",
                "alamat": "Teluk Betung ",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya keliatan pinter dan misterius",
                "pesan": "Semoga keren teruss bang",
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": " 122450031",
                "umur": "19 Tahun",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame  ",
                "hobbi": "Main Game",
                "sosmed": "@mregiiii_",
                "kesan": "Bang Regi sangat menginspirasi!!",
                "pesan": "Sukses di sepanjang perjalanan hidup bang.",
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21 Tahun",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira ",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakaknya kiyowo dan kelihatan pinter gitu",
                "pesan": "Semangat terus kakak",
            },
            {
                "nama": "Natanael Oktavianus Partahan Sihombing ",
                "nim": "121450107",
                "umur": "20 Tahun",
                "asal": "Jakarta",
                "alamat": "Kemiling ",
                "hobbi": "Membuka Wisata HMSD",
                "sosmed": "@natanaeloks",
                "kesan": "Abangnya keren dan beerwibawa gituu, sukaa banget",
                "pesan": "Semoga hobinya menjadi berkah bang",
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21 Tahun",
                "asal": "Bukittinggi",
                "alamat": "Korpri ",
                "hobbi": " ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnyaa baiik banget <3",
                "pesan": "Semangat ngaspraknya bang, semoga menjadi berkat yang melimpah",
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21 Tahun",
                "asal": " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Lucu banget kakaknya, akuu suka yang lucu lucu",
                "pesan": "Semangat terus kakak cantik!",
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20 Tahun",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Main Game",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya seperti orang pinter, baik, dan tidak sombong",
                "pesan": "Semoga selalu menjadi orang yang keren kak!",
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20 Tahun",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak kereen banget sumpahh, apa yang kakak ga bisa?",
                "pesan": "Tetap menginspirasi kak Marletta",
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20 Tahun",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Lucu banget kakak",
                "pesan": "Sukses terus kakak lucuu",
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": " 122450072",
                "umur": "20 Tahun",
                "asal": "Palembang",
                "alamat": "Belwis ",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak yang paling cantik, lucu, pinter, baik hati, dan tidak sombong. Aku suka banget sama kak puspaa, love 3000",
                "pesan": "Semoga kakak selalu diberikan kemudahan ya kak selama hidup, love love kak pus",
            },
            {
                "nama": " Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": " Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Abangnya kereen poll",
                "pesan": "Semangat terus bang kuliahnya, semoga sukses bang!",
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20 Tahun",
                "asal": " Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Keren banget bang",
                "pesan": "Semangat bang ngodingnya",
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20 Tahun",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr ",
                "kesan": "Keliatan banget sepuhnya bang, kereen pokoknya",
                "pesan": "Semangat terus bang eggi dalam menjalani hari-harinya!",
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20 Tahun",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama ",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya cantik banget",
                "pesan": "Semoga kakak sehat terus yaak!",
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20 Tahun",
                "asal": "Lampung",
                "alamat": "Karang Anyar ",
                "hobbi": " Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abangnya pinter dan sangat sangat menginspirasi bangeeet",
                "pesan": "Semangat terus bang Syahrl, semoga sukses selalu dimanapun dan kapanpun!",
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21 Tahun",
                "asal": "Banten",
                "alamat": " Sukarame",
                "hobbi": " Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa baik banget, keren banget pokoknya bang Randa",
                "pesan": "Semoga abang mendapat ipk 4.0 dan sehat selalu bang",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Mikfes()

elif menu == "Departemen Eksternal":
    def Eksternal():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1apZ04jsQ7UCwAmHUU66ik0O2dbZZNHtF",
            "https://drive.google.com/uc?export=view&id=1DQuhLP3MKjMdqySVUF-65LkRAqui-ZfT",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Be5ANFBBHQRGXl3COeI6k347rFY-YTyR",
            "https://drive.google.com/uc?export=view&id=11hv8-gIZcCtAL09yhzUOKr5tedmtB81P",
            "https://drive.google.com/uc?export=view&id=1GfNEEHQ-b5kKyYpkJsdxAbc-RiuXwKCO",
            "https://drive.google.com/uc?export=view&id=1ZBkADgRIxI4soARbsgwb1IrBomhGTrL_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1hM4doNiao2hILS_E-if6UTXgA6giCyGy",
            "https://drive.google.com/uc?export=view&id=1GxB6nJswpd6pttk-KTuwMo98nfQxuc_G",
            "https://drive.google.com/uc?export=view&id=1ZFwGPDmsfwMVUWzAC0GshGW65HQ9JVUy",
            "https://drive.google.com/uc?export=view&id=1moGUaw6I_ucyVs5dsHvJZK1fTgdDDpcZ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=121fh4NH6-uCEc3XMnmrWDZNA_lJ4mbRZ",
            "https://drive.google.com/uc?export=view&id=1OeeqHmj09dyoNzLUGVxEhSX6np63uOXb",
            "https://drive.google.com/uc?export=view&id=1jietI7LEPvfz1TLO_kLp6ZM7R9xWb0aH",
            "https://drive.google.com/uc?export=view&id=1rT2aQHNU5IszP7Hqy51NtbGsB9wxC9rH",
            "https://drive.google.com/uc?export=view&id=1NLjuf1xNW3XcJ9cpMJtG9p4TkUpcTXS1",
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
                "kesan": "Suka banget sama cara jelasin abangnya, gacor pokoknya",
                "pesan": "Sukses dan sehat selalu ya bang", 
            },
            {
                "nama": "Ramadhita Asifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal": "Rajabasa",
                "alamat": "Rajabasa",
                "hobbi": "Belajar",
                "sosmed": "@Ramadhitaasifa",
                "kesan": "Cantik banget kakaknya",
                "pesan": "Semangat belajarnya kak",
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450112",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Belajar dengan Rajin",
                "sosmed": "@nazwanbilla",
                "kesan": "Baik dan cantik banget",
                "pesan": "Semoga belajar dengan rajinya nular ya kak, sukses terus kak",
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Bikin Surat",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya lucuu",
                "pesan": "Semangat terus kakak buat suratnya",
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliadinda",
                "kesan": "Kakaknya kaya girl boss, suka banget sama pembawaannya",
                "pesan": "Tetap dan selalu keren ya kak!",
            },
            {
                "nama": "Ratu Keisha Jasmin Deonova",
                "nim": "122450106",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Ngerjain ADW",
                "sosmed": "@jasminednva",
                "kesan": "Aku suka banget sama kakaknya. Lucu, canti, pinter, dan baik hati <3<3<3",
                "pesan": "Semangat ngaspraknya kakak, semoga menajdi berkah",
            },
            {
                "nama": "Tobias David Monogari",
                "nim": "121450081",
                "umur": "20",
                "asal": "Jakarta Barat",
                "alamat": "Pemda",
                "hobbi": "Bikin Puisi",
                "sosmed": "@tobiassiagian",
                "kesan": "Awalnya kaya serem gitu abangnya, ternyata asik banget waktu ngejelasin seputar eksternal",
                "pesan": "Suukses selalu bang, semoga acara Natalnya lancar",
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Buat Portopolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya keren dan waw banget",
                "pesan": "Sukses dan sehat selalu ya bang!",
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "12245022",
                "umur": "20",
                "asal": "Jogja, Depok",
                "alamat": "Way Huwi",
                "hobbi": "menghafal al-quran",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnya lucu",
                "pesan": "Semangat terus bang",
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara",
                "alamat": "Korpri",
                "hobbi": "cuci baju",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya lucu dan kaya penyayang gitu",
                "pesan": "Aku doain kakak harinya happy terus",
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "sukarame",
                "hobbi": "Quality Time",
                "sosmed": "@chipawww",
                "kesan": "Kakaknya adem banget",
                "pesan": "Sukses kuliahnya kak",
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Jakarta",
                "hobbi": "Nonton Youtube dan main ML",
                "sosmed": "@Alfaritziirfan",
                "kesan": "Abangnya keren sekaliii",
                "pesan": "Semoga kalau main game menang terus bang",
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "main vollly",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kakaknya kaya punya super power, sukaa banget sama energi kakaknya",
                "pesan": "Semoga kakak mendapat kesuksesan dan kemudahan",
            },
            {
                "nama": "Khaalishah Zuhrah ALyaa Valefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Nyanyi",
                "sosmed": "@alyaavalefi",
                "kesan": "Suara kakak pasti bagus banget",
                "pesan": "Semangat terus ya kakak",
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ngeresume Seminar",
                "sosmed": "@rayHis_",
                "kesan": "Abangnya keren banget",
                "pesan": "Semangat ngeresumenya bang!",
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Jakarta",
                "hobbi": "Baca",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya lucu dan gemesin banget",
                "pesan": "Semangat terus kakak",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Eksternal()
elif menu == "Departemen Internal":
    def Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11e8V5oROZyE1fP15ya7nF0SWFNeK90SO",
            "https://drive.google.com/uc?export=view&id=1155oX2zpDJRDDYgPKs2SimY6iswiHCNa",
            "https://drive.google.com/uc?export=view&id=122rJofMgV7u3BZMD2PVoGvA7oEYUcpFD",
            "https://drive.google.com/uc?export=view&id=11H9t_P8z79vakzke5HVjrEVnrsvsUgCq",
            "https://drive.google.com/uc?export=view&id=11XR2xWNxWY1E-zTrTBiM96LZlQY_kS5l",
            "https://drive.google.com/uc?export=view&id=11LZUPjw_BTPVnKOSwlwi980wJhkeMzKc",
            "https://drive.google.com/uc?export=view&id=11f6uLrl0PDz_4A7ecOKU9LZ0pm4Yc6xm",
            "https://drive.google.com/uc?export=view&id=122Xd249CUtXC8w6wpZ5l7TwzS5CsOv20",
            "https://drive.google.com/uc?export=view&id=11jzmkaqapxn3W2Vyc8kexGa_d3DACJyD",
            "https://drive.google.com/uc?export=view&id=121I7yg7FHiTeVSvA2bO7RlxOrtlysDTm",
            "https://drive.google.com/uc?export=view&id=11QkTuLeU0E5WmMAoJlwOX2fZzQQLUH5x",
            "https://drive.google.com/uc?export=view&id=117UxWb7QH3BPwXUQxRbT61i_gwgGpVC2",
            "https://drive.google.com/uc?export=view&id=11ySpfULRqsqaVOwmvmdLMsH3sWhUrXi1",
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
            "https://drive.google.com/uc?export=view&id=1G8GrRmJXiUxz7HNmMpkMX5sPttJjEpuW",
            "https://drive.google.com/uc?export=view&id=1FijPDJF2yw2WYcfowJER3NceMnROcKR3",
            "https://drive.google.com/uc?export=view&id=1FjbHZ1l79cniyt-UhFIVs4pEnh-FWJza",
            "https://drive.google.com/uc?export=view&id=1FoOpRQGxwE_VHBO-xJgRcTkocgyUCgdp",
            "https://drive.google.com/uc?export=view&id=1FaBXkyjPEa76Z0j6Q8IV4zUPA_JqxfyE",
            "https://drive.google.com/uc?export=view&id=1FzvooaiCRdLFgc88qGhTnhG_6t0Qddqo",
            "https://drive.google.com/uc?export=view&id=1Ffde5zns2m1WkJk097vfVRuO99wKMBuI",
            "https://drive.google.com/uc?export=view&id=1FbVmXO5M3z7hTsLYV-7G3fLpk9DJ1vdt",
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
