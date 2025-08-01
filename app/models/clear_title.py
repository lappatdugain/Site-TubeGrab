import re
import unicodedata

def clear_up_title(title) -> str:
    """
    Cleans up a given title by replacing special characters with underscores and removing non-Latin scripts.

    :param title: The title to be cleaned.
    :type title: str
    :return: The cleaned title.
    :rtype: str

    The function performs the following operations:
    - Removes characters from various non-Latin scripts, including:
        - Chinese, Japanese, Korean
        - Arabic
        - Cyrillic
        - Greek
        - Hebrew
        - Thai
        - Devanagari (Hindi, Sanskrit)
        - Bengali
        - Gurmukhi
        - Gujarati
        - Oriya
        - Tamil
        - Telugu
        - Kannada
        - Malayalam
        - Sinhala
        - Khmer
        - Burmese
        - Georgian
        - Armenian
        - Ethiopian
    - Replaces special characters with space.
    """

    normalized = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('ascii')


    new_title_v1 = re.sub(r'[\u4E00-\u9FFF\u3040-\u30FF\uAC00-\uD7AF'
                        r'\u0600-\u06FF'
                        r'\u0400-\u04FF'
                        r'\u0370-\u03FF'
                        r'\u0590-\u05FF'
                        r'\u0E00-\u0E7F'
                        r'\u0900-\u097F'
                        r'\u0980-\u09FF'
                        r'\u0A00-\u0A7F'
                        r'\u0A80-\u0AFF'
                        r'\u0B00-\u0B7F'
                        r'\u0B80-\u0BFF'
                        r'\u0C00-\u0C7F'
                        r'\u0C80-\u0CFF'
                        r'\u0D00-\u0D7F'
                        r'\u0D80-\u0DFF'
                        r'\u1780-\u17FF'
                        r'\u1000-\u109F'
                        r'\u10A0-\u10FF'
                        r'\u0530-\u058F'
                        r'\u1200-\u137F'
                        r']+', '', normalized)
    new_title_v2=re.sub(r'[^a-zA-Z0-9À-ÖØ-öø-ÿ\s]', ' ', new_title_v1)
    return re.sub(r'\s+', ' ', new_title_v2).strip()




if __name__=="__main__":
    print(clear_up_title("澤野弘之×『FaÉte/strange Fake -Whispers of Dawnô-』スペシャルライブ「STRANGEFAKE」"))