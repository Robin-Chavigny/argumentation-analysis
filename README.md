# Argumentation Analysis

## Description
This project is part of my 2024 internship at JAIST University, spanning from May to September. The goal of this project is to create an artificial intelligence system capable of extracting and analyzing arguments in political debates. 

The original dataset (`python/full_data.csv`) is sourced from [this repository](https://github.com/rafamestre/m-arg_multimodal-argumentation-dataset/tree/main), created by extracting data from audio recordings of the US 2020 presidential debates. This project encompasses both the visualization part (PyArg) and the analysis part (python).

### Analysis Part
- **`python/data_extraction.ipynb`**: This notebook generates graphs to analyze the content of the `python/full_data.csv` file. It is used in the 'Choose Topic' section of the Visualization page.
- **`python/Argumentation_Mining_Systeme.ipynb`**: This notebook is used to create the AI system that classifies various arguments and their relationships. The results are displayed in the 'Machine Learning' section of the Visualization page.
- **`python/explanation.py`**: This script provides an explanation of the results generated by the `Argumentation_Mining_Systeme.ipynb` notebook and is featured in the 'Explanation' section of the Visualization page.

### Visualization Part
- **`PyArg/src`**: This directory contains all the visualizations of the results and the presentation of the project.

## Prerequisites
- Python 3.8+
- pip

# Clone the repository
git clone https://github.com/Robin-Chavigny/argumentation-analysis

# Go to the project directory
cd argumentation-analysis

# Install dependencies
pip install -r requirements.txt

# Launch the application
python PyArg\src\py_arg_visualisation\app.py

# Open the web deployement
heroku open

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Installation
```bash

