"""Module providing english to french and vice versa translations."""
import os
# import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))


def english_to_french(english_text):
    """
    English to French model
    """
    #write the code here
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    # print(json.dumps(french_text, indent=2, ensure_ascii=False))

    return french_text.get("translation")[0].get("translation")


def french_to_english(french_text):
    """
    French to English model
    """
    #write the code here
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    # print(json.dumps(english_text, indent=2, ensure_ascii=False))

    return english_text.get("translation")[0].get("translation")
