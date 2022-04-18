import xml.etree.ElementTree as ET


def set_svg_color(input_file: str, output_file: str, replace_color: str):
    tree = ET.parse(input_file)
    root = tree.getroot()
    for el in root.iter():
        name = el.tag.split('}')[1]
        if name == 'path':
            el.set('fill', replace_color)
    with open(output_file, 'wb') as f:
        tree.write(f)