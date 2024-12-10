import transformers as t
import variables as v
import utils as u
import re


def parse_bluu_to_html(bluu_text):
    # Step 1: Mask quoted content (preserving quoted sections)
    masked_text, placeholders = u.mask_quoted_content(bluu_text)
    
    # Step 2: Extract variables from bluu{} block (no need to pass variables anymore)
    masked_text = t.transform_variables(masked_text)
    
    # Step 3: Substitute variables in the content
    def replace_variables(match):
        variable_name = match.group(1).strip('{}')
        variable_value = v.variables.get(variable_name, match.group(0))  # Get the variable value or fallback to original text
        return str(variable_value)  # Replace with variable value (without quotes)

    masked_text = re.sub(r"\{([^}]+)\}", replace_variables, masked_text)
    # Step 4: Transform the content into HTML
    masked_text = t.transform_headings(masked_text)
    masked_text = t.transform_text_formatting(masked_text)
    masked_text = t.transform_links(masked_text)
    masked_text = t.transform_lists(masked_text)
    masked_text = t.transform_dividers(masked_text)
    masked_text = t.transform_code(masked_text)
    masked_text = t.transform_images(masked_text)
    masked_text = t.transform_quotes(masked_text)
    masked_text = t.transform_tables(masked_text)
    masked_text = t.transform_color(masked_text)
    masked_text = t.transform_newlines(masked_text)
    masked_text = t.transform_emojis(masked_text)
    masked_text = t.transform_collapse(masked_text)
    
    # Step 5: Restore quoted content
    return u.restore_quoted_content(masked_text, placeholders)