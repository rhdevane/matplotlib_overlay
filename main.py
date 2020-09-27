# This is a sample Python script.
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from itertools import cycle
import plot_params as pp

def plot_frame():
    """create the base plot frame"""

    fig = plt.figure(figsize=pp.dims)
    fig.suptitle(pp.plot_title, fontsize=pp.title_font)
    #fig.xticks(fontsize=pp.tick_fontsize)

    return fig

def tick_position(ax):
    """set tick position"""

    xtickslocs = ax.get_xticks()
    ymin, _ = ax.get_ylim()

def make_patch_spines_invisible(ax):
    """make patch spines"""

    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

def data_range(field):
    """get range of data to set axis"""

    max = df[field].max()*1.1
    min = df[field].min()*0.25

    return min, max

def bar_text(ax, df, min):
    """add text measures over the bar chart"""

    for index, row in df.iterrows():
        ax.text(index, min * 1.7, pp.on_bar_label_1, color=pp.onbar_fontcolor,
                fontsize=pp.onbar_fontsize, ha="center")
        ax.text(index, min * 1.2, round(row[pp.on_bar_field_1], 2), color=pp.onbar_fontcolor,
                fontsize=pp.onbar_fontsize,ha="center")
        ax.text(index, min * 2.7, pp.on_bar_label_2, color=pp.onbar_fontcolor,
                fontsize=pp.onbar_fontsize, ha="center")
        ax.text(index, min * 2.2, round(row[pp.on_bar_field_2], 2), color=pp.onbar_fontcolor,
                fontsize=pp.onbar_fontsize, ha="center")


def make_subplot(fig, field, type, color, pad, inc, side):
    """create subplots"""

    min, max = data_range(field)
    curr_axes = fig.get_axes()

    if len(curr_axes) == 0:
        ax = fig.add_subplot()
        ax.set_xlabel(pp.xlabel, fontsize=pp.xlabel_fontsize)
        #ax.set_xticklabels(Fontsize=12)
        plt.xticks(fontsize=pp.xtick_fontsize)
        ax.spines["bottom"].set_linewidth(pp.frame_width)
        ax.spines["top"].set_linewidth(pp.frame_width)
        ax.spines["right"].set_linewidth(pp.frame_width)
        ax.spines["left"].set_linewidth(pp.frame_width)

    else:
        ax = curr_axes[0].twinx()
        ax.spines[side].set_position(("axes", inc))
        ax.spines[side].set_linewidth(pp.frame_width)
        make_patch_spines_invisible(ax)
        # the right amount
        fig.subplots_adjust(right=0.75)
        # spines
        ax.spines[side].set_visible(True)
        ax.yaxis.set_label_position(side)
        ax.yaxis.set_ticks_position(side)

    if type == 'bar':
        ax = sns.barplot(x='month', y=field, data=df, color=color)
        bar_text(ax, df, min)
        #for index, row in df.iterrows():
        #    ax.text(index, min * 1.7, pp.on_bar_label_1, color='darkblue', fontsize=pp.onbar_fontsize, ha="center")
        #    ax.text(index, min * 1.2, round(row[pp.on_bar_field_1], 2), color='darkblue', fontsize=pp.onbar_fontsize, ha="center")
        #    ax.text(index, min * 2.7, pp.on_bar_label_2, color='darkblue', fontsize=pp.onbar_fontsize, ha="center")
        #    ax.text(index, min * 2.2, round(row[pp.on_bar_field_2], 2), color='darkblue', fontsize=pp.onbar_fontsize, ha="center")

    if type == 'line':
        ax = sns.lineplot(x='month', y=field, data=df, sort=False, color=color, lw=2)

    ax.set_ylabel(field, fontsize=pp.ylabel_fontsize, color=color, labelpad=pad)
    ax.yaxis.label.set_color(color)

    #set tick mark size
    tkw = dict(size=5, width=3.0, labelsize=pp.ytick_fontsize)
    ax.tick_params(axis='y', colors=color, pad=pad, **tkw)
    ax.set_ylim([min, max])
    ax.set_yticks(np.linspace(min, max, 5))

    return ax

def overlay_plot(df):
    """function to create overlayed plots"""

    fig = plot_frame()

    pad = 0
    inc_r = 1
    inc_l = -0.02

    myIterator = cycle(['left', 'right', 'left','right','right'])

    for key, value in pp.plot_fields.items():
        side = next(myIterator)
        if side == 'right':
            inc = inc_r
            inc_r += 0.13
        else:
            inc = inc_l
            inc_l -= 0.09

        ax = make_subplot(fig, key, value[0], value[1], pad, inc, side)

        pad += 3

    # Shrink current axes by just a little
    box = ax.get_position()
    ax.set_position([box.x0 + 0.01, box.y0, box.width * 0.95, box.height])

    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pd.read_csv("data/test_data.csv")
    overlay_plot(df)

