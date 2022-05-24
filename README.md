# svghelper
Python SVG helper. set/replace svg color, etc.

## Install
`python -m pip install svghelper`

## Method Overview
* `set_color(input_file: str, output_file: str, color: str)` - set the color of a svg file. `input_file` is source, `output_file` is result. `color` argument should be 6 digits string color like `#FF0000`.
* `set_files_color(input_dir: str, output_dir: str, output_color: str)` - set the color of svg files in the `input_dir`.
* `replace_color(input_file: str, output_file: str, input_color: str, output_color: str)` - replace the color.
* `replace_files_color(input_dir: str, output_dir: str, input_color: str, output_color: str)` - replace svg files' color.
* `set_comp_color(input_file: str, output_file: str)` - set complementary color.
* `set_files_comp_color(input_dir: str, output_dir: str)` - set svg files' complementary color

## Example
### Code Sample
```python
import svghelper

# Copy capture.svg as capture2.svg and change the major color of it to #FF0000(red)
svghelper.set_color('capture.svg', 'capture2.svg', '#FF0000')
```

### Result
#### Before
![image](https://user-images.githubusercontent.com/55078043/163768522-e7f39eeb-8c6d-4fe8-a3ee-45283a3f6b2b.png)
#### After
![image](https://user-images.githubusercontent.com/55078043/163768599-55d32215-77dc-4759-8e72-a679730d3434.png)
