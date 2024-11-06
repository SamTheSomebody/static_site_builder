import os
import shutil
from markdown_to_html import markdown_to_html_node
from html_node import *

def main():
    delete_and_copy_files()
    generate_pages_recursive("content", "template.html", "public")


def delete_and_copy_files():
    dest_path = os.path.realpath("public")
    print(f"Destination path is: {dest_path}")
    src_path = os.path.realpath("static")
    print(f"Source path is: {src_path}")
    if os.path.exists(dest_path):
        print(f"Removing directory: {dest_path}")
        shutil.rmtree(dest_path, ignore_errors = False)
    os.mkdir(dest_path)
    copy_file(src_path)

def copy_file(path):
    print(f"Looking through: {path}")
    sub_paths = os.listdir(path)
    for sub_path in sub_paths:
        print(sub_path)
        full_path = os.path.join(path, sub_path)
        dest_path = full_path.replace("/static/", "/public/")
        print(f"Copying: {full_path} to: {dest_path}")
        if os.path.isfile(full_path):
            shutil.copy(full_path, dest_path)
        else:
            os.mkdir(dest_path)
            copy_file(full_path)

def extract_title(markdown):
    if "# " not in markdown:
        raise ValueError("Markdown contains no H1 header")
    heading = markdown.split("# ")[1]
    heading = heading.splitlines()[0]
    return heading.strip()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, encoding="utf-8") as t:
        template = t.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html)
    parent_directory = os.path.dirname(dest_path)
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory, exist_ok=True)
    with open(dest_path, "w") as x:
        x.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Currently at: {dir_path_content}")
    if os.path.isfile(dir_path_content):
        if ".md" in dir_path_content:
            generate_page(dir_path_content, template_path, dest_dir_path.replace(".md", ".html"))
        return
    sub_paths = os.listdir(dir_path_content)
    for sub_path in sub_paths:
        path = os.path.join(dir_path_content, sub_path)
        dest_path = os.path.join(dest_dir_path, sub_path)
        print(f"Found: {path}")
        generate_pages_recursive(path, template_path, dest_path)
main()

