import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import plotly.graph_objs as go
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ✅ SAFE CSV READER
def read_csv_safe(filepath):
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(filepath, encoding='latin1')
        except:
            df = pd.read_csv(filepath, encoding='ISO-8859-1')

    df.columns = df.columns.str.strip()

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.replace('\xa0', '', regex=False)

    df.iloc[:, 0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')
    df.iloc[:, 1] = pd.to_numeric(df.iloc[:, 1], errors='coerce')

    df = df.dropna()
    return df


# ✅ PEAK DETECTION
def detect_peaks(x, y):
    dy = np.gradient(y)
    d2y = np.gradient(dy)

    peaks = []
    threshold = np.percentile(abs(d2y), 75)

    for i in range(1, len(y) - 1):
        if (dy[i - 1] > 0 and dy[i + 1] < 0) or (dy[i - 1] < 0 and dy[i + 1] > 0):
            if abs(d2y[i]) > threshold:
                peaks.append(i)

    return peaks


# ✅ FUNCTIONAL GROUP RANGES
FUNCTIONAL_GROUPS = [
    ("O-H", 3000, 3400),
    ("C-H", 2800, 3000),
    ("C=O", 1600, 1700),
    ("C=C", 1510, 1620),
    ("C-H", 1325, 1460),
    ("C-O", 1030, 1280),
    ("C-H", 750, 900),
    ("Si-O-Si", 590, 785)
]


@app.route("/", methods=["GET", "POST"])
def index():
    plot_html = None

    if request.method == "POST":
        file = request.files["file"]

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            df = read_csv_safe(filepath)

            x = df.iloc[:, 0].values
            y = df.iloc[:, 1].values

            peaks = detect_peaks(x, y)

            dy = np.gradient(y)
            d2y = np.gradient(dy)

            annotations = []
            peak_x = []
            peak_y = []

            # ✅ For each functional group, pick the peak with greatest slope change
            for group, low, high in FUNCTIONAL_GROUPS:
                candidate_indices = [i for i in peaks if low <= x[i] <= high]

                if candidate_indices:
                    best_idx = max(candidate_indices, key=lambda i: abs(d2y[i]))

                    wn = x[best_idx]
                    peak_x.append(wn)
                    peak_y.append(y[best_idx])

                    offset = (max(y) - min(y)) * 0.08
                    if y[best_idx] > np.mean(y):
                        y_text = y[best_idx] + offset
                        arrow_dir = -30
                    else:
                        y_text = y[best_idx] - offset
                        arrow_dir = 30

                    annotations.append(
                        dict(
                            x=wn,
                            y=y_text,
                            text=f"{group} ({wn:.1f} cm⁻¹)",
                            showarrow=True,
                            arrowhead=2,
                            ax=0,
                            ay=arrow_dir,
                            font=dict(size=12, color="red")
                        )
                    )

            # ✅ CREATE GRAPH
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines',
                name='FTIR Spectrum'
            ))

            fig.add_trace(go.Scatter(
                x=peak_x,
                y=peak_y,
                mode='markers',
                marker=dict(size=8, color='red'),
                name='Detected Peaks'
            ))

            fig.update_layout(
                title="FTIR Functional Group Detection",
                xaxis_title="Wavenumber (cm⁻¹)",
                yaxis_title="Absorbance",
                annotations=annotations,
                xaxis=dict(autorange="reversed")
            )

            plot_html = fig.to_html(full_html=False)

    return render_template("index.html", plot_html=plot_html)


if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, port=8080)
