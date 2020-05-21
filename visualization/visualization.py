import pandas as pd
import numpy as np
import plotly.graph_objects as go
import warnings

# RAW DATA METHODS
def num_nan_plot(df: pd.DataFrame):
    fig = go.Figure(
        data=go.Bar(x=df.columns, y=(df.isnull().sum())),
        layout=go.Layout(
            title={
                'text':'Number of NaN Values in Each Column',
                'y':0.9,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            },
            xaxis_title='Column',
            yaxis_title='Number of NaN values',
            yaxis = dict(rangemode='nonnegative'),
        )
    )
    return fig

def percent_nan_plot(df: pd.DataFrame):
    fig = go.Figure(
        data=go.Bar(x=df.columns, y=(df.isnull().sum() / df.shape[0])),
        layout=go.Layout(
            title={
                'text':'Percent of NaN values in Each Column',
                'y':0.9,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            },
            xaxis_title='Column',
            yaxis_title='Percent NaN',
            yaxis=dict(tickformat='.0%', rangemode='nonnegative')
        )
    )
    return fig
    ws
# CLEAN DATA METHODS
def generate_correlation_plot(df: pd.DataFrame):
    if df.isna().sum().sum() > 0:
        warnings.warn("DataFrame contains NaN values, correlations will be infinite")
    fig = go.Figure(
    data=go.Heatmap(z=df.corr(), x=df.corr().columns, y=df.corr().columns, hoverongaps=False), 
        layout=go.Layout(
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
