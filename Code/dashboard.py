import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Medical Appointments Dashboard", layout="wide")

med = pd.read_csv("medical_appointments_updated.csv")
total_patients = len(med)

fig_pie = px.pie(med, names='No-show', title='Percentage of Attended vs No-show',
                 color_discrete_sequence=["#327B64","#B14A4A"], hole=0.4)

sms_counts = med.groupby(['SMS_received','No-show']).size().reset_index(name='Count')
fig_sms = px.bar(sms_counts, x='SMS_received', y='Count', color='No-show', 
                 barmode='group', title='Effect of SMS Reminder on No-show (Count)',
                 text='Count', labels={'SMS_received':'SMS Received', 'Count':'Number of Appointments'},
                 color_discrete_sequence=["#327B64","#B14A4A"])

fig_gender = px.histogram(med, x='Gender', color='No-show', barmode='group',
                          title='No-show by Gender',
                          color_discrete_sequence=["#327B64","#B14A4A"])

top = med['Neighbourhood'].value_counts().head(10).reset_index()
top.columns = ['Neighbourhood','Count']
fig_neigh = px.bar(top, x='Count', y='Neighbourhood', orientation='h',
                   title='Top 10 Neighbourhoods with Appointments',
                   text='Count', color='Neighbourhood',  
                   color_discrete_sequence=px.colors.qualitative.Dark2)

age_counts = med.groupby(['Age','No-show']).size().reset_index(name='Count')
fig_age = px.line(age_counts, x='Age', y='Count', color='No-show',
                  color_discrete_sequence=["#327B64","#B14A4A"],
                  title='Number of Appointments by Age and No-show',
                  markers=True)

wait_counts = med.groupby(['WaitingDays','No-show']).size().reset_index(name='Count')
wait_counts = wait_counts[wait_counts['WaitingDays'] <= 60]
fig_wait = px.bar(wait_counts, x='WaitingDays', y='Count', color='No-show', 
                  barmode='group',
                  title='Number of Appointments by Waiting Days and No-show',
                  text='Count',
                  labels={'WaitingDays':'Waiting Days', 'Count':'Number of Appointments'},
                  color_discrete_sequence=["#327B64","#B14A4A"])

st.title("Medical Appointments Dashboard")
st.subheader(f"Total Number of Patients: {total_patients}")


col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_pie, use_container_width=True)
with col2:
    st.plotly_chart(fig_sms, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_gender, use_container_width=True)
with col2:
    st.plotly_chart(fig_neigh, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_age, use_container_width=True)
with col2:
    st.plotly_chart(fig_wait, use_container_width=True)