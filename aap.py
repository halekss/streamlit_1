import streamlit as st
st.title("Good Morning VIEEEETNAAAAAM !!!!")

quartier = st.selectbox("Indiquez votre arrondissement de récupération", ['Manhattan', 'Bronx', 'Queens', "Hell's Kitchen", 'Arkham', 'Upper East Side', '1725 Slough Avenue'])

st.write(f"Tu as choisis: {quartier}")

if quartier == 'Manhattan':
    st.image("https://images.unsplash.com/photo-1541336032412-2048a678540d?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
elif quartier == 'Bronx':
    st.image("https://images.unsplash.com/photo-1689783101576-627f2fbdb8d5?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
elif quartier == 'Queens':
    st.image("https://images.unsplash.com/photo-1550860759-22105316bc44?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
elif quartier == "Hell's Kitchen":
    st.image("https://i0.wp.com/w42st.com/wp-content/uploads/2020/12/1428540804-DareDevil_2048x1152.jpg?resize=780%2C439&ssl=1")
elif quartier == 'Arkham':
    st.image("https://fr.web.img6.acsta.net/r_654_368/newsv7/20/07/31/12/25/4798126.jpg")
elif quartier == 'Upper East Side':
    st.image("https://sf1.afcdn.com/wp-content/uploads/aufeminin/2025/04/16683_w657h378.jpg")
elif quartier == '1725 Slough Avenue':
    st.image("https://media.licdn.com/dms/image/v2/D5612AQGqPGHORIsa-g/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1691871730624?e=2147483647&v=beta&t=HT4mUN4oFnzQAJ7wz1X7pDqRp38vifBP8d9SkyG7hW4")
    
st.write("Je ne me suis pas servi du dataframe parce que de 1: ce n'est pas expliqué. 2: c'est plus fun comme ça.")
