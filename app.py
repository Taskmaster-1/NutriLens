import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv


st.set_page_config(
    page_title="NutriLens - Nutrition Analysis",
    page_icon="🥗",
    layout="centered"
)


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def local_css():
    st.markdown("""
    <style>
    .main-header {
        color: #2c3e50;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 20px;
        background: linear-gradient(to right, #3498db, #2ecc71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subheader {
        color: #34495e;
        text-align: center;
        margin-bottom: 20px;
    }
    .stFileUploader {
        max-width: 600px;
        margin: 0 auto;
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #27ae60;
        transform: scale(1.05);
    }
    .result-box {
        background-color: #f7f9fc;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def get_gemini_response(input_prompt, image, input_text):
    """Generate response from Gemini API"""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_prompt, image[0], input_text])
    return response.text

def input_image_setup(uploaded_file):
    """Process uploaded image"""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type, 
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def main():
    
    local_css()
    
    
    st.markdown('<div class="main-header">NutriLens 🍽️</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Analyze Your Meal Nutrition Instantly</div>', unsafe_allow_html=True)
    
    
    input_text = st.text_input(
        "Additional Context (Optional):", 
        placeholder="E.g., I'm on a diet, Vegetarian meal, etc.",
        key="input"
    )
    
    
    uploaded_file = st.file_uploader(
        "Upload Your Meal Image", 
        type=["jpg", "jpeg", "png"],
        help="Upload a clear image of your meal"
    )
    
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        col1, col2, col3 = st.columns([1,6,1])
        with col2:
            st.image(image, caption="Your Uploaded Meal", use_container_width=True)
    
    
    input_prompt = """
    You are an expert nutritionist analyzing a meal image. 
    Calculate total calories and provide detailed breakdown:
    - List each food item
    - Calories for each item
    - Total calorie count
    - Brief nutritional insights
    """
    

    if st.button("Analyze Meal Nutrition", help="Click to get detailed nutritional breakdown"):
        try:
            
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input_text)
            
            
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("🍽️ Nutrition Analysis Results")
            st.write(response)
            st.markdown('</div>', unsafe_allow_html=True)
        
        except FileNotFoundError:
            st.error("Please upload an image first!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    main()