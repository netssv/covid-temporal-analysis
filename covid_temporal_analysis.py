"""
COVID-19 Temporal Analysis - Version 2.0
========================================
Analysis of COVID-19 cases by country using Pandas and Plotly
"""

import pandas as pd
import plotly.express as px
from datetime import datetime
import os

def load_and_process_data(csv_path):
    """
    Load and process COVID-19 data from CSV file
    
    Args:
        csv_path (str): Path to the COVID-19 CSV file
        
    Returns:
        pd.DataFrame: Processed monthly data
    """
    # Read the CSV file
    df = pd.read_csv(csv_path)
    
    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'])
    
    # Create column for grouping by year and month
    df['year_month'] = df['date'].dt.to_period('M')
    
    print("Dates converted successfully")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    
    return df

def aggregate_monthly_data(df):
    """
    Aggregate data by country and month
    
    Args:
        df (pd.DataFrame): Raw COVID data
        
    Returns:
        pd.DataFrame: Monthly aggregated data
    """
    # Group by country and month, taking the maximum value of cases in that month
    df_monthly = df.groupby(['country', 'year_month'])['total_cases'].max().reset_index()
    
    # Convert 'year_month' to timestamp for proper plotting
    df_monthly['date'] = df_monthly['year_month'].dt.to_timestamp()
    
    return df_monthly

def filter_countries(df_monthly, countries_to_analyze):
    """
    Filter data for specific countries with error handling
    
    Args:
        df_monthly (pd.DataFrame): Monthly aggregated data
        countries_to_analyze (list): List of countries to analyze
        
    Returns:
        pd.DataFrame: Filtered data for found countries
    """
    print("Verifying selected countries:")
    found_countries = []
    
    for country in countries_to_analyze:
        if country in df_monthly['country'].unique():
            found_countries.append(country)
            print(f"Found: {country}")
        else:
            print(f"Not found: {country}")
    
    # Filter data for found countries
    df_countries = df_monthly[df_monthly['country'].isin(found_countries)].copy()
    
    print(f"\nFiltered data: {len(df_countries)} records for {len(found_countries)} countries")
    
    return df_countries

def create_evolution_chart(df_countries):
    """
    Create monthly evolution chart using Plotly Express
    
    Args:
        df_countries (pd.DataFrame): Filtered country data
        
    Returns:
        plotly.graph_objects.Figure: Interactive line chart
    """
    fig = px.line(df_countries,
                  x='date',
                  y='total_cases',
                  color='country',
                  title='Monthly Evolution of Total COVID-19 Cases by Country',
                  labels={'date': 'Month', 'total_cases': 'Total Cases', 'country': 'Country'})
    
    fig.update_layout(xaxis_title="Month",
                      yaxis_title="Total Cases",
                      hovermode="x unified")
    
    return fig

def main():
    """
    Main function to execute the COVID-19 analysis
    """
    # Countries to analyze (you can modify these)
    countries_to_analyze = ['El Salvador', 'Guatemala', 'Honduras']
    
    # Load and process data
    csv_path = "covid.csv"  # Update this path as needed
    df = load_and_process_data(csv_path)
    
    # Aggregate monthly data
    df_monthly = aggregate_monthly_data(df)
    
    # Filter for specific countries
    df_countries = filter_countries(df_monthly, countries_to_analyze)
    
    # Create and display chart
    fig = create_evolution_chart(df_countries)
    fig.show()

if __name__ == "__main__":
    main()
