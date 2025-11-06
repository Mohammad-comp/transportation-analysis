# -*- coding: utf-8 -*-
"""Transportation-tracts.ipynb

Original file is located at
    https://colab.research.google.com/drive/15n9LPxcmxs1g-CbCcG4pU9xVM8ZhNdKg

Spatial Justice in Transportation
===================
**FYS: Maps that Matter**

**Introduction:**
 - Transportation is a major factor that affects the access to opportunities, but not all communities have the same access to transportation. This notebook explores  transportation patterns in Nassau and Kings counties by using U.S. Census Bureau data to highlight  how residents commute to work. The goal is to achieve this by breaking down the use of different modes of transportation with different demographics  to make sense of the spatial justice issues affecting the mobility and transport in these areas.

**Background:**


- Transportation is important for many individuals in their everyday lives as it allows access to education, healthcare, employment, and other opportunities. Although public transportation is a crucial need, many low income and marginalized communities have trouble accessing transportation due to reliability and affordability. In Nassau and Kings Counties, transportation is proof of social inequality, with some communities getting benefits from great transportation while others lacking the minimum resources. These problems are not just inconvenient but also highlight the ever growing division and disparities between communities.
Research has shown that wealthier communities with higher car dependency have better public transportation, while low income communities are affected by the poor quality of transportation. A paper published by the Civil Rights Project at Harvard University and the Center for Community Change highlights how transportation policies have prevented many communities from social and economic opportunities such as not being able to go to interviews on time or not being able to attend social gatherings such as festivals or carnivals. The paper argues that new standards should be implemented to ensure that everyone gets equal transportation.


Source: [MOVING TO EQUITY:
Addressing Inequitable Effects of
Transportation Policies on Minorities](https://civilrightsproject.ucla.edu/research/metro-and-regional-inequalities/transportation/moving-to-equity-addressing-inequitable-effects-of-transportation-policies-on-minorities/sanchez-moving-to-equity-transportation-policies.pdf?utm_source=chatgpt.com)

Everyday Conversation:
- The issue of inequality in transportation has been increasing in many communities. Community organizations and advocacy groups have been advocating for equality in transportation for underserved communities.

Source: [Kinder Institute for Urban Research](https://kinder.rice.edu/urbanedge/racism-has-shaped-public-transit-and-its-riddled-inequities?utm_source=chatgpt.com)

Research Questins:
- How do transportation patterns in Kings and Nassau counties differentiate among demographic groups?
- How does transportation inequality affect healthcare, education, and other opportunities for low income communities?

Install Libraries
===================
"""

# Install Libraries
!pip install us https://github.com/mcuringa/cartopy/raw/refs/heads/main/dist/maptools-latest.tar.gz -q
import geopandas as gpd
import pandas as pd
import plotly.express as px
from maptools import census_vars, tiger, ui

"""Load Availabe Data
=============

Data table **B08141** from  <data.census.gov>


This table includes data about how people go to work or in other words what mode of transportation do workers take to get to work.
"""

# Load the transportation data for Nassau and Kings Counties
nassau_data = "https://api.census.gov/data/2022/acs/acs5?get=group(B08141)&ucgid=pseudo(0500000US36059$1400000)"
kings_data = "https://api.census.gov/data/2022/acs/acs5?get=group(B08141)&ucgid=pseudo(0500000US36047$1400000)"
meta_url = "https://api.census.gov/data/2022/acs/acs5"
nassau = census_vars.get(nassau_data, meta_url)
nassau["county"] = "nassau"
kings = census_vars.get(kings_data, meta_url)
kings["county"] = "kings"
df = pd.concat([nassau, kings])

# Load demographics data for Nassau and Kings Counties
nassau_data = "https://api.census.gov/data/2022/acs/acs5?get=group(B03002)&ucgid=pseudo(0500000US36059$1400000)"
kings_data = "https://api.census.gov/data/2022/acs/acs5?get=group(B03002)&ucgid=pseudo(0500000US36047$1400000)"
meta_url = "https://api.census.gov/data/2022/acs/acs5"
nassau = census_vars.get(nassau_data, meta_url)
nassau["county"] = "nassau"
kings = census_vars.get(kings_data, meta_url)
kings["county"] = "kings"
demographics = pd.concat([nassau, kings])
demographics.head()

"""# Specific Data

From the data table we extract the specific data we need. In this case, we only need the mode of transportation people take, not how many vehicles they have.

Data for Transportation:
"""

# Extract code that is needed and remove unneccessary columns.
cols = ['total',
        'county',
        'no_vehicle_available',
        'car_truck_or_van_drove_alone',
        'public_transportation_excluding_taxicab',
        'walked', 'geometry']

transit = df[cols].copy()

# Rename the columns for better understanding
new_cols = ['total',
            'county',
            'No Vehicle Available',
            'Car Truck or Van',
            'Public Transportation',
            'Walked', 'geometry']

transit.columns = new_cols

# Check the number of rows in transit
num_rows = len(transit)

# Sample the minimum of 5 or the available number of rows
sample_size = min(num_rows, 5)

# Sample the rows
transit.sample(sample_size)

"""Data for Demographics:"""

# Extract columns of interest for demographics
# Relevant demographic columns
demographic_cols = [
    'total',
    'not_hispanic_or_latino_white_alone',
    'not_hispanic_or_latino_black_or_african_american_alone',
    'not_hispanic_or_latino_american_indian_and_alaska_native_alone',
    'not_hispanic_or_latino_asian_alone',
    'geometry'
]
# Create a smaller DataFrame with the selected columns
demographics = demographics[demographic_cols].copy()


# Rename the columns for better understanding
new_demographic_cols = [
    'total',
    'White',
    'Black or African American',
    'American Indian and Alaska Native',
    'Asian',
    'geometry'
]
demographics.columns = new_demographic_cols

"""# Chart and Table

Now I take the filtered data that I need and program a table and a chart.

Table for Kings County:
"""

# Create a table
# List of columns that will be reflected in the table
transit_cols = ['total',
            'No Vehicle Available',
            'Car Truck or Van',
            'Public Transportation',
            'Walked',
]

# Copy the data so that transit doesn't get modified
# make it only kings county data
table_data = transit[transit.county == "kings"][transit_cols].copy()

# Handle missing values (fill with 0)
table_data = table_data.fillna(0)


# Sum all the values in each column, then convert to a DataFrame and transpose
table_data = table_data.sum().to_frame().T

# Show the resulting DataFrame
table_data

"""Chart for Kings County:"""

# Create the Chart
chart_title = "Transportation, Kings County"

# Everything but total
chart_cols = transit_cols[1:]

x_values = chart_cols
y_values = kings_table = table_data[chart_cols].iloc[0].tolist()

# Create the bar plot
fig = px.bar(y=y_values, x=x_values, title=chart_title)

# Update the layout to hide the legend and set y-axis formatting
fig.update_layout(
    yaxis_title="Total People",
    xaxis_title="Mode of Transportation",
    yaxis_tickformat=',',
    showlegend=False
)

fig.show()

"""Table for Nassau County:"""

# Create a table
# List of columns that will be reflected in the table
transit_cols = ['total',
            'No Vehicle Available',
            'Car Truck or Van',
            'Public Transportation',
            'Walked',
]
# Copy the data so that transit doesn't get modified
# make it only nassau county data
table_data = transit[transit.county == "nassau"][transit_cols].copy()

# Handle missing values (fill with 0)
table_data = table_data.fillna(0)


# Sum all the values in each column, then convert to a DataFrame and transpose
table_data = table_data.sum().to_frame().T

# Show the resulting DataFrame
table_data

"""Chart for Nassau County:"""

# Create the Chart
chart_title = "Transportation, Nassau County"

# everything but total
chart_cols = transit_cols[1:]

x_values = chart_cols
y_values = nassau_table = table_data[chart_cols].iloc[0].tolist()

# Create the bar plot
fig = px.bar(y=y_values, x=x_values, title=chart_title)

# Update the layout to hide the legend and set y-axis formatting
fig.update_layout(
    yaxis_title="Total People",
    xaxis_title="Mode of Transportation",
    yaxis_tickformat=',',
    showlegend=False
)

fig.show()

"""Create a Map that compares data
================================================

This map shows **Public Transportaton total** based on the data provided and geographic location.

Readers can see how public transportation is more used in Kings County compared to Nassau County.
"""

# Create a map showing public transportation usage
# Make sure this is the correct DataFrame that has the transportation data
map_data = transit.copy()

# Create a new column for total of public transportation usage
map_data["Public Transportation"] = round(map_data["Public Transportation"] / map_data["total"] * 100)

# Drop tracts with no data/no people
map_data = map_data[map_data["total"] > 0]

# Make a map showing the percentage of public transportation usage in a tract
base = ui.base_map(map_data, zoom=12)
map_data.explore(m=base, column='Public Transportation', tooltip="Public Transportation", cmap='Blues', legend=True)

"""This map shows **Demographic total** based on the data provided and geographic location.

Readers notice how there are more Black or African Americans in Kings county.


"""

# Drop tracts with no population
demographics = demographics[demographics['total'] > 0]

# Create the map for a specific demographic group
# Example: Black or African American Alone total
base = ui.base_map(demographics, zoom=12)
demographics.explore( m=base, column='Black or African American', tooltip=['Black or African American'], cmap='Reds', legend=True)

"""**Conclusion:**
 - The data gathered from B03002 (race/ethnicity demographics) and B08141 (transportation) allows us to analyse transportation inequalities in Nassau and Kings Counties. The data highlights inequities in low income communitie when accessing public transportation. Kings County communities mostly rely on public transportation while in Nassau County, private vehicles such as cars are most used. The highlighted inequalities show how transportation is connected to demographics especially those communities who are marginalized.

 Analyzing these two datasets together, we can understand how transportation inequalities have affected both urban and suburban communities. Although Kings County benefits most from public transportation, its low income communities struggle with poor quality transit, while Nassau County's reliance on personal vehicles creates problems for those without access to a car. To solve these issues, we need equitable investments, public/community driven plans, and policy reforms.

"""
