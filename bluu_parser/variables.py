import ast

# Global variables dictionary to hold all variables
variables = {}

def extract_variables_from_bluu_block(match):
    content = match.group(1).strip()
    assignments = content.splitlines()

    for assignment in assignments:
        if '->' in assignment:
            var_name, var_value = assignment.split(FLOW)
            var_name = var_name.strip()
            var_value = var_value.strip()

            # Check if the value is a string (enclosed in quotes)
            if (var_value.startswith("'") and var_value.endswith("'")) or (var_value.startswith('"') and var_value.endswith('"')):
                var_value = var_value[1:-1]  # Remove quotes from string value
                variables[var_name] = var_value  # Store the string without quotes
            else:
                # Check if the value is an expression and evaluate it
                try:
                    variables[var_name] = ast.literal_eval(var_value)
                except Exception:
                    variables[var_name] = var_value  # Fallback to raw text
    return ''  # Return an empty string to remove the bluu{} block