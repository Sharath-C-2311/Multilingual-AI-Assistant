from flask import Flask, render_template, request, jsonify
import google.genai as genai

app = Flask(__name__)
client = genai.Client(api_key="YOUR_API_KEY")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/assistant')
def assistant():
    lang = request.args.get('lang', 'English')
    return render_template('va.html', lang=lang)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data['message']
    lang = data['lang']
    if lang!="English":
        prompt = f"Respond strictly in {lang} without using any English words or phrases. User said: {user_input}"
    else:
        prompt = f"Respond in {lang}. User said: {user_input}"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return jsonify({'reply': response.text})

if __name__ == '__main__':
    app.run(debug=True)