# ATS Pulse AI 📊
https://aistudio.google.com/: go here to get your api key 
Also run it in code spaces and run the commands I have put here for you

A professional backend AI researcher agent built entirely in Python. The tool simulates an enterprise Automated Tracking System (ATS) to cross-examine technical resumes against target job descriptions using the Google Gemini LLM engine.

## 🛠️ Key Features
- **Semantic Mapping**: Deep context matching beyond raw text strings.
- **Secure Architecture**: Environment variable decoupling to shield confidential API credentials.
- **Actionable Optimization**: Automated matrix sorting to extract missing engineering keywords.

## ⚡ Quick Start

1. **Install dependencies:**
   ```bash
   pip install google-genai
   ```

2. **Run the parser agent pipeline (Single-Line Command):**
   ```bash
   GEMINI_API="your_new_key_here" python matcher.py
   ```
   *(This passes your credential securely to the runtime without saving it to your local terminal shell history).*

