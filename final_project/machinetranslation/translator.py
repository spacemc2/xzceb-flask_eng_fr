from . import config
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



apikey = config.APIKEY
url = config.URL


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# languages = language_translator.list_identifiable_languages()
# print(languages)


def english_to_french(english_text):
    """translate english to french"""
    if english_text != '':
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    return ''
def french_to_english(french_text):
    """translate french to english"""
    if french_text!='':
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    return ''
