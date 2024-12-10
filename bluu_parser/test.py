from bluu_parser.parser import parse_bluu_to_html  # Ensure your parser is accessible


text = """
h1-> Welcome to Bluu Syntax Parser
h2-> A Demonstration of All Features
color-> Text with colors! | red
bg-> Highlighted text | #f0f0f0
font-> Arial | size:16
hr->standard

list->
- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2
- Item 3
<

code->python
def greet(name):
    return f"Hello, {name}!"
<
code->highlight | javascript
function greet(name) {
    return `Hello, ${name}!`;
}
<

collapse-> Click me to see more | Here is some hidden content!
video-> https://www.youtube.com/embed/dQw4w9WgXcQ | 560x315

icon-> fa fa-check
tooltip-> Hover me | This is a tooltip.

button-> Click me | alert('Hello from Bluu!')

audio-> https://www.example.com/audio.mp3 | This is an audio file

class-> my-custom-class | This is custom-styled text.

emoji-> :smile:

accordion->
Accordion 1 | This is the first accordion content.
Accordion 2 | This is the second accordion content.
<

img-> https://via.placeholder.com/150 | Placeholder Image

quote->
This is a blockquote that spans
multiple lines to demonstrate
the feature.
<

table->
Name | Age | Occupation
John | 25 | Developer
Jane | 30 | Designer
<



"""
print(parse_bluu_to_html(text))  # Example usage)