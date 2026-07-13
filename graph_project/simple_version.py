import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')
print('Data loaded successfully!')
print(df)
print('\n')

# GRAPH 1: LINE GRAPH
print('Creating line graph...')
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], marker='o', color='blue', linewidth=2)
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('simple_graph.png')
plt.show()
print('✓ Saved as: simple_graph.png\n')

# GRAPH 2: BAR CHART
print('Creating bar chart...')
plt.figure(figsize=(10, 5))
plt.bar(df['Month'], df['Profit'], color='green', alpha=0.7)
plt.xlabel('Month')
plt.ylabel('Profit ($)')
plt.title('Monthly Profit')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('simple_bar_chart.png')
plt.show()
print('✓ Saved as: simple_bar_chart.png\n')

# GRAPH 3: PIE CHART
print('Creating pie chart...')
plt.figure(figsize=(8, 8))
total_sales = df['Sales'].sum()
total_expenses = df['Expenses'].sum()
total_profit = df['Profit'].sum()

plt.pie([total_sales, total_expenses, total_profit], 
        labels=['Sales', 'Expenses', 'Profit'], 
        autopct='%1.1f%%',
        colors=['blue', 'red', 'green'],
        startangle=90)
plt.title('Yearly Totals Distribution')
plt.tight_layout()
plt.savefig('simple_pie_chart.png')
plt.show()
print('✓ Saved as: simple_pie_chart.png\n')

print('=' * 50)
print('SUCCESS! All 3 graphs created!')
print('=' * 50)
print('\nGraph files:')
print('• simple_graph.png')
print('• simple_bar_chart.png')
print('• simple_pie_chart.png')