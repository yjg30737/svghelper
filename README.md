# svghelper
Set svg color with Python

## Method Overview
* `set_svg_color(input_file: str, output_file: str, color: str)` - `input_file` is source, `output_file` is result. `color` argument should be 6 digits string color like `#FF0000`.

## Example
### Code Sample
```python
import svghelper

# Copy capture.svg as capture2.svg and change the major color of it to #FF0000(red)
python_set_svg_color.set_svg_color('capture.svg', 'capture2.svg', '#FF0000') 
```

### Result
#### Before
![image](https://user-images.githubusercontent.com/55078043/163768522-e7f39eeb-8c6d-4fe8-a3ee-45283a3f6b2b.png)
#### After
![image](https://user-images.githubusercontent.com/55078043/163768599-55d32215-77dc-4759-8e72-a679730d3434.png)
