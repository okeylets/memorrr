
from flask import Flask, request, send_file, render_template, jsonify
from flask_cors import CORS
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for API requests

def generate_song(text, genre):
    """Generate song lyrics based on input text and genre."""
    return f"{text} in {genre} style. This is a simulated song."

@app.route('/')
def home():
    """Serve the main HTML page for the application."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Generate the song audio file based on user input."""
    data = request.json
    text = data.get('text', '').strip()  # Extract text and genre safely
    genre = data.get('genre', '').strip()

    if not text or not genre:
        return jsonify({"error": "Text and genre are required!"}), 400

    song_lyrics = generate_song(text, genre)  # Generate song lyrics

    # Generate the song audio
    audio_stream = BytesIO()  # Create an in-memory byte stream for the audio
    tts = gTTS(text=song_lyrics, lang='en')  # Convert text to speech
    tts.save(audio_stream)  # Save audio to the byte stream
    audio_stream.seek(0)  # Reset stream position to the beginning

    # Serve the audio file as a response
    return send_file(audio_stream, as_attachment=True, download_name='generated_song.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
