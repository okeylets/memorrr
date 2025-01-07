python app.py
pip install Flask flask-cors gTTS
from flask import Flask, request, send_file, render_template, jsonify
from flask_cors import CORS
from gtts import gTTS
from io import BytesIO



app = Flask(__name__)
CORS(app)

def generate_song(text, genre):
    # Placeholder for actual song generation based on text and genre
    return f"{text} in {genre} style. This is a simulated song."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text = data['text']
    genre = data['genre']

    if not text or not genre:
        return jsonify({"error": "Text and genre are required!"}), 400

    song_lyrics = generate_song(text, genre)

    # Generate the song audio
    audio_stream = BytesIO()
    tts = gTTS(text=song_lyrics, lang='en')
    tts.save(audio_stream)
    audio_stream.seek(0)  # Go back to the start of the BytesIO stream

    # Serve the audio file
    return send_file(audio_stream, as_attachment=True, download_name='generated_song.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
