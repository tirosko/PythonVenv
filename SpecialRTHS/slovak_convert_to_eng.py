import unicodedata


def remove_diacritics(text):
    # Normalize the text to decompose accents
    normalized = unicodedata.normalize('NFD', text)
    # Filter out combining characters (accents)
    ascii_text = ''.join(
        char for char in normalized if not unicodedata.combining(char))
    return ascii_text


# Example usage
slovak_text = "Údržbársko-hasiaci balíček konsolidácie"
clean_text = remove_diacritics(slovak_text)

print("Original:", slovak_text)
print("Converted:", clean_text)
