import pickle 
import streamlit as st

#baca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

col1,col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input('Nilai Pregnancies : ')
with col2 :    
    Glucose = st.text_input('Nilai Glucose : ')
with col1 :
    BloodPressure = st.text_input('Nilai Blood Pressure : ')
with col2 : 
    SkinThickness = st.text_input('Nilai Skin Thickness : ')
with col1 :
    Insulin = st.text_input('Nilai Insulin : ')
with col2 : 
    BMI = st.text_input('Nilai BMI : ')
with col1 :
    DiabetesPedigreeFunction = st.text_input('Nilai Diabetes Pedigree Function : ')
with col2 : 
    Age = st.text_input('Nilai Age : ')

# code utk prediksi 
diab_diagnosis = ''

# tombol submit utk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    if (diab_prediction[0]==0):
        diab_diagnosis = 'Pasien Kena Diabetes'
    else:
        diab_diagnosis = 'Pasien Tidak Diabestes'

    st.success(diab_diagnosis)
