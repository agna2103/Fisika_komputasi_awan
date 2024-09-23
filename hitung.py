import streamlit as st

# Input suhu dan satuan awal
x = st.number_input("Insert a number", value=0.0)
sx = st.text_input("Satuan (C, F, K)", "C").upper()

# Input satuan yang ingin dikonversi
sy = st.text_input("Dikonversi ke (C, F, K)", "C").upper()

# Fungsi untuk konversi suhu
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Konversi ke Celsius
    if from_unit == "F":
        value = (value - 32) * 5/9
    elif from_unit == "K":
        value = value - 273.15
    
    # Konversi dari Celsius ke satuan yang diinginkan
    if to_unit == "F":
        return (value * 9/5) + 32
    elif to_unit == "K":
        return value + 273.15
    return value  # jika to_unit adalah "C"

# Melakukan konversi dan menampilkan hasil
if x is not None:
    n = convert_temperature(x, sx, sy)
    st.write(x, " ", sx, "=", n, sy)


