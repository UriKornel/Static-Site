from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown_text = f.read()
    with open(template_path) as f:
        template = f.read()

    html_text = markdown_to_html_node(markdown_text)
    html_text = html_text.to_html()
    title = extract_title(markdown_text)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_text)

    # /home/uri/Workspace/Static-Site/public/contact
    # /home/uri/Workspace/Static-Site/public/blog/tom
    os.makedirs(dest_path, exist_ok=True)

    with open(os.path.join(dest_path, "index.html"), 'w') as f:
        f.write(template)
