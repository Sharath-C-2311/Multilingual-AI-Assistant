🧠 Multilingual AI Voice + Text Assistant
A web-based AI assistant that supports multilingual interaction via both text and voice. Users can choose from five languages—English, Hindi, Kannada, Telugu, and Tamil—and communicate with the assistant using typed input or speech. The assistant responds in the selected language and speaks the reply aloud using browser-based speech synthesis.


🌐 Features
Language Selection Interface: Choose your preferred language from a dropdown menu.
Multilingual Support: Communicate in English, Hindi, Kannada, Telugu, or Tamil.
Voice Recognition: Speak to the assistant using your microphone.
Text-to-Speech: AI responses are spoken aloud in the selected language.
AI-Powered Responses: Uses Gemini 2.0 Flash model via Google Generative AI API.


🛠️ Tech Stack
Component     | Technology
Frontend      |HTML,CSS, JavaScript
Backend       |	Flask (Python)
AI Model      |	Gemini 2.0 Flash (Google GenAI)
Voice Features|	Web Speech API (SpeechRecognition + SpeechSynthesis)



🚀 Getting Started
Prerequisites:
Python 3.7+
Flask
Google Generative AI Python SDK (google-genai)
A valid Google GenAI API key


Installation

1.Clone the repository:
git clone https://github.com/yourusername/multilingual-ai-assistant.git
cd multilingual-ai-assistant

2.Install dependencies:
pip install flask google-genai

3.Set your API key in the Flask app:
client = genai.Client(api_key="YOUR_API_KEY")

4.Run the server:
python app.py

5.Open your browser and go to:
http://localhost:5000

📁 Project Structure
multilingual-ai-assistant/
│
├── static/
│   └── style.css          # Custom styles
│
├── templates/
│   ├── home.html          # Language selection page
│   └── va.html            # Chat interface
│
├── app.py                 # Flask backend
└── README.md              # Project documentation


💬 Supported Languages
🇬🇧 English
🇮🇳 Hindi
🇮🇳 Kannada
🇮🇳 Telugu
🇮🇳 Tamil


🎤 Voice Interaction
Click the 🎤 button to start speaking.
The assistant transcribes your voice and responds in the selected language.
Responses are spoken aloud using the appropriate voice settings.


📌 Notes
Speech recognition may vary across browsers. Best supported in Chrome.
Ensure microphone permissions are enabled.
API key should be kept secure and not exposed in public repositories.
