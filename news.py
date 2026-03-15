import streamlit as st
import requests
api_key = st.secrets["NEWS_API_KEY"]

st.title("WORLD'S TOP LATEST NEWS")

countries = {
    "India":"in",
    "United States":"us",
    "United Kingdom":"gb",
    "France":"fr",
    "Germany":"de",
    "Australia":"au"
}

country_name = st.selectbox("Select Country", list(countries.keys()))
con = countries[country_name]

languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Chinese": "zh"
}
language_name = st.selectbox("Select Language", languages.keys())
lan = languages[language_name]

st.write("Selected Country:", con)
st.write("Selected Language:", lan)

is_clicked= st.button('Search',use_container_width=True, type='primary')

if is_clicked:
    import requests
    res= requests.get(url= f"https://api.worldnewsapi.com/top-news?source-country={con}&language={lan}&api-key={api_key}")
    if res.status_code == 200 :
        data = res.json()

        top_news=data.get("top_news",[])
        if not top_news:
            st.write("no news avalaible")
        else:
            st.write("Latest news") 

            count=1
            for topic in top_news:
                articles=topic.get("news",[])
                for article in articles:
                    title=article.get("title")
                    description=article.get("text")
                    link=article.get("url")

                    st.write(f"{count},{title}")
                    st.write("description:",description)
                    st.write("read more:",link)
                    count+=1
    else:
        st.write("Error:",res.status_code)
            
