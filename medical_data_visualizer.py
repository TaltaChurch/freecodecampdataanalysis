import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2 $$calcula bmi e criar coluna overweight 
df['BMI'] = df.weight/((df.height/100) ** 2)
df['overweight'] = (df.BMI > 25).astype(int)

df.drop(columns='BMI',axis=1, inplace=True)

# 3 $$normalizar valores para 0 e 1
df['cholesterol'] = (df.cholesterol > 1).astype(int)
df['gluc'] = (df.gluc > 1).astype(int)


def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])

    # 6
    df_cat =  df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')

    # 8
    fig = sns.catplot(
        data=df_cat,
        kind='bar',
        x='variable',
        y='total',
        hue='value',
        col='cardio'
    ).figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025))&
                 (df['height'] <= df['height'].quantile(0.975))&
                 (df['weight'] >= df['weight'].quantile(0.025))&
                 (df['weight'] <= df['weight'].quantile(0.975))   
                 ]
    

    # 12
    corr = df_heat.corr(numeric_only=True)

    # 13
    mask = np.triu(np.ones_like(corr))

    # 14
    fig, ax = plt.subplots(figsize=(7,7))
    

    # 15
    fig = sns.heatmap(data=corr,mask=mask,annot=True ,fmt=".1f",
        ax=ax,center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}).figure

    # 16
    fig.savefig('heatmap.png')
    return fig


if __name__ == "__main__":
    draw_cat_plot()
    
    draw_heat_map()
   
    
