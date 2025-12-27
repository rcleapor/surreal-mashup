import streamlit as st
from openai import OpenAI

# 1. Setup the Title and Description
st.title("Richard's Surrealist Mash-Up Tool")
st.write("Pick your favorite masters and create a new dreamscape!")

# 2. Artist Selection (The "Mash-Up" Menu)
artists = st.multiselect(
    "Which artists should we blend together?",
    ["Salvador Dalí", "René Magritte", "Max Ernst", "Giorgio de Chirico"],
    default=["Salvador Dalí", "René Magritte"]
)

# 3. Setting the Scene
user_input = st.text_input("Describe one specific thing to include (e.g., 'a dog named Jim' or 'a flying clock'):")

# 4. The "Magic" Button
if st.button("Generate My Surrealist Masterpiece"):
    if not artists:
        st.error("Please pick at least one artist!")
    else:
        # Constructing the prompt for the AI
        artist_string = " and ".join(artists)
        full_prompt = f"A surrealist painting in the combined styles of {artist_string}. Featured subject: {user_input}. Dreamlike, high detail, oil painting texture."
        
        st.info(f"Generating your {artist_string} mash-up...")
        
        # This part connects to the AI to draw the picture
        # (You will put your API key in the settings later)
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=full_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        st.image(image_url, caption=f"Your {artist_string} Mash-Up")
