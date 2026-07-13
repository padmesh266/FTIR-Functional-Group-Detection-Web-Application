# 🎯 COMPLETE WEB APPLICATION SETUP GUIDE
# Excel Upload + Automatic Graph Generation

---

## 📦 WHAT YOU GET

**3 Files:**
1. **app.py** - Backend (Flask server)
2. **templates/index.html** - Frontend (Web interface)
3. **requirements.txt** - All dependencies

**Features:**
✅ Upload Excel (.xlsx, .xls) or CSV files
✅ Automatically detects columns from first row
✅ Select X-axis and Y-axis from dropdown
✅ Choose graph type (Line, Bar, Scatter, Histogram, Pie)
✅ Custom graph titles
✅ Download graphs as PNG files
✅ Beautiful modern interface
✅ Drag & drop file upload

---

## 🚀 STEP 1: Install Dependencies

Open terminal and run:

```
pip install -r requirements.txt
```

Or install individually:

```
pip install Flask pandas matplotlib openpyxl
```

---

## 📁 STEP 2: File Structure

Create this folder structure:

```
project_folder/
├── app.py                  (Backend code)
├── requirements.txt        (Dependencies)
├── templates/
│   └── index.html         (Frontend code)
└── uploads/               (Created automatically)
```

**Folder creation command:**
```
mkdir templates
mkdir uploads
```

---

## ▶️ STEP 3: Run the Application

Navigate to your project folder and run:

```
python app.py
```

You should see:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## 🌐 STEP 4: Open in Browser

Open your web browser and go to:

```
http://127.0.0.1:5000
```

or

```
http://localhost:5000
```

---

## 📊 HOW TO USE THE WEB APP

### Step 1: Upload Excel File
- Click "Choose File" button
- Select your Excel (.xlsx) or CSV file
- File info appears (rows, columns)

### Step 2: Select Axes
**X-Axis (Horizontal):** Choose column for horizontal axis
**Y-Axis (Vertical):** Choose column for vertical axis

The dropdowns are automatically filled from your file's header row!

### Step 3: Choose Graph Type
- **Line Graph** - Show trends over time
- **Bar Chart** - Compare values
- **Scatter Plot** - Show relationships
- **Histogram** - Show distributions
- **Pie Chart** - Show percentages

### Step 4: Add Title
Enter custom title for your graph (optional)

### Step 5: Create Graph
Click "Create Graph" button
Graph appears instantly!

### Step 6: Download
Click "Download Graph" to save as PNG

---

## 📋 EXAMPLE USAGE

### Excel File Structure:

**File: sales.xlsx**
```
Month,Sales,Expenses,Profit
January,5000,3000,2000
February,6500,3500,3000
March,7200,3800,3400
April,8100,4000,4100
```

### Using the Web App:
1. Upload sales.xlsx
2. X-Axis: "Month"
3. Y-Axis: "Sales"
4. Graph Type: "Line Graph"
5. Title: "Monthly Sales Trend"
6. Click "Create Graph"
7. Download as PNG

---

## 🎨 GRAPH TYPES EXPLAINED

### 1. LINE GRAPH
**Use when:** Showing trends over time
**Example:** Sales growth month by month

### 2. BAR CHART
**Use when:** Comparing values across categories
**Example:** Sales by product type

### 3. SCATTER PLOT
**Use when:** Showing relationship between two variables
**Example:** Price vs Sales volume

### 4. HISTOGRAM
**Use when:** Showing data distribution
**Example:** Distribution of student scores

### 5. PIE CHART
**Use when:** Showing parts of a whole
**Example:** Market share by company

---

## 📝 SUPPORTED FILE FORMATS

✅ Excel 2007+ (.xlsx) - **RECOMMENDED**
✅ Excel 97-2003 (.xls)
✅ Comma-Separated Values (.csv)

**File size:** Up to 5MB

**Requirements:**
- First row must contain column headers
- Data should be in columns

---

## 🔧 TROUBLESHOOTING

### Problem: "Address already in use"
**Solution:** Port 5000 is busy. Change port in app.py:
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Changed to 5001
```

Then open: http://localhost:5001

---

### Problem: File won't upload
**Solutions:**
1. Check file format (.xlsx, .xls, or .csv)
2. Ensure first row has column headers
3. File size under 5MB
4. No special characters in column names

---

### Problem: Columns not appearing in dropdown
**Solution:**
1. Check first row has column names
2. No empty columns
3. Column names don't have extra spaces

---

### Problem: Graph won't create
**Solutions:**
1. Select both X and Y axes
2. Use columns with data
3. For Pie chart: Y-axis must have numbers

---

### Problem: "ModuleNotFoundError"
**Solution:** Install requirements:
```
pip install -r requirements.txt
```

---

## 🎯 COMPLETE EXAMPLE

**Sample Excel File: students.xlsx**

| Name | Math | English | Science |
|------|------|---------|---------|
| Alice | 85 | 90 | 88 |
| Bob | 78 | 82 | 85 |
| Charlie | 92 | 88 | 95 |
| Diana | 88 | 91 | 89 |

**How to use:**

**Graph 1: Math vs English Scores**
- X-Axis: Name
- Y-Axis: Math
- Type: Bar Chart
- Title: "Math Scores by Student"

**Graph 2: Overall Performance**
- X-Axis: Name
- Y-Axis: Science
- Type: Scatter Plot
- Title: "Science Scores"

**Graph 3: Subject Distribution**
- X-Axis: Name
- Y-Axis: Math
- Type: Pie Chart
- Title: "Score Distribution"

---

## 💾 HOW GRAPHS ARE SAVED

**Saved Locations:**

1. **View in Browser:**
   - Displays immediately after "Create Graph"
   - Can zoom, take screenshots

2. **Download as PNG:**
   - High quality (300 DPI)
   - Filename: graph.png
   - Downloads to your Downloads folder

3. **Server Side:**
   - Stored in 'uploads/' folder temporarily
   - Automatically cleaned up

---

## 🔐 SECURITY FEATURES

✅ File upload validation
✅ File size limit (5MB)
✅ Allowed file types only
✅ Secure filename handling
✅ No code execution from files

---

## 📊 AXIS LABELS EXPLAINED

The application **automatically uses your column names as axis labels**!

**Example:**

Excel file has columns: `Date, Temperature, Humidity`

When you select:
- X-Axis: "Date" → Horizontal axis shows "Date"
- Y-Axis: "Temperature" → Vertical axis shows "Temperature"

**No manual typing needed!**

---

## 🎨 CUSTOMIZATION

### Change Graph Title
Simply type in the "Graph Title" field
(Appears at top of graph)

### Change Colors
Edit in app.py, find graph creation section:

```python
plt.plot(df[x_column], df[y_column], color='blue')  # Change to: red, green, orange, etc.
plt.bar(df[x_column], df[y_column], color='green')  # Change color here
```

### Change Graph Size
Edit in app.py:

```python
plt.figure(figsize=(12, 6))  # Width, Height in inches
# Change to: (16, 8) for larger, (8, 4) for smaller
```

---

## 📈 DATA PREPARATION TIPS

### Good Format ✅
```
Date,Sales,Cost
2024-01-01,1000,500
2024-01-02,1200,600
```

### Bad Format ❌
```
Date,Sales,Cost,,,
2024-01-01,1000,500,
2024-01-02,1200,600,
```

### Tips:
- No empty rows in data
- No empty columns
- Column names in first row only
- Consistent data types (numbers vs text)

---

## 🚀 ADVANCED: Modify Graph Types

Edit app.py to add new graph types:

```python
elif graph_type == 'box':
    import numpy as np
    plt.boxplot(df[y_column])
    plt.ylabel(y_column, fontsize=12)
```

Then add option in templates/index.html:

```html
<option value="box">Box Plot</option>
```

---

## 🎓 LEARNING RESOURCES

- Flask: https://flask.palletsprojects.com/
- Pandas: https://pandas.pydata.org/
- Matplotlib: https://matplotlib.org/
- JavaScript Fetch API: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

---

## ✅ QUICK CHECKLIST

- [ ] Python installed (python --version)
- [ ] Flask installed (pip install Flask)
- [ ] pandas installed (pip install pandas)
- [ ] matplotlib installed (pip install matplotlib)
- [ ] app.py in main folder
- [ ] templates/index.html created
- [ ] Run: python app.py
- [ ] Open: http://localhost:5000
- [ ] Upload Excel file
- [ ] Select axes
- [ ] Create graph
- [ ] See beautiful graph!

---

## 📞 QUICK HELP

| Problem | Solution |
|---------|----------|
| Port in use | Change port 5000 to 5001 |
| Module not found | pip install -r requirements.txt |
| File won't upload | Check format (.xlsx, .csv) |
| No columns in dropdown | First row must have headers |
| Graph won't create | Select both X and Y axes |
| Can't open browser | Check: http://127.0.0.1:5000 |

---

## 🎉 YOU'RE READY!

You now have a professional-grade Excel to Graph application!

**Features:**
✅ Upload any Excel/CSV file
✅ Automatic column detection
✅ Multiple graph types
✅ Beautiful interface
✅ Download as high-quality PNG
✅ Modern responsive design

**Happy graphing!** 📊