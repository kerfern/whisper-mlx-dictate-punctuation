import gradio as gr
import requests

def transcribe(audio):
    if audio is None:
        return "No audio file provided"
    
    audio_path = audio
    try:
        with open(audio_path, 'rb') as f:
            files = {'speech_file': f}
            response = requests.post(
                'http://192.168.1.101:5000/transcribe',
                files=files
            )

            # Print response for debugging purposes
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            # Attempt to parse JSON response
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json().get('text', 'Transcription failed')
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return "Transcription request failed"
    except ValueError:
        print("Invalid JSON received")
        return "Invalid response from transcription server"

with gr.Blocks() as demo:
    msg = gr.Textbox()
    audio_box = gr.Audio(label="Audio", type="filepath", elem_id='audio')
    with gr.Row():
        send_btn = gr.Button('Send')
        clear = gr.Button("Clear")
        send_btn.click(fn=transcribe, inputs=audio_box, outputs=msg)
        clear.click(lambda: "", None, msg, queue=False)
    demo.queue().launch(
        debug=True,
        server_name="192.168.1.101",
        server_port=7860,
        # ssl cert made for lcoal deployment using mkcert.
        ssl_certfile="192.168.1.101.pem",
        ssl_keyfile="192.168.1.101-key.pem",
        ssl_verify=False  # Optional: Disable SSL verification for self-signed certificates
    )
