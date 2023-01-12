import streamlit as st

def calculator():
    st.set_page_config(page_title="Kalkulator Kimia", page_icon=":chemistry:", layout="wide")
    st.sidebar.title("  :green[Kalkulator Kimia]")
    st.sidebar.header('Pilih Operasi Kalkulator')
    operation = st.sidebar.selectbox("", ["Molaritas", "Normalitas", "PPM"])

    if operation == "Molaritas":
        st.title("Menghitung Molaritas")
        mass = st.number_input("Masukkan massa (g)", value=1.0, step=0.1)
        molar_mass = st.number_input("Masukkan massa molar (g/mol)", value=1.0, step=0.1)
        volume = st.number_input("Masukkan volume (L)", value=1.0, step=0.1)
        molarity = mass / (molar_mass * volume)
        st.write("Molaritas: {:.4f} M".format(molarity))
    elif operation == "Normalitas":
        st.title("Menghitung Normalitas")
        molarity = st.number_input("Masukkan molaritas (M)", value=1.0, step=0.1)
        equivalent = st.number_input("Masukkan equivalent", value=1.0, step=0.1)
        normality = molarity * equivalent
        st.write("Normalitas: {:.4f} N".format(normality))
    elif operation == "PPM":
        st.title("Menghitung PPM")
        mass = st.number_input("Masukkan massa (mg)", value=1.0, step=0.1)
        volume = st.number_input("Masukkan volume (L)", value=1.0, step=0.1)
        solute_mass = st.number_input("Masukkan massa solute (g)", value=1.0, step=0.1)
        ppm = (mass / volume) * (10**6) / solute_mass
        st.write("PPM: {:.4f}".format(ppm))

if __name__ == "__main__":
    calculator()

