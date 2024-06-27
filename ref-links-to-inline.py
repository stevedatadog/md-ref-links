import re
import argparse
import sys

def convert_reference_links_to_inline(input_file, output_file=None):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Regular expression to find reference-style links and definitions
    link_regex = re.compile(r'\[([^\]]+)\]\[([^\]]+)\]')
    ref_def_regex = re.compile(r'^\[([^\]]+)\]:\s*(\S+)')

    # Dictionary to store reference definitions
    references = {}

    # First pass: extract all reference definitions
    for line in lines:
        match = ref_def_regex.match(line)
        if match:
            reference, url = match.groups()
            references[reference] = url

    # Second pass: convert reference-style links to inline links
    new_lines = []
    for line in lines:
        # Skip reference definitions
        if ref_def_regex.match(line):
            continue

        def replace_link(match):
            text, reference = match.groups()
            url = references.get(reference, '')
            return f'[{text}]({url})'

        new_line = link_regex.sub(replace_link, line)
        new_lines.append(new_line)

    if output_file:
        with open(output_file, 'w') as file:
            file.writelines(new_lines)
    else:
        sys.stdout.writelines(new_lines)

def main():
    parser = argparse.ArgumentParser(description='Convert reference-style links to inline links in a Markdown file.')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output file (if not provided, prints to STDOUT)', default=None)

    args = parser.parse_args()
    convert_reference_links_to_inline(args.input_file, args.output)

if __name__ == '__main__':
    main()

