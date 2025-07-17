import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],index_col='date')

df = df[(df.value >= df.value.quantile(0.025)) &
              (df.value <= df.value.quantile(0.975))]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df.value,color='red', linewidth=0.5)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
   
    
    
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month
    df_bar['month_name'] = df.index.month_name()
    
    avg_view= df_bar.groupby(by=['year','month']).value.mean().reset_index().pivot(index='year', columns='month', values='value')
    
    fig= avg_view.plot(kind='bar',figsize=(12,6)).figure
    months = df_bar.groupby(by=['month','month_name']).size().reset_index().month_name

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(labels=months,title='Months')
    plt.tight_layout()
    
    fig.savefig('bar_plot.png')
    return fig
    
def draw_box_plot():
    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(16,6))
    
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df.index.year
    df_box['month'] = df.index.month
    df_box['month_name'] = df.index.month_name()
    months = df_box.groupby(by=['month','month_name']).size().reset_index().month_name.tolist()

    # Draw box plots (using Seaborn)
   
    sns.boxplot(data=df_box,x='year',y='value',hue='year',palette=sns.color_palette("tab10", 4),ax=ax1,legend=False, flierprops={  
        'marker': 'd',     
        'markerfacecolor': 'black',  
        'markersize': 2,    
        'markeredgecolor': 'black'  
    })
    
    
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    sns.boxplot(data=df_box,x='month_name',y='value',hue='month_name',palette=sns.color_palette("pastel", 12),ax=ax2,legend=False,order=months, flierprops={  
        'marker': 'd',     
        'markerfacecolor': 'black',  
        'markersize': 2,    
        'markeredgecolor': 'black'  
    })
    ax2.set_xticklabels([i[:3] for i in months])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    plt.tight_layout()
    
    fig.savefig('box_plot.png')
    return fig


if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()        
