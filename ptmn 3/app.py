import streamlit as st
from core import Blockchain

st.set_page_config(page_title="Blockchain Explorer", page_icon="🤖", layout="wide")
st.title("📦 Blockchain for Halal Coffee Supply Chain")

if 'my_blockchain' not in st.session_state:
    st.session_state.my_blockchain = Blockchain()

st.sidebar.header("Tambah Data Baru")

petani = st.sidebar.text_input("Nama petani/aktor:")
jumlah_kopi = st.sidebar.text_input("Jumlah kopi:")
lokasi = st.sidebar.text_input("Lokasi kebun:")

if st.sidebar.button("Tambah Data"):
    if petani and jumlah_kopi and lokasi:
        data_transaksi = f"Nama petani: {petani}, Jumlah kopi: {jumlah_kopi}, Lokasi kebun: {lokasi}"
        st.session_state.my_blockchain.add_block(data_transaksi)
        st.sidebar.success("Data berhasil ditambahkan ke blockchain")
    else:
        st.sidebar.error("Harap isi semua field sebelum menambahkan data")

st.subheader("Data Transaksi di Blockchain")

is_valid = st.session_state.my_blockchain.is_chain_valid()
if is_valid:
    st.success("✅ Blockchain valid")
else:
    st.error("❌ Blockchain tidak valid")

for block in st.session_state.my_blockchain.chain:
    with st.expander(f"Block {block.index} | Hash {block.hash[:15]}..."):
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Data Payload**")
            st.info(block.data)
            st.write(f"**Timestamp:** {block.timestamp_readable}")

        with col2:
            st.write("**Kriptografi:**")
            st.write("**Hash saat ini:**")
            st.code(block.hash, language='python')
            st.write("**Hash sebelumnya (pointer):**")
            st.code(block.prev_hash, language='python')