import streamlit as st

st.set_page_config(page_title= "tugas fisika komputasi awan",page_icon="🌡️",layout= "wide")
st.header("Kalkulator Suhu 🌡️")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        x = st.number_input("Insert a number", value=0.0)
        sx = st.selectbox("Satuan", ("C", "F", "R", "K"), key='sx')
        sy = st.selectbox("Dikonversi ke ",  ("C", "F", "R", "K"), key='sy')
# Fungsi untuk konversi suhu
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Konversi ke Celsius
    if from_unit == "F":
        value = (value - 32) * 5/9
    elif from_unit == "K":
        value = value - 273.15
    elif from_unit == "R":
        value = value * 5/4
    
    # Konversi dari Celsius ke satuan yang diinginkan
    if to_unit == "F":
        return (value * 9/5) + 32
    elif to_unit == "K":
        return value + 273.15
    elif to_unit == "R":
        return value * 4/5
    return value  # jika to_unit adalah "C"

# Melakukan konversi dan menampilkan hasil
if x is not None:
    n = convert_temperature(x, sx, sy)
    with right_column:
        st.subheader("hasil konversi")
        st.write("###")
        st.write(x, " ", sx, "=", n, sy)
st.write("---")
st.caption("agna aldhaka-fisika_komputasi_awan")


    


