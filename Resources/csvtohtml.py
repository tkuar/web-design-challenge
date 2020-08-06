# Dependencies
import pandas as pd
import os

# Import CSV
weather_data = pd.read_csv('cities.csv')

# Create export path
export_path = os.path.join('..', 'data_raw.html')

# Export table as HTML
weather_data.to_html(export_path, index=False)