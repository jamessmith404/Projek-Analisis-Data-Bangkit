import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

day_df = pd.read_csv('clean_day.csv')
hour_df = pd.read_csv('clean_hour.csv')

q1_df = day_df.groupby(by='mnth').agg({
    "cnt": "sum",
    "casual": "sum",
    "registered": "sum"
})

clusters = day_df["weathersit"]

q2_df = day_df[["atemp", "cnt"]]

q3_df = day_df.groupby(by='season').agg({
    "cnt": "sum",
    "casual": "sum",
    "registered": "sum"
})

# Create a sidebar selectbox for the plots
plot = st.sidebar.selectbox(
    'Which plot do you want to display?',
    ('Pengguna Bulanan Aplikasi', 'Sebaran Jumlah Pengguna dengan Suhu yang Terasa', 'Pengguna Aplikasi Tiap Musim')
)

if plot == 'Pengguna Bulanan Aplikasi':
    st.subheader("Pengguna Bulanan Aplikasi")
    sns.set_palette(sns.color_palette())
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x="mnth", y="cnt", data=q1_df, ax=ax1)
    for i, v in enumerate(q1_df['cnt']):
       ax1.text(i, v + 0.2, str(v), ha='center')
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Pelanggan")
    st.pyplot(fig1)

elif plot == 'Sebaran Jumlah Pengguna dengan Suhu yang Terasa':
    st.subheader("Sebaran Jumlah Pengguna dengan Suhu yang Terasa")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x=(q2_df["atemp"]*50), y=q2_df["cnt"], hue=clusters, ax=ax2)
    plt.xlabel("Suhu yang Terasa (dalam Celcius)")
    plt.ylabel("Jumlah Pelanggan")
    st.pyplot(fig2)

elif plot == 'Pengguna Aplikasi Tiap Musim':
    st.subheader("Pengguna Aplikasi Tiap Musim")
    sns.set_palette(sns.color_palette())
    cols = ['grey' if (x < max(q3_df['cnt'])) else 'orange' for x in q3_df['cnt']]
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(x="season", y="cnt", data=q3_df, palette=cols, ax=ax3)
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Pelanggan")
    st.pyplot(fig3)