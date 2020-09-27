# set plot dimensions
plot_title = 'My Plot Overlay'
title_font=24

# probably best to leave this alone
dims = (15,8)

# frame thickness
frame_width = 3

# x axis settings
xaxis = 'Month'
xlabel = 'Month'
xlabel_fontsize = 14
xtick_fontsize = 14

# y label settings
ytick_fontsize=12
ylabel_fontsize=14
# axis field:[line type,color]
plot_fields = {'ROAS':['bar', 'slategray'],
                'Clicks':['line', 'orangered'],
                'Spend':['line', 'royalblue'],
                'Sales':['line', 'black'],
                'Impressions':['line', 'darkcyan']}

# info for bar chart text
onbar_fontsize=14
onbar_fontcolor = 'darkblue'
on_bar_field_1 = 'Conv_Rate'
on_bar_label_1 = 'CR'
on_bar_field_2 = 'CPC'
on_bar_label_2 = 'CPC'
