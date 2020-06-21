import pandas as pd
import numpy as np
import warnings

import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
# RAW DATA METHODS

# class Plot:
#     def __init__(self, df, cols = None, fig_data):
#         self.df = df
#         if cols is not None:
#             self.df = df[[cols]]
#         self.fig = 

def num_nan_plot(df: pd.DataFrame, cols: list = None):
    if cols is not None:
        df = df[[cols]]
    fig = go.Figure(
        data=go.Bar(x=df.columns, y=(df.isnull().sum())),
        layout=go.Layout(
            title={
                'text': 'Number of NaN Values in Each Column',
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
            },
            xaxis_title='Column',
            yaxis_title='Number of NaN values',
            yaxis=dict(rangemode='nonnegative'),
        )
    )
    return fig


def percent_nan_plot(df: pd.DataFrame, cols: list = None):
    if cols is not None:
        df = df[[cols]]
    fig = go.Figure(
        data=go.Bar(x=df.columns, y=(df.isnull().sum() / df.shape[0])),
        layout=go.Layout(
            title={
                'text': 'Percent of NaN values in Each Column',
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
            },
            xaxis_title='Column',
            yaxis_title='Percent NaN',
            yaxis=dict(tickformat='.0%', rangemode='nonnegative')
        )
    )
    return fig

# CLEAN DATA METHODS


def correlation_plot(df: pd.DataFrame, cols: list = None):
    """Returns correlation plot for all features in given DataFrame"""
    if cols is not None:
        df = df[[cols]]
    if df.isna().sum().sum() > 0:
        warnings.warn(
            "DataFrame contains NaN values, correlations are not well defined (will be infinity)")
    fig = go.Figure(
        data=go.Heatmap(z=df.corr(), x=df.corr().columns,
                        y=df.corr().columns, hoverongaps=False),
        layout=go.Layout(
            height=900,
            width=900,
            title={
                'text': 'Variable Correlation Matrix',
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            })
        )
    return fig


def pairwise_plot(df: pd.DataFrame, cols: list = None):
    """Returns pairplot for features listed in cols parameter"""
    if cols is not None:
        df = df[[cols]]
    fig = go.Figure(
        data=go.Splom(
            dimensions=[{'label': i, 'values': df[i]} for i in cols],
        ),
        layout=go.Layout(
            title={
                'text':'Pairwise Plot',
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'

            }
        )
    )
    return fig


def distribution_plot(df: pd.DataFrame, cols: list = None):
    """ Returns overlayed distributions for the given columns"""
    l = [df[i] for i in cols]  # generate list of each column as specified by the ff documentation
    fig = ff.create_distplot(l, cols)
    fig.update_layout(
        title={
            'text': 'Distribution Plot',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )
    return fig