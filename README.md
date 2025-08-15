# COVID-19 Temporal Analysis

A comprehensive analysis of COVID-19 case evolution over time using Python data science libraries.

## Description

This project analyzes the temporal evolution of COVID-19 cases by country, focusing on Central American countries (El Salvador, Guatemala, and Honduras). The analysis includes data processing, monthly aggregation, and interactive visualizations.

## Features

- **Data Processing**: Clean and prepare COVID-19 time series data
- **Monthly Aggregation**: Group data by country and month for trend analysis
- **Interactive Visualizations**: Create dynamic charts using Plotly Express
- **Country Comparison**: Compare trends across multiple countries
- **Error Handling**: Robust validation for data availability

## Technologies Used

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **Plotly Express**: Interactive data visualization
- **Datetime**: Date and time handling

## Project Structure

```
covid-temporal-analysis/
│
├── covid_temporal_analysis.py     # Main Python script
├── covid_temporal_analysis.ipynb  # Jupyter notebook
├── README.md                      # Project documentation
└── covid.csv                      # COVID-19 dataset (not included)
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/covid-temporal-analysis.git
cd covid-temporal-analysis
```

2. Install required packages:
```bash
pip install pandas plotly
```

## Usage

### Using the Python Script

1. Place your COVID-19 CSV file in the project directory and name it `covid.csv`
2. Run the analysis:
```bash
python covid_temporal_analysis.py
```

### Using the Jupyter Notebook

1. Start Jupyter:
```bash
jupyter notebook
```

2. Open `covid_temporal_analysis.ipynb`
3. Run cells sequentially to perform the analysis

## Data Requirements

The CSV file should contain the following columns:
- `date`: Date in YYYY-MM-DD format
- `country`: Country name
- `total_cases`: Cumulative number of COVID-19 cases

## Example Output

The analysis generates an interactive line chart showing:
- Monthly evolution of total COVID-19 cases
- Separate lines for each country
- Hover information for detailed data points
- Time series comparison across countries

## Customization

You can modify the countries to analyze by changing the `countries_to_analyze` list in the code:

```python
countries_to_analyze = ['El Salvador', 'Guatemala', 'Honduras', 'Costa Rica', 'Nicaragua']
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- COVID-19 data sources
- Plotly development team for excellent visualization tools
- Pandas development team for powerful data analysis capabilities

## Contact

For questions or suggestions, please open an issue in this repository.
