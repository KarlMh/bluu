import re
import variables
from tokenizer import TOKENS


def transform_headings(text):
    """
    Transforms headings (h1-h6) to HTML.
    """
    for level in range(1, 7):
        text = re.sub(TOKENS[f'h{level}'], rf'<h{level}>\1</h{level}>', text, flags=re.M)
    return text


def transform_text_formatting(text):
    """
    Transforms bold, italic, underline, and strikethrough formatting to HTML.
    """
    text = re.sub(TOKENS['bold'], r'<strong>\2</strong>', text)
    text = re.sub(TOKENS['italic'], r'<em>\2</em>', text)
    text = re.sub(TOKENS['underline'], r'<u>\2</u>', text)
    text = re.sub(TOKENS['strike'], r'<s>\2</s>', text)
    return text


def transform_links(text):
    """
    Transforms links into HTML anchor tags.
    """
    return re.sub(TOKENS['link'], r'<a href="\2">\1</a>', text)


def transform_lists(text):
    """
    Transforms lists (ordered and unordered) into HTML list tags.
    """
    return re.sub(
        TOKENS['list'],
        lambda m: (
            '<ul>' + ''.join(
                f"<li>{line.strip('- ').strip()}</li>" 
                for line in m.group(2).splitlines() if line.strip().startswith('-')
            ) + '</ul>' 
            if '-' in m.group(2) else
            '<ol>' + ''.join(
                f"<li>{line.split('.', 1)[1].strip()}</li>" 
                for line in m.group(2).splitlines() if line.strip() and '.' in line
            ) + '</ol>'
        ),
        text
    )


def transform_dividers(text):
    """
    Transforms horizontal dividers based on the style.
    """
    if 'standard' in TOKENS['hr_style']:
        return re.sub(TOKENS['hr_style'], r'<hr style="margin: 10px 0;">', text, flags=re.M)
    elif 'dotted' in TOKENS['hr_style']:
        return re.sub(TOKENS['hr_style'], r'<hr style="border-top: 1px dotted; margin: 10px 0;">', text, flags=re.M)
    elif 'thick' in TOKENS['hr_style']:
        return re.sub(TOKENS['hr_style'], r'<hr style="border-top: 3px solid; margin: 10px 0;">', text, flags=re.M)
    return text


def transform_code(text):
    """
    Transforms code blocks into HTML preformatted code blocks.
    """
    return re.sub(
        TOKENS['code'],
        lambda m: f"<pre><code class='{m.group(1)}'>{m.group(2)}</code></pre>",
        text,
        flags=re.S
    )


def transform_images(text):
    """
    Transforms image links into HTML <img> tags.
    """
    return re.sub(TOKENS['img'], r'<img src="\1" alt="\2">', text)


def transform_quotes(text):
    """
    Transforms quotes into HTML blockquote tags.
    """
    return re.sub(
        TOKENS['quote'],
        lambda m: f"<blockquote>{m.group(1).strip().replace('\n', '<br>')}</blockquote>",
        text,
        flags=re.S
    )


def transform_tables(text):
    """
    Transforms tables into HTML <table> tags.
    """
    return re.sub(
        TOKENS['table'],
        lambda m: (
            '<table>' + ''.join(
                f"<thead><tr>{''.join(f'<th>{cell.strip()}</th>' for cell in line.split('|') if cell.strip())}</tr></thead>"
                if idx == 0 else
                f"<tr>{''.join(f'<td>{cell.strip()}</td>' for cell in line.split('|') if cell.strip())}</tr>"
                for idx, line in enumerate(m.group(1).splitlines()) if line.strip()
            ) + '</table>'
        ),
        text,
        flags=re.S
    )


def transform_color(text):
    """
    Transforms color text into HTML span with style.
    """
    return re.sub(TOKENS['color'], r'<span style="color: \2;">\1</span>', text, flags=re.M)


def transform_newlines(text):
    """
    Transforms newlines into <br> tags, handling optional multipliers.
    """
    return re.sub(
        TOKENS['newline'],
        lambda match: (
            match.group(0)  # Leave as-is if any TOKENS precedes
            if any(
                text[:match.start()].endswith(f"{TOKENS}")
                for TOKENS in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'list', 'code', 'img', 'quote', 'bold', 'b', 'italic', 'i', 'underline', 'u', 'strike', 's', 'link', 'color', 'collapse', 'variable']
            )
            else '<br>' * int(match.group(1) or 1)  # Replace with <br> otherwise
        ),
        text,
        flags=re.M
    )




def transform_emojis(text):
    """
    Transforms emoji placeholders into actual emoji characters.
    """
    EMOJI_MAP = {
        'smile': '😊',
        'heart': '❤️',
        'thumbs_up': '👍',
        # Add more emoji mappings as needed
    }
    return re.sub(
        TOKENS['emoji'],
        lambda match: EMOJI_MAP.get(match.group(1), f"[{match.group(1)}]"),  # Fallback to placeholder
        text
    )


def transform_collapse(text):
    """
    Transforms collapse sections into HTML details and summary tags.
    This avoids transforming content that's already inside a <details> or <summary>.
    """
    # Using negative lookahead to avoid matching inside existing <details> or <summary> tags
    return re.sub(
        TOKENS['collapse'],
        lambda m: f'<details><summary>{m.group(1)}</summary>{m.group(2).strip()}</details>',
        text,
        flags=re.S
    )
    
def transform_variables(text):
    return re.sub(TOKENS['bluu'], lambda match: variables.extract_variables_from_bluu_block(match), text, flags=re.S)
