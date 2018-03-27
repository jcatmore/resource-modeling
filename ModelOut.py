#! /usr/bin/env python


"""
Common plotting code
"""

from __future__ import absolute_import, division, print_function

import matplotlib
matplotlib.use('Agg')

import pandas as pd

# Make sort order that includes tiers from unrefined to refined and both string and integer years
SORT_ORDER = ['Run1 & 2', 'Ops space', 'RAW', 'GENSIM', 'AOD', 'MINIAOD', 'MICROAOD', 'USER'] + \
             [str(year) for year in range(2006, 2050)] + list(range(2006, 2050))
COLOR_MAP = 'Paired'


def plotStorageWithCapacity(data, name, title='', columns=None, bars=None):
    bars = sorted(bars, key=SORT_ORDER.index)
    frame = pd.DataFrame(data, columns=columns)
    ax = frame[bars + ['Year']].plot(x='Year', kind='bar', stacked=True, colormap=COLOR_MAP)
    ax.set(ylabel='PB', title=title)

    ax.legend(loc='best', markerscale=0.25, fontsize=11)
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    fig = ax.get_figure()
    fig.savefig(name)


def plotStorage(data, name, title='', columns=None, index=None):
    # Make the plot of produced data per year (input to other plots)
    plot_order = sorted(columns, key=SORT_ORDER.index)
    frame = pd.DataFrame(data, columns=columns, index=index)
    ax = frame[plot_order].plot(kind='bar', stacked=True, colormap=COLOR_MAP)
    ax.set(ylabel='PB', title=title)

    ax.legend(loc='best', markerscale=0.25, fontsize=11)
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    fig = ax.get_figure()
    fig.savefig(name)


def plotEvents(data, name, title='', columns=None, index=None):
    # Make the plot of produced events per year by type (input to other plots)
    plot_order = sorted(columns)
    frame = pd.DataFrame(data, columns=columns, index=index)
    print(title)
    print(frame)
    ax = frame[plot_order].plot(kind='bar', stacked=True, colormap=COLOR_MAP)
    ax.set(ylabel='Billions of events', title=title)
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    fig = ax.get_figure()
    fig.savefig(name)
