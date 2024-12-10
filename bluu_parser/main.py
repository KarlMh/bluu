import sys
from parser import parse_bluu_to_html

def main():
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename.bluu>")
        sys.exit(1)

    # Get the file name from the command-line arguments
    input_filename = sys.argv[1]

    # Ensure the file ends with .bluu
    if not input_filename.endswith('.bluu'):
        print("Error: The file must have a .bluu extension.")
        sys.exit(1)

    try:
        # Read the content of the .bluu file
        with open(input_filename, 'r', encoding='utf-8') as file:
            bluu_content = file.read()

        # Parse the content using parse_bluu_to_html
        html_output = parse_bluu_to_html(bluu_content)

        # Create an output HTML file
        output_filename = input_filename.replace('.bluu', '.html')
        with open(output_filename, 'w', encoding='utf-8') as html_file:
            html_file.write(html_output)

        print(f"HTML content has been written to {output_filename}.")
        print("Open the file in a web browser to view the rendered content.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
