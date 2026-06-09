import os
from google import genai

GEMINI_API_KEY = os.environ.get("GEMINI_API")

MOCK_RESUME = """
Scott Nice - Software Engineering Intern
Skills: Python, JavaScript, Git, Code Sandbox, Terminal Scripting.
Experience: Built automation scripts inside secure cloud containers. 
Optimized data manipulation configurations using automated logic parameters.
"""

MOCK_JOB_DESCRIPTION = """
We are looking for a Junior AI Integration Engineer. 
Required Stack: Python, Google Gemini SDK or OpenAI API, LLM Prompt Engineering.
Responsibilities: Build backend data pipelines and connect automation workflows to remote LLM models.
"""

print("[*] Starting ATS Optimization Agent Pipeline...")

if not GEMINI_API_KEY:
    print("\n[!] DATA LOADED, BUT SKIPPING AI ANALYSIS STEP")
    print("To finish: Run 'export GEMINI_API=your_key' in the terminal, then run this file.")
else:
    print("[+] Transmission payload packetized. Analyzing match via Gemini LLM...")
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        prompt = (
            "You are an expert technical recruiter and ATS parsing scanner. "
            "Compare this candidate resume with the target job description. "
            "Output an exact compatibility percentage rating, a short bulleted list "
            "of missing critical keywords, and 2 actionable sentences to optimize the resume:\n\n"
            "RESUME:\n" + MOCK_RESUME + "\n\n"
            "JOB DESCRIPTION:\n" + MOCK_JOB_DESCRIPTION
        )
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        print("\n=== ATS RECRUITING AGENT REPORT ===")
        print(response.text)
        
    except Exception as e:
        print("[!] Execution error inside LLM handler: " + str(e))
