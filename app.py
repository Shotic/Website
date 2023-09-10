import streamlit as st
from PIL import Image

# assets 
img_contact_f = Image.open("images/1.jpg")

img_contact_r = Image.open("images/2.jpg")


st.set_page_config(page_title="Miss na kita", page_icon="😓", layout="wide")

st.subheader("Hi, miss na miss na kita ay hayayayyayayyayayyaaa")

st.title("Missyou")

st.write("Missnamissnakita")

st.write("[Click me para makita mo gf ko](https://cdn.discordapp.com/attachments/1011582106775867452/1150309715339923456/received_6318941761535002.jpg)")


with st.container():
    st.write("---")
    left_c, right_c = st.columns(2)
    with left_c:
        st.header("Sino ako?")
        st.write("##")
        st.write(
        """
        Sino nga ba ako?
        
        -Hotdog seller ng isang particular na babae
            
        -miss na kita
            
        -Anong English ng baka? Cow
        Eh ng karne? Meat
        MEAT na kita Baby hindi ko na kaya. Sobrang saya ko na muli tayong magsasama.🎶
                
        -okay next joke
        """
        )
    st.write("##")
    st.write ("[Tignan mo kung gaano siya ka ganda ohhh](https://cdn.discordapp.com/attachments/1011582106775867452/1150274329993555968/360196538_180172795043632_7694469735070664522_n.jpg)")

with st.container():
    st.write("---")
    st.header("Showcase: ")
    st.write("##")
    image_c, text_c = st.columns((1, 2))
    with image_c:
        st.image(img_contact_f)
    with text_c:
        st.subheader("Kita mo yan bbq yan")
        st.write(
        """
        Bbq ko yan
        
        Bff ko den yan
        
        Ganda noh?
        
        Swerte ko heh
        
        Olats lahat ng mga babae jan tsk tsk tignan nyo naman kung gaano ka ganda ohhh
        
        """
        )
    
with st.container():
    st.write("---")
    st.header("Bakit ko ginawa tong website na to?")
    st.write("##")
    st.write(
    """
    -Mga dahilan:
    
    - miss ko na bbq
    
    - nangungulila na ako
    
    - isang daang taon ko na di nakikita(nagkita lang kami nung saturday)
    
    - miss ko na presensya niya
    
    - miss ko na boses niya
    
    - miss ko na buhok niya
    
    - miss ko na ngiti niya
    
    """
    )

with st.container():
    st.write("---")
    st.header("Mga kinakatakutan ko:")
    st.write("##")
    st.write(
    """
    -Mga kinakatakutan ko:
    
    - May kasama na siyang iba
    
    - May nagpapayong na sakanya na ibang tao na lalaki
    
    - May makatabi na sporty tall and handsome at varsity na smart pa na classmate (Lugi na tayo dun olats nako)
    
    - May iba na siyang hotdog seller
    
    """
    )
    
with st.container():
    st.write("---")
    st.header("Number 1 bb niya: ")
    st.write("##")
    image_d, text_f = st.columns((1, 2))
    with text_f:
        st.subheader("Number 1 bb niya yan")
        st.write(
        """
        Olats ako jan par wala yun lang olats talaga
        """
        )
    with image_d:
        st.image(img_contact_r)
        
with st.container():
    st.write("---")
    st.header("More Info")
    st.write("##")
    st.write(
    """
    -Birthday niya is July 28
    
    -Favorite thing to do is:
    
    - Sleep
    
    - Sing
     
    -Favorite ng bbq na artist is si Taylor Swift
    
    - Mama niya nga daw eh
    
    
    -Hotdog seller niya ako
    
    -Madami din gf yan
    - Richelle
    - Stella
    - Classmate niya (Di ko alam pangalan😅😅)
    
    """
    )
    
st.subheader("The end")

st.title("MORE:")

st.write("Gusto ko lang sabihin matagal na nung nakailang araw poa na pero ang hirap sabihin na ano na nga yun basta ano uli tawag dun hmmmmmm....... waiit iisipin ko pa..........ahhh yun alam ko na..... miss na kita")
