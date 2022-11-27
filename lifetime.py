import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.header("hove many weeks you have in your life")
gh=st.date_input(label="enter your brithday")
st.write(gh)
from datetime import date
from datetime import datetime
now = datetime.now()
now=now.strftime("%d/%m/%Y")
d,m,y=list(map(int,now.split("/")))
d0 = gh
d1 =date(y, m, d)
delta = d1 - d0
last=delta.days
st.write(last)
if last!=0:
    sns.set(rc = {'figure.figsize':(14,14)})
    num=np.zeros(72)
    df=pd.DataFrame(num)
    df.rename({0:"1"},axis=1,inplace=True)
    for i in range(2,73):
        df["{}".format(i)]=num
    goal=round(last/7)
    g=0
    for x in df.columns:
        if g==goal:
            break
        for i in list(df[x].index):
            g=g+1
            df[x][i]=1.0
            if g==goal:
                break
    print("suriya")
    fig=plt.figure(figsize=(14,14))
    sns.heatmap(df,annot=True,cmap="Blues",cbar=False)
    plt.title("time")
    st.pyplot(fig)
    print("sss")
    print("sdflk")