import streamlit as st
import pickle
import os

# Verifikasi dan memuat model
file_path = 'credit_customers.sav'
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        Customer_Credit_model = pickle.load(open(credit_customers.sav', 'rb'))
else:
    st.error(f"File not found: {file_path}")

# judul web
st.title('Prediksi Customer Credit')

# membagi Kolom
col1, col2 = st.columns(2)

with col1 :
    checking_status = st.text_input('Input Checking Status ( 0.0 = Checking ; 1.0 = No Checking)')

with col2 :
    duration = st.text_input('Input Duration')

with col1 :
    credit_history = st.text_input('Input Credit History ( 1.0 = existing paid , 3.0 = critical/other existing credit , 0.0 = all paid , 2.0 = delayed previously )')

with col2 :
    credit_amount = st.text_input('Input Credit Amount')

with col1 :
    savings_status = st.text_input('Input Saving Status ( 1.1 = there are known savings , 0.0 = no known savings )')

with col2 :
    employment = st.text_input('Input Employment ( 1.0 = working , 0.0 = unemployed )')

with col1 :
    installment_commitment = st.text_input('Input Installment Comitment')

with col2 :
     personal_status = st.text_input('Input Personal Status ( 1.0 = single , 0.0 = married)')

with col1 :
    other_parties = st.text_input('Input Other Parties ( 2.0 = none , 1.0 = guarantor , 0.0 = co applicant)')

with col2 :
    residence_since = st.text_input('Input Residence Since')

with col1 :
    age = st.text_input('Input Age')

with col2 : 
    housing = st.text_input('Input Housing ( 1.0 = own , 0.0 = for free)')

with col1 :
    existing_credits = st.text_input('Input Existing Credits')

with col2 :
    job = st.text_input('Input Job ( 0.0 = skilled , 1.0 = unskilled )')

with col1 :
    num_dependents = st.text_input('Input Num Dependents')

with col2 :
    own_telephone = st.text_input('Input Own Telephone ( 1.0 = yes , 0.0 = none )')

# Code untuk prediksi
CustomerCredit_prediksi = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Customer Credit'):
    CustomerCredit_prediksi = Customer_Credit_model.predict([[checking_status, duration, credit_history, credit_amount, savings_status, employment, installment_commitment, personal_status, other_parties, residence_since, age, housing, existing_credits, job, num_dependents, own_telephone]])

    if(CustomerCredit_prediksi[0] == 1):
        CustomerCredit_prediksi = 'Customer dengan History Kredit yang Baik'
    else:
        CustomerCredit_prediksi = 'Customer dengan History Kredit yang Buruk'
        
    st.success(CustomerCredit_prediksi)

