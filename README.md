# FTIR Functional Group Detection Web App

## Project Heading
FTIR Functional Group Detection and Visualization System

## Project Description
This project is a Flask-based web application that analyzes FTIR CSV data and automatically highlights likely spectral peaks with functional-group labels.

It is designed for quick inspection of FTIR spectra by uploading a file, detecting important points in the curve, and showing them on an interactive plot.

## What This Project Does
- Accepts FTIR data as a CSV file upload.
- Reads data safely using multiple encoding fallbacks.
- Cleans and converts the first two columns to numeric values.
- Detects likely peaks using first and second derivatives.
- Maps peak positions to predefined functional-group ranges.
- Shows an interactive FTIR spectrum with:
  - Main spectrum line
  - Detected peak markers
  - Functional group annotations
- Displays the wavenumber axis in reversed FTIR style.

## Key Features
- Web interface for easy upload and visualization
- Automatic CSV encoding fallback (`utf-8`, `latin1`, `ISO-8859-1`)
- Noise-tolerant peak filtering using percentile threshold
- One label per functional group to reduce annotation clutter
- Interactive plot rendered with Plotly

## Tech Stack
- Python
- Flask
- Pandas
- NumPy
- Plotly

## How It Works
1. User uploads a CSV file from the browser.
2. Backend saves the file to the uploads folder.
3. Application reads and sanitizes the data.
4. Peak detection runs on the intensity values.
5. Peaks are checked against functional-group ranges.
6. Annotated interactive graph is generated and displayed.

## Input File Format
- File type: `.csv`
- Minimum expected content:
  - Column 1: Wavenumber values
  - Column 2: Absorbance/Intensity values
- Rows with invalid numeric values are removed during preprocessing.

## Functional Group Ranges Used
| **Wave Number (cm⁻¹)** | **Functional Groups** | **Assignment**                 |
| ---------------------- | --------------------- | ------------------------------ |
| 3000–3400              | O–H                | Alcohol, phenol, carboxylic acids |
| 2800–3000              | C–H                | Alkanes, alkanes (stretching)     |
| 1600–1700              | C=O                | Ketones, aldehydes                |
| 1510–1620              | C=C                | Olefinics, aromatics              |
| 1325–1460              | C–H                | Aliphatic (bending)               |
| 1030–1280              | C–O                | Alcohol, phenol, ester, ether     |
| 750–900                | C–H                | Aromatics (out-of-plane bending)  |
| 590–785                | Si–O–Si            | Siloxane / silica compounds       |


## Project Structure
```
FTIR/
  app.py
  data.csv
  requirements.txt
  WEB_APP_GUIDE.md
  templates/
    index.html
  static/
  uploads/
  graph_project/
```

## Installation
1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App
```bash
python app.py
```

Open in browser:
- http://127.0.0.1:8080

## Typical Use Case
- FTIR data exploration in lab workflows
- Quick first-pass identification of possible functional groups
- Educational demonstrations of FTIR spectrum interpretation

## Current Limitations
- Expects FTIR data in the first two columns.
- Uses rule-based ranges, not model-based classification.
- Peak detection may need tuning for highly noisy signals.

## Future Improvements
- Support user-selected columns from uploaded files.
- Add smoothing and baseline correction options.
- Export annotated peak tables.
- Add confidence scores for group matches.

## GitHub Link Placeholder
Repository URL:
https://github.com/padmesh266/FTIR-Functional-Group-Detection-Web-Application

## How the FTIR Peak Detection Works
The application processes FTIR spectrum data (wavenumber vs. absorbance) and identifies the most significant peaks that correspond to functional groups. The method relies on basic calculus concepts applied to the spectral curve.

- Step 1: Slope (First Derivative)
  - The first derivative of the absorbance curve tells us how steeply the signal is rising or falling.

  - A positive slope means the curve is going upward.

  - A negative slope means the curve is going downward.

  - A peak occurs when the slope changes from positive to negative.

- Step 2: Curvature (Second Derivative)
  - The second derivative measures how sharply the curve bends.

  - Large values indicate strong curvature, which corresponds to sharp peaks or troughs.

  - This helps distinguish real peaks from gentle fluctuations.

- Step 3: Detecting Peaks
  - A point is considered a peak if:

  - The slope changes sign (from rising to falling).

  - The curvature is strong enough (above a threshold).

  - This ensures that only meaningful peaks are detected, not noise.

- Step 4: Functional Group Ranges
  - Each functional group in chemistry absorbs infrared light in a characteristic wavenumber range. For example:

  - O–H stretch: 3000–3400 cm⁻¹

  - C=O stretch: 1600–1700 cm⁻¹

  - The algorithm checks which detected peaks fall inside these ranges.

- Step 5: Selecting the Most Significant Peak
  - If multiple peaks fall within the same functional group range, the algorithm chooses the one with the greatest change in slope (largest curvature).

  - Mathematically, this means selecting the point with the highest absolute value of the second derivative.

  - This ensures the sharpest, most prominent peak is labeled.

- Step 6: Annotation
  - The chosen peak is then labeled on the graph with the functional group name and its exact wavenumber. This makes the output clear and easy to interpret.
