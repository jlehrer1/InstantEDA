import pandas as pd
import numpy as np
import plotly.graph_objects as go

# RAW DATA METHODS
def num_nan_plot(df: pd.DataFrame):
    num_nans = sum([True for idx, row in df.iterrows() if any(row.isnull())])
    fig = go.Figure(
        data=go.Bar(x=df.columns, y=(df.isnull().sum())),
        layout=go.Layout(
            title={
                'text':'Number of NaN values in each column',
                'y':0.9,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            }
        )
    )

def percent_nan_plot(df: pd.DataFrame):
    pass

# CLEAN DATA METHODS
def generate_correlation_plot(df: pd.DataFrame):
    fig = go.Figure(data=go.Heatmap(
        z=df.corr(),
        x=df.corr().columns,
        y=df.corr().columns,
        hoverongaps=False,
    ), layout=go.Layout(
        height=900,
        width=900,
        title={
            'text': 'Variable Correlation Matrix',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    ))
    return fig
