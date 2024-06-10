# Whisper for Radiologist Use

## Why
Whisper autopunctuates, and dictating punctuation results in words, not actual punctuations.

## What
This repository contains two Python files:
1. **whisper-mlx**: The back end for Whisper.
2. **gradio**: The front end for local deployment using Gradio.

Using a series of text transformations, one can strip the punctuation, add punctuation, and then capitalize after punctuation.

## Other Features
- Use of mlx-whisper for apple silicon use.
- Use of `initial_prompt` to include vocabulary to improve generated output.
- Use of Gradio front end for webui.

## Disclaimer
Most of this was trial and error using GPT-4 and GPT-4o.
