"""Convert emoji characters into human-friendly text descriptions.

Requires the `demoji` package for best results:
    pip install demoji

This script uses `demoji` when available and falls back to the
standard-library `unicodedata.name()` when needed. It prints a small
sample list and demonstrates converting a short sentence.
"""

import unicodedata
from typing import Optional

try:
    import demoji
except Exception:
    demoji = None

emoji_list = ["😀", "😂", "😍", "😊", "😒", "😉", "😁", "👍", "🙏","🚒"]


def ensure_demoji_codes() -> Optional[str]:
    """Ensure demoji codes are downloaded.

    Returns None on success, or an error message string on failure / missing
    demoji package.
    """
    if demoji is None:
        return "demoji package not installed"
    try:
        # idempotent; downloads codes if not present
        demoji.download_codes()
        return None
    except Exception as e:
        return str(e)


def convert_emoji_to_text(emoji_char: str) -> str:
    """Return a human-friendly description for a single emoji character.

    Preference order:
    1. demoji.findall() mapping (if demoji available)
    2. unicodedata.name() fallback
    If nothing is available, returns an empty string.
    """
    if not emoji_char:
        return ""

    # Use demoji if available
    if demoji is not None:
        try:
            mapping = demoji.findall(emoji_char)
            if mapping and emoji_char in mapping and mapping[emoji_char]:
                # demoji may return names with underscores; normalize
                return mapping[emoji_char].replace("_", " ")
        except Exception:
            # fall back to unicodedata
            pass

    # Fallback: unicode name (e.g., 'GRINNING FACE')
    try:
        name = unicodedata.name(emoji_char)
        return name.lower().replace("_", " ")
    except Exception:
        return ""


def convert_text_with_emojis(text: str) -> str:
    """Replace emojis in a text with :description: style tokens.

    Example: 'Hi �' -> 'Hi :grinning face:'. Uses demoji when available.
    """
    if demoji is not None:
        try:
            mapping = demoji.findall(text)
            out = text
            for em, name in mapping.items():
                desc = (name or "").replace("_", " ") if name else convert_emoji_to_text(em)
                out = out.replace(em, f":{desc}:")
            return out
        except Exception:
            pass

    # Simple fallback: try to replace characters that have unicode names
    out_chars = []
    for ch in text:
        try:
            name = unicodedata.name(ch)
            # Heuristic: treat characters with common emoji-related words as emojis
            if any(k in name for k in ("FACE", "HAND", "HEART", "EYE", "THUMBS", "FOLD")):
                out_chars.append(f":{name.lower().replace('_', ' ')}:")
            else:
                out_chars.append(ch)
        except Exception:
            out_chars.append(ch)
    return "".join(out_chars)


def main():
    # Warn about demoji if missing or its codes couldn't be downloaded
    err = ensure_demoji_codes()
    if err is not None:
        print("Note:", err)
        print("For best results install demoji: pip install demoji")

    for e in emoji_list:
        text = convert_emoji_to_text(e)
        print(f"Emoji: {e}  |  Text: {text}")

    # Demonstrate converting a short sentence
    sample = "Hello 😀! I love Python 👍🙏"
    print("\nSample text:")
    print(sample)
    print("Converted:")
    print(convert_text_with_emojis(sample))


if __name__ == "__main__":
    main()
