from cpy import cpy
from generate_pages_recursive import generate_pages_recursive

import sys

def main():
    basepath = sys.argv
    if basepath is None:
        basepath = "/"
    src = "static/"
    dest = "docs"
    cpy(src, dest)

    from_path = "content"
    template_path = "template.html"
    generate_pages_recursive(from_path, template_path, dest, basepath)

main()
