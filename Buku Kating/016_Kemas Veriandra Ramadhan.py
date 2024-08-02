import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.header("Buku Kating")


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
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None


def display_images_with_data(gambar_urls, data_list):
    st.write("Mengunduh dan menampilkan gambar:")
    progress_bar = st.progress(0)
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}..."):
            img = load_image(url)
            if img is not None:
                images.append(img)
        progress_bar.progress((i + 1) / len(gambar_urls))

    for i, img in enumerate(images):
        st.image(img)
        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Deskripsi: {data_list[i]['deskripsi']}")
            st.write(f"Tanggal Lahir: {data_list[i]['tanggal_lahir']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Deskripsi Singkat: {data_list[i]['deskripsi']}")
    st.write("Semua gambar telah dimuat!")


menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH

if menu == "Kesekjenan":

    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T779zcre4ABKNJTATkIPVMzI_1fnDAIG",  # 1
            "https://drive.google.com/uc?export=view&id=1hyjXZIFQj3BEO3RG8Fei1PBYsuag6Ioe",
            "https://drive.google.com/uc?export=view&id=1hyjXZIFQj3BEO3RG8Fei1PBYsuag6Ioe",
            "https://drive.google.com/uc?export=view&id=1hyjXZIFQj3BEO3RG8Fei1PBYsuag6Ioe",
        ]
        data_list = [
            {
                "nama": "Kakak C",
                "deskripsi": "Kakak ini hebat.",
                "tanggal_lahir": " Bekasi, 23 Oktober 2004",
                "nim": "122450016",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@kemasverii",
                "deskripsi": "Kakak ini asik saya suka belajar dengan dia",  # 1
            },
            {
                "nama": "Kakak C",
                "deskripsi": "Kakak ini hebat.",
                "tanggal_lahir": " Bekasi, 23 Oktober 2004",
                "nim": "122450016",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@kemasverii",
                "deskripsi": "Kakak ini asik saya suka belajar dengan dia",  # 2
            },
            {
                "nama": "Kakak C",
                "deskripsi": "Kakak ini hebat.",
                "tanggal_lahir": " Bekasi, 23 Oktober 2004",
                "nim": "122450016",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@kemasverii",  # 3
            },
            {
                "nama": "Kakak C",
                "deskripsi": "Kakak ini hebat.",
                "tanggal_lahir": " Bekasi, 23 Oktober 2004",
                "nim": "122450016",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@kemasverii",
                "deskripsi": "Kakak ini asik saya suka belajar dengan dia",
            },
            {
                "nama": "Kakak C",
                "deskripsi": "Kakak ini hebat.",
                "tanggal_lahir": " Bekasi, 23 Oktober 2004",
                "nim": "122450016",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@kemasverii",
                "deskripsi": "Kakak ini asik saya suka belajar dengan dia",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Baleg":

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T779zcre4ABKNJTATkIPVMzI_1fnDAIG",  # 1
            "https://drive.google.com/uc?export=view&id=1hyjXZIFQj3BEO3RG8Fei1PBYsuag6Ioe",  # 2
            "https://drive.google.com/uc?export=view&id=1hyjXZIFQj3BEO3RG8Fei1PBYsuag6Ioe",  # 3
        ]
        data_list = [
            {
                "nama": "Kakak C",
                "deskripsi": "Kakak ini hebat.",
                "tanggal_lahir": " Bekasi, 23 Oktober 2004",
                "nim": "122450016",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@kemasverii",
                "deskripsi": "Kakak ini asik saya suka belajar dengan dia",
            },
            {
                "nama": "Kakak C",
                "deskripsi": "Kakak ini hebat.",
                "tanggal_lahir": " Bekasi, 23 Oktober 2004",
                "nim": "122450016",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@kemasverii",
                "deskripsi": "Kakak ini asik saya suka belajar dengan dia",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
