# 📄 AI Resume Analyzer

An intelligent resume analysis tool powered by AI that provides comprehensive feedback on your resume, covering formatting, content quality and career impact.

**🚀 [Live Demo](https://ai-resume-analyzer-tyhan.streamlit.app/)**

## ✨ Features

- **AI-Powered Analysis**: Uses advanced language models to analyze resumes comprehensively
- **Content Evaluation**: Assess the quality and impact of your resume content
- **Formatting Review**: Get feedback on layout, design, and readability
- **Skill Analysis**: Identify and evaluate technical and soft skills
- **Easy-to-Use Interface**: Clean, intuitive web interface powered by Streamlit

## 🎯 What You'll Get

- **Overall Score**: A comprehensive rating of your resume (0-100)
- **Detailed Feedback**: Section-by-section analysis and improvement suggestions
- **Strengths**: Highlight what's working well in your resume
- **Areas for Improvement**: Specific recommendations for enhancement
- **Career Impact Score**: Assessment of how well your resume showcases your value

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/tyhan-data/AI-Resume-Analyzer.git
   cd AI-Resume-Analyzer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with your API keys:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Access the app**
   Open your browser and navigate to `http://localhost:8501`

## 📖 Usage

1. **Upload or Paste Your Resume**: Choose to upload a PDF/DOCX file or paste your resume text
2. **Select Analysis Type**: Choose between quick analysis or comprehensive review
3. **Get Instant Feedback**: Receive detailed insights and recommendations
4. **Download Report**: Export your analysis results as a PDF (optional)

## 📁 Project Structure

```
AI-Resume-Analyzer/
│
├── resume_analyzer.py
├── requirements.txt
├── README.md
```

## 🤖 Technology Stack

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework
- **PyPDF2**: PDF file parsing
- **pandas**: Data processing and analysis


## 📊 How It Works

1. **Resume Parsing**: Extracts text from uploaded PDF, DOCX, or plain text
2. **Content Analysis**: Uses AI to evaluate resume content, structure, and impact
4. **Scoring Algorithm**: Generates a comprehensive score based on multiple factors
5. **Report Generation**: Presents actionable feedback and recommendations

## 💡 Tips for Best Results

- Ensure your resume is well-formatted and readable
- Include relevant keywords from the job description
- Use clear section headers (Experience, Skills, Education, etc.)
- Keep your resume concise (1-2 pages)
- Highlight quantifiable achievements with metrics
- Tailor your resume to the specific job you're applying for

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🙋 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/tyhan-data/AI-Resume-Analyzer/issues) page
2. Create a new issue with detailed information
3. Include steps to reproduce the problem

## 🌟 Show Your Support

If you find this tool helpful, please consider:

- ⭐ Starring the repository
- 🐛 Reporting bugs and suggesting features
- 💬 Sharing feedback and improvements
- 📢 Spreading the word to others

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Resume Best Practices](https://www.indeed.com/career-advice/resumes)

## 👨‍💻 Author

**Tyhan-Data** - [GitHub Profile](https://github.com/tyhan-data)

---

**Try it now**: 🚀 [AI Resume Analyzer](https://ai-resume-analyzer-tyhan.streamlit.app/)

Made with ❤️ to help you land your dream job.
