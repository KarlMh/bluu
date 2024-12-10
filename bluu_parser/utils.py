import re

def mask_quoted_content(text):
    placeholders = []
    def replacer(match):
        placeholders.append(match.group(0))  # Save quoted content
        return f"__PLACEHOLDER_{len(placeholders) - 1}__"  # Replace with placeholder
    masked_text = re.sub(r"'[^']*'|\"[^\"]*\"", replacer, text)
    return masked_text, placeholders


def restore_quoted_content(text, placeholders):
    """
    Restores masked quoted content in the text.
    """
    for i, placeholder in enumerate(placeholders):
        text = text.replace(f"__PLACEHOLDER_{i}__", placeholder)
    return text
