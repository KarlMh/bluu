import gradio as gr
import parser as p

# Gradio interface
def render_bluu(bluu_text):
    return f"<div>{p.parse_bluu_to_html(bluu_text)}</div>"

# Create Gradio app with live updates
interface = gr.Interface(
    fn=render_bluu,  # Function to render Bluu as HTML
    inputs=gr.TextArea(elem_id="shared_box"),  # Use same element ID
    outputs=gr.HTML(elem_id="shared_box"),  # Use same element ID to overlay
    live=True,  # Enable real-time updates
    title="Bluu to HTML Live Renderer", 
    description="Type Bluu syntax directly, and see the rendered HTML output live!"
)



# Run the app
if __name__ == "__main__":
    interface.launch()
