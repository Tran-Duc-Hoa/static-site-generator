from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches
    
# Create a similar function extract_markdown_links(text) that extracts markdown links instead of images. It should return tuples of anchor text and URLs. For example:
def extract_markdown_links(text):
    pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches
    
result = extract_markdown_images("![alt text](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)")
print(result)
links = extract_markdown_links("[Google](https://www.google.com)")
print(links)