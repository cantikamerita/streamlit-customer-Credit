import streamlit as st
import pickle
import os

# Tentukan jalur file
file_path = 'credit_customers.sav'  # Jalur relatif jika file berada di direktori yang sama
# file_path = '/path/to/your/file/credit_customers.sav'  # Jalur absolut jika file berada di direktori lain

# Verifikasi dan memuat model
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        Customer_Credit_model = pickle.load(file)
else:
    st.error(f"File tidak ditemukan: {file_path}")
    st.stop()  # Hentikan eksekusi jika file tidak ditemukan

# Judul web
st.title('Prediksi Customer Credit')

# Membagi Kolom
col1, col2 = st.columns(2)

with col1:
    checking_status = st.text_input('Input Checking Status')

with col2:
    duration = st.text_input('Input Duration')

with col1:
    credit_history = st.text_input('Input Credit History')

with col2:
    credit_amount = st.text_input('Input Credit Amount')

with col1:
    savings_status = st.text_input('Input Saving Status')

with col2:
    employment = st.text_input('Input Employment')

with col1:
    installment_commitment = st.text_input('Input Installment Commitment')

with col2:
    personal_status = st.text_input('Input Personal Status')

with col1:
    other_parties = st.text_input('Input Other Parties')

with col2:
    residence_since = st.text_input('Input Residence Since')

with col1:
    age = st.text_input('Input Age')

with col2:
    housing = st.text_input('Input Housing')

with col1:
    existing_credits = st.text_input('Input Existing Credits')

with col2:
    job = st.text_input('Input Job')

with col1:
    num_dependents = st.text_input('Input Num Dependents')

with col2:
    own_telephone = st.text_input('Input Own Telephone')

# Code untuk prediksi
CustomerCredit_prediksi = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Customer Credit'):
    try:
        prediction = Customer_Credit_model.predict([[
            checking_status, duration, credit_history, credit_amount, savings_status,
            employment, installment_commitment, personal_status, other_parties, residence_since,
            age, housing, existing_credits, job, num_dependents, own_telephone
        ]])
        if prediction[0] == 1:
            CustomerCredit_prediksi = 'Customer dengan History Kredit yang Baik'
        else:
            CustomerCredit_prediksi = 'Customer dengan History Kredit yang Buruk'
        st.success(CustomerCredit_prediksi)
    except Exception as e:
        st.error(f"Error dalam prediksi: {e}")
