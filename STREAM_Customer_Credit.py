import streamlit as st
import pickle
import os

# Verifikasi dan memuat model
file_path = 'credit_customers.sav'
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        Customer_Credit_model = pickle.load(open('credit_customers.sav', 'rb'))
else:
    st.error(f"File not found: {file_path}")

# judul web
st.title('Prediksi Customer Credit')

checking_status = st.text_input('1. Input Checking Status ( 0.0 = Checking ; 1.0 = No Checking)')

duration = st.text_input('2. Input Duration')

credit_history = st.text_input('3. Input Credit History ( 0.0 = all paid , 1.0 = existing paid ,2.0 = delayed previously , 3.0 = critical/other existing credit)')

credit_amount = st.text_input('4. Input Credit Amount')

savings_status = st.text_input(' 5. Input Saving Status (  0.0 = no known savings, 1.0 = there are known savings )')

employment = st.text_input( '6. Input Employment ( 0.0 = unemployed , 1.0 = working  )')

installment_commitment = st.text_input('7. Input Installment Comitment')

personal_status = st.text_input('8. Input Personal Status ( 0.0 = married , 1.0 = single )')

other_parties = st.text_input('9. Input Other Parties ( 0.0 = co applicant ,1.0 = guarantor, 2.0 = none )')

residence_since = st.text_input('10. Input Residence Since')

age = st.text_input('11. Input Age')

housing = st.text_input('12. Input Housing ( 0.0 = for free , 1.0 = own )')

existing_credits = st.text_input('13. Input Existing Credits')

job = st.text_input('14. Input Job ( 0.0 = skilled , 1.0 = unskilled )')

num_dependents = st.text_input('15. Input Num Dependents')

own_telephone = st.text_input('16. Input Own Telephone ( 0.0 = none , 1.0 = yes)')

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

