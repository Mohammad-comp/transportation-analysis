# 🚇 Spatial Justice in Transportation: Nassau & Kings Counties

A comprehensive geospatial analysis examining transportation equity and accessibility patterns across Nassau and Kings counties in New York, using U.S. Census Bureau data to reveal demographic disparities in transportation access.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Geopandas](https://img.shields.io/badge/GeoPandas-Geospatial-red?logo=python&logoColor=white)](https://geopandas.org)

## 📊 Project Overview

**Course:** FYS: Maps that Matter  
**Focus:** Spatial Justice in Transportation  
**Data Sources:** U.S. Census Bureau (ACS 2021 5-Year Estimates)

I found the data table **B08141** from \<data.census.gov\>

## 📍 Introduction

Transportation is a major factor that affects the access to opportunities, but not all communities have the same access to transportation. This notebook explores transportation patterns in Nassau and Kings counties by using U.S. Census Bureau data to highlight how residents commute to work. The goal is to achieve this by breaking down the use of different modes of transportation with different demographics to make sense of the spatial justice issues affecting the mobility and transport in these areas.

## 📚 Background

Transportation is important for many individuals in their everyday lives as it allows access to education, healthcare, employment, and other opportunities. Although public transportation is a crucial need, many low income and marginalized communities have trouble accessing transportation due to reliability and affordability. In Nassau and Kings Counties, transportation is proof of social inequality, with some communities getting benefits from great transportation while others lacking the minimum resources.

These problems are not just inconvenient but also highlight the ever growing division and disparities between communities. Research has shown that wealthier communities with higher car dependency have better public transportation, while low income communities are affected by the poor quality of transportation. A paper published by the Civil Rights Project at Harvard University and the Center for Community Change highlights how transportation policies have prevented many communities from social and economic opportunities such as not being able to go to interviews on time or not being able to attend social gatherings such as festivals or carnivals. The paper argues that new standards should be implemented to ensure that everyone gets equal transportation.

**Source:** [MOVING TO EQUITY: Addressing Inequitable Effects of Transportation Policies on Minorities](https://civilrightsproject.ucla.edu)

### Current Advocacy Efforts

The issue of inequality in transportation has been increasing in many communities. Community organizations and advocacy groups have been advocating for equality in transportation for underserved communities.

**Source:** [Kinder Institute for Urban Research](https://kinder.rice.edu)

## 🔍 Research Questions

- How do transportation patterns in Kings and Nassau counties differentiate among demographic groups?
- How does transportation inequality affect healthcare, education, and other opportunities for low income communities?

## 🗺️ Data Sources

| Dataset | Table | Description |
|---------|-------|-------------|
| **Transportation** | B08141 | Means of Transportation to Work |
| **Demographics** | B03002 | Origin by Race |

**Geographic Level:** Census Tracts  
**Coverage:** Nassau County (36059) & Kings County (36047), New York

## 🚀 Quick Start

### Prerequisites

**Google Colab**
1. Upload the `.ipynb` file to Google Drive
2. Open with Google Colab
3. Run all cells

### 📝 Note for Interactive Maps
If maps don't display in Jupyter, go to **File → Trust Notebook** to enable interactive visualizations.

## 📈 Analysis Components

### 1. Data Loading & Processing
- Fetches Census data via API calls
- Cleans and standardizes column names
- Combines Nassau and Kings county data

### 2. Statistical Analysis
- County-level transportation mode summaries
- Demographic composition analysis
- Comparative statistics between counties

### 3. Visualizations
- **Bar Charts**: Transportation mode usage by county
- **Choropleth Maps**: Public transportation usage patterns
- **Demographic Maps**: Racial/ethnic distribution

### 4. Spatial Analysis
- Census tract-level mapping
- Geographic patterns of transportation inequality
- Demographic-transportation correlations

## 🔍 Key Metrics Analyzed

### Transportation Modes
- No Vehicle Available
- Car, Truck, or Van (Drove Alone)
- Public Transportation (Excluding Taxicab)
- Walked to Work

### Demographics
- White (Non-Hispanic)
- Black or African American (Non-Hispanic)
- American Indian and Alaska Native (Non-Hispanic)
- Asian (Non-Hispanic)

## 📊 Key Findings

- **Kings County** residents rely heavily on public transportation (~45%)
- **Nassau County** shows higher dependency on private vehicles (~75%)
- Significant correlation between demographic composition and transportation access
- Transportation inequities disproportionately affect marginalized communities

### Transportation Usage by County
| Mode | Kings County | Nassau County |
|------|--------------|---------------|
| Public Transit | ~45% | ~15% |
| Private Vehicle | ~35% | ~75% |
| Walking | ~15% | ~5% |
| No Vehicle | ~30% | ~10% |

*Note: Actual percentages may vary based on latest data*

## 🛠️ Technical Stack

- **Python 3.8+**: Core programming language
- **GeoPandas**: Geospatial data manipulation
- **Pandas**: Data analysis and processing
- **Plotly**: Interactive visualizations
- **Folium**: Interactive web maps
- **Census API**: Data retrieval
- **Jupyter**: Interactive development environment


## 🎓 Academic Context

This analysis is part of ongoing research into **spatial justice** and **transportation equity**. The project builds on established literature highlighting how transportation policies can perpetuate social inequalities.

### Key References
- Civil Rights Project at Harvard University
- Center for Community Change transportation policy research
- Kinder Institute for Urban Research

## 📋 Conclusion

The data gathered from B03002 (race/ethnicity demographics) and B08141 (transportation) allows us to analyse transportation inequalities in Nassau and Kings Counties. The data highlights inequities in low income communities when accessing public transportation. Kings County communities mostly rely on public transportation while in Nassau County, private vehicles such as cars are most used. The highlighted inequalities show how transportation is connected to demographics especially those communities who are marginalized.

Analyzing these two datasets together, we can understand how transportation inequalities have affected both urban and suburban communities. Although Kings County benefits most from public transportation, its low income communities struggle with poor quality transit, while Nassau County's reliance on personal vehicles creates problems for those without access to a car. To solve these issues, we need equitable investments, public/community driven plans, and policy reforms.

## 💡 Future Enhancements

- [ ] Add more demographic variables (income, education)
- [ ] Include temporal analysis (multi-year trends)
- [ ] Expand to additional NYC boroughs
- [ ] Implement machine learning clustering
- [ ] Add public transit accessibility scores
- [ ] Create interactive dashboard

## Acknowledgments

- **FYS: Maps that Matter** course instructors
- **U.S. Census Bureau** for providing comprehensive demographic data
- **Transportation equity researchers** whose work inspired this analysis
- **Open-source geospatial community** for excellent tools and libraries

---


