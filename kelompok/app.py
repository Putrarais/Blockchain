import streamlit as st
from core import Blockchain

st.set_page_config(page_title="film", page_icon="🎬", layout="wide")
st.title("Hipelem 🎞️")

if 'my_blockchain' not in st.session_state:
    st.session_state.my_blockchain = Blockchain()

# --- SIDEBAR ---
st.sidebar.header("Tambahkan data Film")

genre = st.sidebar.selectbox("Genre Film:", ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", "Documentary"])
film = st.sidebar.text_input("Nama Film:")
sutradara = st.sidebar.text_input("Sutradara:")
durasi = st.sidebar.text_input("Durasi (jam):")
sinopsis = st.sidebar.text_area("Sinopsis:")

if st.sidebar.button("Tambah Data"):
    if film and sutradara and durasi:
        data_transaksi = f"Nama film: {film}, Sutradara: {sutradara}, Durasi: {durasi}, Sinopsis: {sinopsis}, Genre: {genre}"
        with st.spinner("Sedang melakukan penambangan blok (Proof of Work)..."):
            st.session_state.my_blockchain.add_block(data_transaksi)
        st.sidebar.success("Film berhasil ditambahkan ke data")
    else:
        st.sidebar.error("Harap isi semua field sebelum menambahkan data")

st.sidebar.markdown("---")
st.sidebar.subheader("Simulasi Peretasan")

# Tombol Khusus Hack Blok 1
if st.sidebar.button("💥 HACK BLOK 1"):
    if len(st.session_state.my_blockchain.chain) > 1:
        st.session_state.my_blockchain.chain[1].data = "DATA PALSU!"
        st.sidebar.warning("⚠️ Data Blok Index 1 telah diubah secara paksa menjadi 'DATA PALSU!'")
    else:
        st.sidebar.error("Belum ada Blok Index 1. Tambahkan data film terlebih dahulu!")

# --- HALAMAN UTAMA ---
st.subheader("Data Film di Hipelem")

# Tombol Pembuktian Integritas Rantai
if st.button("🛡️ Cek Integritas Rantai"):
    is_valid = st.session_state.my_blockchain.is_chain_valid()
    if is_valid:
        st.success("✅ Status Jaringan: AMAN (Rantai Valid & Data Utuh)")
    else:
        st.error("🚨 Status Jaringan: BAHAYA (Data telah dimanipulasi!)")

for block in st.session_state.my_blockchain.chain:
    with st.expander(f"Block {block.index} | Hash {block.hash[:15]}..."):
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Data Payload**")
            st.info(block.data)
            st.write(f"**Timestamp:** {block.timestamp_readable}")
            st.write(f"**Nonce:** `{block.nonce}`")

        with col2:
            st.write("**Kriptografi:**")
            st.write("**Hash saat ini:**")
            st.code(block.hash, language='text')
            st.write("**Hash sebelumnya (pointer):**")
            st.code(block.prev_hash, language='text')