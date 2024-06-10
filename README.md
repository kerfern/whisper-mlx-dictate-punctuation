# Whisper MLX allowing dictation of puncutation and new line, for Radiologist Use

## Problem this overcomes
Whisper autopunctuates, and dictating punctuation results in words, not actual punctuations.

## What
This repository contains two Python files:
1. **whisper-mlx**: The back end for Whisper.
2. **gradio**: The front end for local deployment using Gradio.

Using a series of text transformations, one can strip the punctuation, add punctuation, and then capitalize after punctuation.

## Other Features
- Use of mlx-whisper for apple silicon use.
- Use of `initial_prompt` to include vocabulary to improve generated output.
- https to allow microphone use via gradio. Use mkcert to make local certificate.

## Disclaimer
Most of this was trial and error using GPT-4 and GPT-4o.
