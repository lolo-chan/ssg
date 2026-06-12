import os
import shutil
from helpers import markdown_to_blocks
from block import block_to_block_type, BlockType
from markdown_to_html import markdown_to_html_node


def static_to_public(source: str, dest: str):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for i in os.listdir(source):
        if os.path.isfile(os.path.join(os.getcwd(), source, i)):
            shutil.copy(f"{source}/{i}", dest)
            print(f"copied {i} to {dest}/")
        elif os.path.isdir(os.path.join(os.getcwd(), source, i)):
            print(f"copied {i}/ to {dest}/")
            static_to_public(f"{source}/{i}", f"{dest}/{i}")


def extract_title(markdown: str) -> str:
    header = markdown_to_blocks(markdown)[0]
    if block_to_block_type(header) == BlockType.HEADING:
        return header[2:].strip()
    raise Exception("no header!")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(f"{from_path}/index.md", encoding="utf-8") as f:
        contents_md_file = f.read()
    
    with open(template_path, encoding="utf-8") as f:
        contents_html_file = f.read()

    html_node = markdown_to_html_node(contents_md_file)
    html_str = html_node.to_html()

    title = extract_title(contents_md_file)

    content = contents_html_file.replace("{{ Title }}", title)
    content = content.replace("{{ Content }}", html_str)

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    with open(f"{dest_path}/index.html", "w") as f:
        f.write(content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for i in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, i)) and i.endswith('.md'):
            generate_page(dir_path_content, template_path, dest_dir_path)
        if os.path.isdir(os.path.join(dir_path_content, i)):
            if not os.path.isdir(os.path.join(dest_dir_path, i)):
                os.mkdir(os.path.join(dest_dir_path, i))
            generate_pages_recursive(os.path.join(dir_path_content, i), template_path, os.path.join(dest_dir_path, i))