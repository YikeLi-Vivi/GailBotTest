# -*- coding: utf-8 -*-
# @Author: Vivian Li
# @Date:   2024-04-05 07:48:22
# @Last Modified by:   Vivian Li
# @Last Modified time: 2024-04-05 12:40:23
from gailbot import GailBot
from gailbot import ProfileSetting
from tqdm import tqdm

INPUT = "./input/test2ab/"
OUTPUT = "./output/"


# basic usage using default whisperX engine and HiLabSuite setting
def transcribe_with_default():
    gb = GailBot()
    gb.add_source(source_path=INPUT, output_dir="../output/")
    result = gb.transcribe()
    print(f"WhisperX default profile transcription result: {result}")


# transcription with google engine
def transcribe_with_google():
    gb = GailBot()
    google_engine_setting = {
        "engine": "google",
        "google_api_key": "../input/google-api.json",
    }
    google_engine_name = "google engine"

    google_profile_setting = ProfileSetting(
        engine_setting_name=google_engine_name,
        plugin_suite_setting={
            "HiLabSuite": ["XmlPlugin", "ChatPlugin", "TextPlugin", "CSVPlugin"]
        },
    )
    google_profile_name = "google profile"

    if not gb.is_engine(google_engine_name):
        gb.add_engine(name=google_engine_name, setting=google_engine_setting)

    if not gb.is_profile(google_profile_name):
        gb.create_profile(name=google_profile_name, data=google_profile_setting)

    source_id = gb.add_source(INPUT, OUTPUT)
    gb.apply_profile_to_source(source_name=source_id, profile_name=google_profile_name)
    google_transcription_result = gb.transcribe()
    print(f"Google transcription result: {google_transcription_result}")


# transcribe with whisper
def transcribe_with_whisper():
    gb = GailBot()
    whisper_engine_setting = {
        "engine": "whisper",
        "language": "English",
        "speaker_detect": False,
    }
    whisper_engine_name = "whisper engine"

    whisper_profile_setting = ProfileSetting(
        engine_setting_name=whisper_engine_name,
        plugin_suite_setting={
            "HiLabSuite": ["XmlPlugin", "ChatPlugin", "TextPlugin", "CSVPlugin"]
        },
    )
    whisper_profile_name = "whisper profile"

    if not gb.is_engine(whisper_engine_name):
        gb.add_engine(name=whisper_engine_name, setting=whisper_engine_setting)

    if not gb.is_profile(whisper_profile_name):
        gb.create_profile(name=whisper_profile_name, data=whisper_profile_setting)

    source_id = gb.add_source(INPUT, OUTPUT)
    gb.apply_profile_to_source(source_name=source_id, profile_name=whisper_profile_name)
    whisper_transcription_result = gb.transcribe()
    print(f"Whisper transcription result: {whisper_transcription_result}")


def transcribe_with_watson():
    gb = GailBot()
    WATSON_API_KEY = "MSgOPTS9CvbADe49nEg4wm8_gxeRuf4FGUmlHS9QqAw3"
    WATSON_LANG_CUSTOM_ID = "41e54a38-2175-45f4-ac6a-1c11e42a2d54"
    WATSON_REGION = "dallas"
    WATSON_BASE_LANG_MODEL = "en-US_NarrowbandModel"
    watson_engine_name = "Watson Engine"
    watson_engine_setting = {
        "engine": "watson",
        "apikey": WATSON_API_KEY,
        "region": WATSON_REGION,
        "base_model": WATSON_BASE_LANG_MODEL,
    }

    watson_profile_name = "Watson Profile"
    watson_profile = ProfileSetting(
        engine_setting_name=watson_engine_name,
        plugin_suite_setting={
            "HiLabSuite": ["XmlPlugin", "ChatPlugin", "TextPlugin", "CSVPlugin"]
        },
    )

    if not gb.is_engine(watson_engine_name):
        gb.add_engine(name=watson_engine_name, setting=watson_engine_setting)
    if not gb.is_profile(watson_profile_name):
        gb.create_profile(name=watson_profile_name, data=watson_profile)
    source_id = gb.add_source(INPUT, OUTPUT)
    gb.apply_profile_to_source(source_name=source_id, profile_name=watson_profile_name)
    watson_transcription_result = gb.transcribe()
    print(f"Watson transcription result: {watson_transcription_result}")


if __name__ == "__main__":
    transcribe_with_default()
    transcribe_with_google()
    transcribe_with_whisper()
    transcribe_with_watson()
