import streamlit as st
from deep_translator import MyMemoryTranslator
from gtts import gTTS
import io

st.set_page_config(page_title="Language Translation Tool", page_icon="🌐", layout="centered")

st.title("🌐 Language Translation Tool")
st.write("Translate text instantly into multiple languages.")

# Supported language codes for MyMemory Translator
languages = {
    'English': 'en-GB',
    'Bengali': 'bn-IN',
    'Spanish': 'es-ES',
    'French': 'fr-FR',
    'German': 'de-DE',
    'Hindi': 'hi-IN',
    'Arabic': 'ar-SA',
    'Japanese': 'ja-JP',
    'Russian': 'ru-RU'
}

col1, col2 = st.columns(2)
with col1:
    source_lang_name = st.selectbox("Select Source Language", options=list(languages.keys()), index=0)
with col2:
    target_lang_name = st.selectbox("Select Target Language", options=list(languages.keys()), index=1)

input_text = st.text_area("Enter text to translate:", height=150, placeholder="Type your text here...")

if st.button("Translate", type="primary"):
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            source_code = languages[source_lang_name]
            target_code = languages[target_lang_name]
            
            translated_result = MyMemoryTranslator(source=source_code, target=target_code).translate(input_text)
            
            st.subheader("Translated Output:")
            st.success(translated_result)
            
            # Text-to-Speech (Target short code extraction)
            try:
                short_lang = target_code.split('-')[0]
                tts = gTTS(text=translated_result, lang=short_lang)
                audio_bytes = io.BytesIO()
                tts.write_to_fp(audio_bytes)
                st.audio(audio_bytes.getvalue(), format="audio/mp3")
            except Exception:
                pass
                
        except Exception as e:
            st.error(f"Error occurred: {e}")