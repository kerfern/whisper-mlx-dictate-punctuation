from flask import Flask, request, jsonify
import mlx_whisper
import re

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_speech():
    # Check if the request contains a file
    if 'speech_file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['speech_file']

    # If the user does not select a file, the browser submits an empty file without a filename.
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Assuming you have a specific location to save the uploaded file
    file.save("/Users/kerf/Kerf's MLX/input/" + file.filename)
    
    text = mlx_whisper.transcribe(
        "/Users/kerf/Kerf's MLX/input/" + file.filename, 
        path_or_hf_repo="mlx-community/whisper-large-v3-mlx-4bit",
        # add more words ato initia_prompt to improve words generated
        initial_prompt="sulci, sylvian fissure, haemorrhage, mastoid, anterolisthesis, 4mm",
        language="en",
        temperature=0.1,
        compression_ratio_threshold=2.4,
        logprob_threshold=-1.0,
        no_speech_threshold=0.6,
        condition_on_previous_text=True,
        hallucination_silence_threshold=0.8,
        
    )["text"].lstrip()

#     # Strip punctuation from the transcribed text
    text = strip_punctuation(text)

#     # Call replace_punctuation to modify the transcribed text
    text = replace_punctuation(text)
    
#     # Capitalize letters after punctuation
    text = capitalize_after_punctuation(text)
    
    return jsonify({'text': text})

def strip_punctuation(transcription):
    # Remove commas and periods from the transcription
    transcription = re.sub(r'[,.]', '', transcription)
    return transcription

def replace_punctuation(transcription):
    replacements = {
        "new line": "\n",
        "newline": "\n",
        "neoline": "\n",
        "Neoline": "\n",
        "comma": ",",
        "period": ".",
        "full stop": ".",
        "Full stop": ".",
        "colon": ":",
        "exclamation mark": "!",
        "question mark": "?"
    }
    for word, symbol in replacements.items():
        transcription = transcription.replace(f" {word}", symbol).replace(word, symbol)
        transcription = transcription.replace("\n ", "\n")
    return transcription

def capitalize_after_punctuation(text):
    # Capitalize the first letter of the text
    text = text[0].upper() + text[1:]
    
    # Function to capitalize the first letter after punctuation
    def capitalize_match(match):
        return match.group(1) + match.group(2).upper()
    
    # Capitalize after newline, period, and colon, accounting for optional spaces
    text = re.sub(r'(\n\s*)(\w)', capitalize_match, text)
    text = re.sub(r'(\.\s*)(\w)', capitalize_match, text)
    text = re.sub(r'(\:\s*)(\w)', capitalize_match, text)
    
    return text

if __name__ == '__main__':
    # Replace '192.168.x.x' with your actual local IP address
    app.run(host='192.168.1.101', port=5000)