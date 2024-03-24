#!/usr/bin/python3
""" a script that takes an argument 2 strings"""

import sys
import os
import markdown2


def convert_markdown_to_html(input_file, output_file):
    """Converts Markdown content to HTML.

    Args:
    input_file: First argument, the name of the Markdown file
    output_file: Second argument the output file name

    """
    if not os.path.isfile(input_file):
        print("Missing {}".format(input_file), file=sys.stderr)
        sys.exit(1)

    with open(input_file, "r") as markdown_file:
        markdown_texts = markdown_file.read()

    html_tags = markdown2.markdown(markdown_texts)

    with open(output_file, "w") as html_file:
        html_file.write(html_tags)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file.md> "
              "<output_file.html>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_markdown_to_html(input_file, output_file)
