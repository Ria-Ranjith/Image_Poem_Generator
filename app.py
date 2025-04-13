import google.generativeai as genai
import gradio as gr
from PIL import Image
import os

# Load API key
google_api_key = "AIzaSyDEMtR6ZiTTg87av13iHMkUuKin3JeKXbI"  # Replace with your actual Google API key
genai.configure(api_key=google_api_key)

def generate_multilingual_poem(image, selected_languages, length, style):
    """Generate poems in selected languages based on the image and preferences."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    img = Image.open(image)
    
    poems = {}
    for lang in selected_languages:
        prompt = (
            f"Write a {length.lower()} {style.lower()} poem in {lang} inspired by the uploaded image. "
            f"Be creative and poetic."
        )
        response = model.generate_content([img, prompt])
        poems[lang] = response.text.strip()
    
    return poems

# Language options (you can expand this list)
language_choices = ['English', 'Spanish', 'French', 'German', 'Hindi', 'Chinese']

# Gradio UI
iface = gr.Interface(
    fn=generate_multilingual_poem,
    inputs=[
        gr.Image(type="filepath", label="Upload an Image"),
        gr.CheckboxGroup(choices=language_choices, label="Select Languages"),
        gr.Radio(choices=["Short", "Medium", "Long"], label="Poem Length", value="Medium"),
        gr.Radio(choices=["Free Verse", "Haiku", "Sonnet"], label="Poem Style", value="Free Verse"),
    ],
    outputs=gr.JSON(label="Generated Poems"),
    title="🌍 Multilingual Poem Generator from Image",
    description="Upload an image, select languages, poem style, and length. Get artistic poems in multiple languages.",
    theme="default",
)

if __name__ == "__main__":
    iface.launch()
