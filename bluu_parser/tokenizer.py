FLOW = '->'

# Token definitions
TOKENS = {
    # Headings
    'h1': rf"^h1{FLOW}\s*(.+)$",
    'h2': rf"^h2{FLOW}\s*(.+)$",
    'h3': rf"^h3{FLOW}\s*(.+)$",
    'h4': rf"^h4{FLOW}\s*(.+)$",
    'h5': rf"^h5{FLOW}\s*(.+)$",
    'h6': rf"^h6{FLOW}\s*(.+)$",

    # Bold, italic, underline
    'bold': rf"(b|bold){FLOW}\s*([^<]+)\s*<",
    'italic': rf"(i|italic){FLOW}\s*([^<]+)\s*<",
    'underline': rf"(u|underline){FLOW}\s*([^<]+)\s*<",
    'strike': rf"(s|strike){FLOW}\s*([^<]+)\s*<",

    # Links
    'link': rf"link{FLOW}\s*(.+)\s*\|\s*(.+)",

    # Lists
    'list': rf"(list|l){FLOW}\s*\n((?:\s*[-\d+\.]\s*.+\n)+?)\s*<",

    # Code
    'code': rf"code{FLOW}([a-zA-Z]*)\s*\n(.*?)\s*<",
    
    # Inline code
    'inline_code': rf"code{FLOW}\s*([^<]+)\s*<",

    # Images
    'img': rf"img{FLOW}\s*(.+)\s*\|\s*(.+)",

    # Quotes
    'quote': rf"quote{FLOW}\s*\n(.*?)\s*<",

    # Tables
    'table': rf"table{FLOW}\s*\n((?:\s*[^\n]+\n)+?)\s*<",

    # Horizontal line with style
    'hr_style': rf"hr{FLOW}(standard|dotted|thick)",

    # Text
    'text': r"(.+)",

    # Color text
    'color': rf"color{FLOW}\s*(.+)\s*\|\s*([a-zA-Z0-9#]+)",
    
    # New Line
    'newline': rf"{FLOW}(\d+)?",

    # Emojis
    'emoji': rf"emoji{FLOW}\s*([a-zA-Z0-9_]+)",
    
    # Collapse section
    'collapse': rf"collapse{FLOW}\s*(.+?)\s*\|\s*([^<]+)\s*<",

    # Bluuu block
    'bluu': r"bluu\{(.+?)\}",
}