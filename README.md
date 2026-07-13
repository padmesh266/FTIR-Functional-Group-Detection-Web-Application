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
- O-H: 3000-3400
- C-H: 2800-3000
- C=O: 1600-1700
- C=C: 1510-1620
- C-H: 1325-1460
- C-O: 1030-1280
- C-H: 750-900
- Si-O-Si: 590-785

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

## Author Notes
Update this README as features evolve so users can understand setup, usage, and analysis assumptions.
