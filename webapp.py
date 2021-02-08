import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pydeck as pdk
import plotly.express as px
import altair as alt

URL = ("/Users/Dell/zom.csv")

st.markdown("## 𝓩𝓸𝓶𝓪𝓽𝓸, 𝓽𝓸 𝓽𝓱𝓮 𝔀𝓸𝓻𝓵𝓭 𝓬𝓾𝓲𝓼𝓲𝓷𝓮𝓼")
st.markdown("###### All you can know here about ✎Cost ✎Address ✎Rating ✎Review ✎Location ✎Currency ✎Cuisines ✎Votes")
st.markdown("###  ᴍʀɪɴᴀʟ ᴍᴀʏᴀɴᴋ , ᴄʜᴀɴᴅɪɢᴀʀʜ ᴜɴɪᴠᴇʀꜱɪᴛʏ. ᴳʳᵉᵉᵗⁱⁿᵍˢ ᵗᵒ ᵃˡˡ .")
st.markdown("HOLA! Welcome to my virtual restaurant .Here you will be enjoying the world tour to the  delicious cuisines all over the world by Zomato. Get the mouth watering taste all over the globe and and enjoy your virtual ride . Hope to see you soon after the trip . Get there and enjoy.")
def load():
    data=pd.read_csv(URL)
    return data
data= load()
if st.checkbox(" ᴄʟɪᴄᴋ ᴛᴏ ꜱᴇᴇ ʀᴀᴡ ᴅᴀᴛᴀ ",False):
    st.markdown("###### THIS IS THE RAW DATA FOR ALL COMPARISONS AND GRAPH")
    st.write(data)


pict = Image.open('webpic2.jpg')
st.sidebar.image(pict, use_column_width=True)
pic = Image.open('food.png')
st.image(pic, use_column_width=True)



st.sidebar.markdown("### RATING OUT OF ★★★★★")
rate=st.sidebar.slider("slide to see the rating in the global places ",0.0,5.0)
st.sidebar.map(data.query("Rating >= @rate")[["lon","lat"]].dropna(how="any"))


st.markdown("### THE BUBBLE COMPARIOSON")
st.markdown("This is the rating of the top 200 restaurants in terms of price range . Here in the Y axis the size of the bubble describes the rating which scattered over the pool of the  price range .")
df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['Restaurant_Name', 'Rating', 'Price_Range'])
st.vega_lite_chart(df, {
     'mark': {'type': 'circle', 'tooltip': 500},
     'encoding': {
         'x': {'field': 'Restaurant_Name', 'type': 'quantitative'},
         'y': {'field': 'Price_Range', 'type': 'quantitative'},
         'size': {'field': 'Rating', 'type': 'quantitative'},
         'color': {'field': 'Rating', 'type': 'quantitative'},
     },
 },use_container_width=200)




st.markdown("### RESTAURANT REVIEWS / COST & MORE")
select=st.selectbox('Select the options to view details about your favourite restaurant', ['Cuisines' , 'Address','Review','City','Currency', 'Average cost'])
if select == 'Cuisines':
    st.write(data.query("Cuisines >= Cuisines")[["Restaurant_Name","Cuisines"]])
elif select == 'Address':
    st.write(data.query("Address >= Address")[["Restaurant_Name","Address"]])
elif select == 'Review':
    st.write(data.query("Review>= Review")[["Restaurant_Name","Review"]])
elif select == 'City':
    st.write(data.query("City >= City")[["Restaurant_Name","City"]])
elif select == 'Currency':
    st.write(data.query("Currency >= Currency")[["Restaurant_Name","Currency"]])
else :
    st.write(data.query("cost_for_two >= cost_for_two")[["Restaurant_Name","cost_for_two"]])



st.sidebar.markdown('______________________________________')
sel=st.sidebar.selectbox('See the votes of top restautants', ['Top 50','50 to 100','101 to 150','151 to 200','201 to 250'])
if sel=='Top 50':
    hist_values = np.histogram(
       data['Votes'], bins =50, range=(0,200))[0]
    st.sidebar.bar_chart(hist_values)

elif sel=='50 to 100':
      hist_values = np.histogram(
         data['Votes'], bins =50, range=(51,100))[0]
      st.sidebar.bar_chart(hist_values)

elif sel=='101 to 150':
      hist_values = np.histogram(
         data['Votes'], bins =50, range=(51,100))[0]
      st.sidebar.bar_chart(hist_values)

elif sel=='151 to 200':
      hist_values = np.histogram(
         data['Votes'], bins =50, range=(51,100))[0]
      st.sidebar.bar_chart(hist_values)
elif sel=='201 to 250':
      hist_values = np.histogram(
         data['Votes'], bins =50, range=(201,250))[0]
      st.sidebar.bar_chart(hist_values)
else:
     hist_values = np.histogram(
        data['Votes'], bins =50, range=(250,300))[0]
     st.sidebar.bar_chart(hist_values)

st.markdown("-----------------------------------------")
st.markdown("### COMPARE 9000+ RESTAURANTS WITH THIS TOOL")
get = st.multiselect('Select any restaurants from the list to compare  ', data['Restaurant_Name'].unique())
col1 = st.selectbox('select feature on y', data.columns[10:21])
col2 = st.selectbox('Select feature to show by colour', data.columns[10:21])
new_df = data[(data['Restaurant_Name'].isin(get))]
st.write(new_df)
fig = px.scatter(new_df, y =col1,x= 'Restaurant_Name', color =col2)
st.plotly_chart(fig)


st.markdown("#### THIS GRAPH SHOWS STATISTICS OF THREE GROUP COMPARISON")
df = pd.DataFrame(np.random.randn(50, 3),columns=['Rating','Price_Range','Votes'])
columns = st.multiselect(label='Select to see rating vs price vs votes of top 50 restaurants(see names in raw data list) ', options=df.columns)
st.line_chart(df[columns])


st.markdown("---------------------------------")
st.markdown("##  𝒲𝑜𝒽𝑜𝑜 ! 𝒜𝓁𝓁 𝒹𝑜𝓃𝑒. ✌︎ ✌︎ ✌︎")
st.sidebar.markdown("---------------------------------")
st.sidebar.markdown("### 𝑨𝒃𝒐𝒖𝒕 𝒄𝒓𝒆𝒂𝒕𝒐𝒓")
st.sidebar.markdown(" Hello everyone , I'm Mrinal Mayank from Chandigarh University . This is my first web application with python . I had tried my every aspect to make it user friendly . I hope you like it .")
