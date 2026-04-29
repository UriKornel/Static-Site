import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_path_content = os.path.abspath(dir_path_content)
    template_path = os.path.abspath(template_path)
    dest_dir_path = os.path.abspath(dest_dir_path)

    print(f"content path: {dir_path_content}")
    print(f"template path: {template_path}")
    print(f"destination path: {dest_dir_path}")

    if not os.path.exists(dir_path_content):
        raise Exception("Generate error: Content Path does not exist")
    elif not os.path.exists(template_path):
        raise Exception("Generate error: template does not exist")

    for file in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, file)
        if os.path.isfile(src_path) and src_path.endswith(".md"):
            generate_page(src_path, template_path, dest_dir_path, basepath)
        elif os.path.isdir(src_path):
            dest_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(src_path, template_path, dest_path, basepath)
