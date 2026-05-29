import streamlit as st
import matplotlib.pyplot as plt
import PyPDF2
import re
import nltk
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# --- NLTK RESOURCES ---
@st.cache_resource
def download_nltk_data():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

download_nltk_data()

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title='AI Resume Analyzer', page_icon='📄', layout='wide')

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---

def extract_text_from_pdf(uploaded_file):
    try:
        text_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in text_reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def extract_keywords(text, top_n=10):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
    return Counter(filtered_words).most_common(top_n)

def get_missing_skills(resume_text, job_text):
    resume_words = set(word_tokenize(resume_text.lower()))
    job_words = set(word_tokenize(job_text.lower()))
    missing = job_words - resume_words
    return list(missing)[:15]

def analyze_resume_strength(resume_text):
    sections = ["education", "experience", "skills", "projects", "certifications", "summary", "languages"]
    found = [section.capitalize() for section in sections if section in resume_text.lower()]
    return found

def calculate_similarity(resume_text, job_description):
    resume_processed = remove_stopwords(preprocess_text(resume_text))
    job_processed = remove_stopwords(preprocess_text(job_description))
    
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform([resume_processed, job_processed])
    
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
    return round(score, 2), resume_processed, job_processed

# --- MAIN APP ---

def main():
    # --- Header Section Styling ---
    st.markdown("""
    <div style="background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%); padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 25px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);">
        <h1 style="color: white; font-family: 'Helvetica Neue', sans-serif; margin-bottom: 0;">📄 AI Resume Analyzer</h1>
        <p style="color: white; font-size: 1.2rem; opacity: 0.9; font-weight: 300; margin-top: 10px;">
            🚀 Upload your resume and discover how well it matches your dream job!
        </p>
    </div>
     """, unsafe_allow_html=True)
    
    # Sidebar Info
    with st.sidebar:
        st.header('📌 About This Tool')
        st.success("""
        - **Match Score:** Uses Cosine Similarity.
        - **Keyword Extraction:** Finds top job terms.
        - **Gap Analysis:** Identifies missing skills.
        """)
        st.divider()
        st.write("💡 *Tip: Make sure your PDF is not an image scan.*")

    # Layout: Two columns for inputs
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📤 Step 1: Upload Resume")
        uploaded_file = st.file_uploader('Choose a PDF file', type=['pdf'])
    
    with col2:
        st.subheader("📝 Step 2: Job Description")
        job_description = st.text_area('Paste the job requirements here', height=200)

    if st.button('🔍 Analyze Match', use_container_width=True):
        if uploaded_file and job_description:
            with st.spinner('⏳ Analyzing your profile against the job description...'):
                
                # Extraction
                resume_raw_text = extract_text_from_pdf(uploaded_file)
                
                if not resume_raw_text.strip():
                    st.error("❌ Could not extract text. The PDF might be empty or a scanned image.")
                    return

                # Calculations
                score, resume_proc, job_proc = calculate_similarity(resume_raw_text, job_description)
                keywords = extract_keywords(job_description)
                missing = get_missing_skills(resume_proc, job_proc)
                strength = analyze_resume_strength(resume_raw_text)

                # --- UI DISPLAY ---
                st.divider()
                
                # Metrics Row
                m1, m2 = st.columns([1, 2])
                with m1:
                    st.subheader('Results')
                    st.metric(label="Match Score", value=str(score) + "%")
                    
                    # Pie Chart
                    fig, ax = plt.subplots(figsize=(3,3))
                    ax.pie([score, 100-score], labels=['Match', 'Gap'], 
                           autopct='%1.1f%%', colors=['#4CAF50', '#ff9999'], startangle=90)
                    ax.axis('equal') 
                    st.pyplot(fig)

                with m2:
                    st.subheader("📊 Analysis Insights")
                    
                    tab1, tab2, tab3 = st.tabs(["Keywords", "Missing Skills", "Resume Sections"])
                    
                    with tab1:
                        st.write("Top 10 Keywords found in Job Description:")
                        cols = st.columns(2)
                        for i, (word, count) in enumerate(keywords):
                            cols[i % 2].write(f"🔹 **{word}** ({count})")

                    with tab2:
                        if missing:
                            st.write("💡 Consider adding these terms to your resume:")
                            st.info(", ".join(missing))
                        else:
                            st.success("Great! Your resume covers most keywords.")

                    with tab3:
                        st.write("Sections detected in your resume:")
                        st.write(" ✅ " + "  ✅ ".join(strength) if strength else "No standard sections found.")

        else:
            st.warning("⚠️ Please provide both the Resume and the Job Description.")

if __name__ == "__main__":
    main()