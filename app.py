import joblib
import streamlit as st    
import pandas as pd

st.set_page_config(page_icon='❤️',page_title='Heart Disease Prediction',layout='wide')

with st.sidebar:
    st.title('Heart Disease Prediction')

df=pd.read_csv('cleaned_data.csv')
with open('Log_model.joblib','rb') as file:
    model=joblib.load(file)
    
with st.container(border=True):
    col1,col2=st.columns(2)
    with col1:
        age=st.number_input('Age:',min_value=1,max_value=100,step=5)
        gender=st.radio('Gender:',options=['male','female'],horizontal=True)
        gender=1 if gender=='male' else 0
        d={'Typical angina':0,'Atypical angina':1,'non-anginal pain':2,'Asymptotic':3}
        chest_pain_type=st.selectbox('Chest pain type',options=d.keys())
        chest_pain_type=d[chest_pain_type]
        resting_bp=st.number_input('Resting BP:',min_value=50,max_value=200,step=10)
        cholestrol=st.number_input('Cholestrol:',min_value=50,max_value=600,step=20)
        fbs=st.radio('Fasting blood sugar:',options=['yes','no'],horizontal=True)
        fbs=1 if fbs=='yes' else 0
        
    with col2:
        d1={'normal':0,'having ST-T wave abnormality':1,'left ventricular hypertrophy':2}
        restecg=st.selectbox('Resting ECG:',options=d1.keys())
        restecg=d1[restecg]
        max_heart=st.number_input('Maximun_heart_rate:',min_value=50,max_value=250,step=5)
        exang=st.radio('Exercise Induced Angina:',options=['yes','no'],horizontal=True)
        exang=1 if exang=='yes' else 0
        oldpeak=st.number_input("OldPeak:",min_value=0.0,max_value=10.0,step=1.0)
        d2={'upsloping':0,'flat':1,'downsloping':2}
        slope=st.selectbox('Slope:',options=d2.keys())
        slope=d2[slope]
        num_vessels=st.selectbox('Number of Major vessels:',options=[0,1,2,3])
        d3={'normal':1,'fixed defect':2,'reversable defect':3}
        thal=st.selectbox('THAL:',options=d3.keys())
        thal=d3[thal]
if st.button('predict'):
    data=[[age,gender,chest_pain_type,resting_bp,cholestrol,fbs,restecg,max_heart,exang,oldpeak,slope,num_vessels,thal]]
    pred=model.predict(data)[0]
    
    if pred==0:
        st.subheader('low risk of heart disease')
        st.image('heart2.jpeg',width=200)
    else:
        st.subheader('High risk of heart disease')
        st.image('heart1.jpeg',width=200)       