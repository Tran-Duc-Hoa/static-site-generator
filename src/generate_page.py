import os

from markdown_blocks import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, 'r') as file:
        markdown_content = file.read()

    # Read the template file
    with open(template_path, 'r') as file:
        template_content = file.read()

    # Convert markdown to HTML
    html_content = markdown_to_html_node(markdown_content).to_html()

    # Extract the title
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    full_html = template_content.replace(
        '{{ Title }}', title).replace('{{ Content }}', html_content)

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the full HTML to the destination file
    with open(dest_path, 'w') as file:
        file.write(full_html)
