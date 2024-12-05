import pickle
import streamlit as st
import numpy as np
st.header("ONLINE RETAIL RECOMMENDATION SYSTEM")

model = pickle.load(open('ORRS/model.pkl','rb'))
name = pickle.load(open('ORRS/name.pkl','rb'))
fin_Retail = pickle.load(open('ORRS/fin_Retail.pkl','rb'))
pivot = pickle.load(open('ORRS/pivot.pkl','rb'))

def fecth_poster(suggestion):
    retails_name = []
    id_index = []
    poster_url = []
    for retail_id in suggestion:
        retails_name.append(pivot.index[retail_id])
        
    for i in retails_name[0]:
        id = np.where(fin_Retail['Description'] == name)[0][0]
        id_index.append(id)
        
    for id in id_index:
        url = fin_Retail.iloc[id]['CustomerID']
        poster_url.append(url)
    return poster_url
        
def recom_retail(retail_name):
    retail_list = []
    retail_id = np.where(pivot.index == retail_name)[0][0]
    distance, suggestion = model.kneighbors(pivot.iloc[retail_id,:].values.reshape(1,-1),n_neighbors=6)
    
    # poster_url = fecth_poster(suggestion)
    for i in range(len(suggestion)):
        retails = pivot.index[suggestion[i]]
        for j in retails:
            retail_list.append(j)
    return retail_list

select = st.selectbox("Search the product to select",name)
if st.button("Show Recommendation"):
    recommendation = recom_retail(select)
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        st.text(recommendation[1])
        # st.image(poster_url[1])
    with col2:
        st.text(recommendation[2])
        # st.image(poster_url[2])
    with col3:
        st.text(recommendation[3])
        # st.image(poster_url[3])
    with col4:
        st.text(recommendation[4])
        # st.image(poster_url[4])
    with col5:
        st.text(recommendation[5])
        # st.image(poster_url[5])