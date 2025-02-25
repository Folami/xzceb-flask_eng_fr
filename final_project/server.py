from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/")
def render_index_page():
    # Write the code to render template
    return render_template("index.html")

@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    translator.english_to_french(text_to_translate)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    translator.french_to_english(text_to_translate)
    return "Translated text to English"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
