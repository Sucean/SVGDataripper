# SVGDataripper  
## Extract Datapoints from graphs saved as Scalable Vector Graphics (svg)  

This project provides a Python class, `SVGDataripper`, for extracting data points from SVG files.  
It enables users to identify paths by stroke color, extract their coordinates, and map them to a  
specified data range, with support for both linear and logarithmic scaling on the x-axis.  
This tool is ideal for researchers and developers needing to digitize data from vector graphics.  

### Key Features  
- 🎨 **Color-based data extraction**: Extract paths from SVG files based on their stroke color.
- 📏 **Coordinate mapping**: Map extracted SVG coordinates to a specified data range.
- 📈 **Scaling options**: Support for both linear and logarithmic scaling on the x-axis.
- 🔍 **Data color identification**: Identify potential data colors used in the SVG file.


---

## Before you start:
**IMPORTANT** The extracted data is an approximation based on the visual data! It won't  
return the exact same data that was used for the graph in the first place! Please keep this in mind.  
Further - since he script uses the absolute coordinates of the SVG, it is necessary to crop  
the data region, removing e.g. title, axis annotations/labels, even tick marks! (Everything outside the plot area).  
For this purpose any vector graphic tool like [Inkscape](https://inkscape.org/) can be used.  

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Initializing the Class](#initializing-the-class)
  - [Finding Potential Data Colors](#finding-potential-data-colors)
  - [Extracting Data](#extracting-data)
- [License](#license)
- [References](#references)

---

## Installation

### Requirements

|Package        | Version   | Installation Command            |
|---------------|-----------|---------------------------------|
| Python        |  ≥3.8     | `conda install python=3.9.2`    |
| NumPy         |  1.19.x   | `pip install numpy==1.19.5`     |
| svgpathtools  |  1.7.x    | `pip install scipy==1.7.0`      |
|---------------|-----------|---------------------------------|


**For exact reproduction:**
```bash
pip install -r requirements.txt
```


### Option 1: Clone Repository (Development Setup)
For local development or to use as a Python package in your environment:  

```bash
git clone https://github.com/sucean/SVGDataripper.git
cd alphabetasquared
pip install -e .
```

### Option 2: Install via pip (Production Use)
```bash
pip install git+https://github.com/sucean/SVGDataripper.git
```
---
## Usage

First import the package into your prefered Python environment:  

```python
from SVGDataripper import SVGDataripper
```

### Initializing the Class

Create an instance of `SVGDataripper` by providing the path to your SVG file:  

```python
svg_file = "path/to/your/file.svg"
ripper = SVGDataripper(svg_file)
```

### Finding Potential Data to be extracted

Identify stroke colors in the SVG file using the `find_data` method:  

```python
color_counts = ripper.find_data()
print(color_counts)
```

This returns a dictionary with stroke colors as keys and their frequencies as values. Use this to select a color for `extract_data`.  

### Extracting Data

Use the `extract_data` method to extract coordinates from paths with a specific stroke color. Specify data ranges  
for x and y, and optionally use logarithmic scaling for the x-axis. **Important**, the x and y ranges are  
determined by the minimum and maximum values of your data and are independent from the axis!  

```python
data_color = "#ff0000"  # Red stroke color
data_x_range = (0, 10)  # Range of x-values
data_y_range = (0, 100) # Range of y-values
ripper.xlog = True      # Setting logarithmic scaling for x-axis, usually set to False
	                    # Use ripper.ylog = True if the y-axis is scaled log

data_x, data_y = ripper.extract_data(data_color, data_x_range, data_y_range)
```

This returns mapped x and y data points as NumPy arrays.  

## License


This project is licensed under the GNU General Public License version 2.0 (GNU GPL v2.0).  

Key Terms of the GNU GPL v2.0:

 1. **Source Code Distribution:** 
	If you distribute copies of the software, you must provide the source code or make it available upon request.
    
 2. **Copyleft Provision:**
	Any modifications or derivative works must also be licensed under the GNU GPL v2.0, ensuring that the software remains free and open-source.
    
 3. **No Warranty:** 
	The software is provided "as is," without warranty of any kind, express or implied.

For the full license text, please refer to the [GNU General Public License version 2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## References

- [SVG Path Tools Documentation](https://github.com/mathandy/svgpathtools)
- [NumPy Documentation](https://numpy.org/doc/)
