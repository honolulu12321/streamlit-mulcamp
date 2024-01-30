# -*- coding:utf-8 -*-
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
@st.cache_data
def cal_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue
# 데이터 불러오기
@st.cache_data
def load_data():
    df = sns.load_dataset('iris')
    return df
def plot_matplotlib(df):
    st.title('Scatter Plot with Matplotlib')
    fig, ax = plt.subplots()
    ax.scatter(df['sepal_length'], df['sepal_width'])
    st.pyplot(fig)
def plot_seaborn(df):
    st.title('Scatter Plot with Seaborn')
    fig, ax = plt.subplots()
    sns.scatterplot(df, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig)
def plot_plotly(df):
    st.title('Scatter Plot with Plotly')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x = df['sepal_length'],
                   y = df['sepal_width'],
                   mode='markers')
    )
    st.plotly_chart(fig)