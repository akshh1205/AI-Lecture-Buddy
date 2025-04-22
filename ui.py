import streamlit as st
from yt_transcript import get_transcript
from summarizer import summarize_text

st.set_page_config(page_title="AI Lecture Buddy - YouTube Summarizer", layout="centered")
st.title("🎓 AI Lecture Buddy – YouTube Video Summarizer")

yt_url = st.text_input("📺 Enter a YouTube Video URL")

if st.button("Summarize"):
    if yt_url:
        with st.spinner("🎙️ Fetching transcript..."):
            transcript = get_transcript(yt_url)

        if transcript.startswith("Error"):
            st.error(transcript)
        else:
            st.success("✅ Transcript fetched! Now summarizing...")
            with st.spinner("🧠 Summarizing..."):
                summary = summarize_text(transcript)
                st.markdown("### 📝 Summary:")
                st.write(summary)

                st.download_button("💾 Download Summary as TXT", summary, file_name="lecture_summary.txt")
    else:
        st.warning("Please paste a valid YouTube video URL.")
 