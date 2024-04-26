#!/usr/bin/python3
"""
Markdown to HTML Converter.
"""

import sys
import os
import markdown2


def convert_markdown_to_html(input_file, output_file):
    """Converts Markdown content to HTML.

    Args:
        input_file (str): The name of the Markdown file.
        output_file (str): The output file name.

    """
    if not os.path.isfile(input_file):
        print(f"Error: Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    with open(input_file, "r") as markdown_file:
        markdown_texts = markdown_file.read()

    html_tags = markdown2.markdown(markdown_texts)

    html_tags = html_tags.replace("# ", "<h1>").replace("## ", "<h2>").replace("### ", "<h3>").replace("#### ", "<h4>").replace("##### ", "<h5>").replace("###### ", "<h6>")
    html_tags = html_tags.replace("\n", "</h1>\n").replace("</h1>\n<h2>", "</h1>\n\n<h2>").replace("</h2>\n<h3>", "</h2>\n\n<h3>").replace("</h3>\n<h4>", "</h3>\n\n<h4>").replace("</h4>\n<h5>", "</h4>\n\n<h5>").replace("</h5>\n<h6>", "</h5>\n\n<h6>")

    with open(output_file, "w") as html_file:
        html_file.write(html_tags)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_markdown_to_html(input_file, output_file)
