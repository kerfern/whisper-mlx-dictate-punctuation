Why:
Whisper for Radiologist use.
whisper autopunctuates and dictating puncutation results in words not actual punctuations.

What:
2 python files. 1 for the whisper-mlx back end, other for gradio front end for local deployment.

Using a series of text transformation, one can strip the puncutation, add punctuation and then capitalise after punctuation.

other features:
use of intial_prompt to include vocaublary to improve generated output
use of gradio front end

disclaimer:
Most of this was trial and error using GPT4, GPT4o
