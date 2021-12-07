# utilities
import pandas as pd
import numpy as np
from util import convert_daily_return_to_pyfolio_ts
# plotting
import plotly.graph_objs as go
import plotly.express as px

# URL to git repo
url_df = 'https://github.com/changjulian17/DataSciencePortfolio/blob/main/Investment_Portfolio/data/processed_data.pkl?raw=true'
url_ppo4_ret = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/results/df_daily_return_14_4.csv'
url_ppo5_ret = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/results/df_daily_return_14_5.csv'
url_ppo4_act = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/results/df_actions_14_4.csv'
url_ppo5_act = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/results/df_actions_14_5.csv'
url_drg_ret = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/results/df_drg_returns.csv'
url_minv_ret = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/results/df_minv_returns.csv'
url_rand_ret = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/results/df_rand_returns.csv'
url_strat_stat = 'https://raw.githubusercontent.com/changjulian17/DataSciencePortfolio/main/Investment_Portfolio/results/df_strat_stats.csv'
# Read files
df = pd.read_pickle(url_df)
df_ppo4_ret = pd.read_csv(url_ppo4_ret,index_col='Unnamed: 0')
df_ppo5_ret = pd.read_csv(url_ppo5_ret,index_col='Unnamed: 0')
df_ppo4_act = pd.read_csv(url_ppo4_act)
df_ppo5_act = pd.read_csv(url_ppo5_act)
df_drg_ret = pd.read_csv(url_drg_ret)
df_minv_ret = pd.read_csv(url_minv_ret)
df_rand_ret = pd.read_csv(url_rand_ret)
# df_strat_stat = pd.read_csv(url_strat_stat)

def overview_chart():
    # cumulative plot
    ppo_cumpod =((df_ppo5_ret.daily_return+1).cumprod()-1)*100
    drg_cumpod =((df_drg_ret.daily_return+1).cumprod()-1)*100
    rdm_cumpod =((df_rand_ret.daily_return+1).cumprod()-1)*100
    min_var_cumpod =((df_minv_ret.daily_return+1).cumprod()-1)*100
    time_ind = pd.Series(df_ppo4_ret.date)
    # traces
    trace0_portfolio = go.Scatter(x = time_ind, y = ppo_cumpod, mode = 'lines', name = 'AI Allocator')
    trace1_portfolio = go.Scatter(x = time_ind, y = drg_cumpod, mode = 'lines', name = 'Dragon')
    trace2_portfolio = go.Scatter(x = time_ind, y = rdm_cumpod, mode = 'lines', name = 'Random')
    trace3_portfolio = go.Scatter(x = time_ind, y = min_var_cumpod, mode = 'lines', name = 'Min-Variance')
    # plot trces
    fig = go.Figure()
    fig.add_trace(trace0_portfolio)
    fig.add_trace(trace1_portfolio)
    fig.add_trace(trace2_portfolio)
    fig.add_trace(trace3_portfolio)

    fig.update_layout(
        legend=dict(
            x=0,
            y=1,
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=15,
                color="black"),
            bgcolor="White",
            bordercolor="white",
            borderwidth=2),
    )
    fig.update_layout(title={
            #'text': "Cumulative Return using FinRL",
            'y':0.85,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    fig.update_layout(
        paper_bgcolor='rgba(1, 1, 0, 0)',
        plot_bgcolor='rgba(1, 1, 0, 0)',
        yaxis_title="Cumulative Return",
        xaxis={'type': 'date', 
                'tick0': time_ind[0], 
                'tickmode': 'linear', 
                'dtick': 86400000.0 *80})

    fig.update_xaxes(showline=True,linecolor='black',showgrid=True, gridwidth=1, gridcolor='LightSteelBlue',mirror=True)
    fig.update_yaxes(showline=True,linecolor='black',showgrid=True, gridwidth=1, gridcolor='LightSteelBlue',mirror=True)
    fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='LightSteelBlue')

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                    dict(count=1,
                        label="1y",
                        step="year",
                        stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    return fig

def strats_table():
    df_strat_stat.columns = ['Metric', 'AI Allocator', 'Random', 'Dragon', 'Min Var']
    df_strat_dsply = df_strat_stat.set_index('Metric')
    return df_strat_dsply

def dist_returns():
    d_rets = {'ppo_4' : convert_daily_return_to_pyfolio_ts(df_ppo4_ret),
              'ppo_5' : convert_daily_return_to_pyfolio_ts(df_ppo5_ret),
              'dragon' : convert_daily_return_to_pyfolio_ts(df_drg_ret),
              'min_var': convert_daily_return_to_pyfolio_ts(df_minv_ret),
              'random' : convert_daily_return_to_pyfolio_ts(df_rand_ret),
    }
    df_rets = pd.DataFrame(d_rets)*100
    df_rets_melt = pd.melt(df_rets.reset_index(),
                    id_vars=['date'],
                    var_name='portfolio',
                    value_name='Percent Return')

    fig = px.histogram(df_rets_melt, 
                        x="Percent Return", 
                        color="portfolio",
                        title="Percent return by portfolio",
                        barmode='group',
                        height=600,
                        )

    fig.update_layout(yaxis_range=(0, 100))

    return fig

def ppo_charts():
    # cumulative returns and time indices
    ppo_cumpod_14 =((df_ppo4_ret.daily_return+1).cumprod()-1)*100
    ppo_cumpod_15 =((df_ppo5_ret.daily_return+1).cumprod()-1)*100
    time_ind = pd.Series(df_ppo4_ret.date)
    # traces
    trace4_portfolio = go.Scatter(x = time_ind, y = ppo_cumpod_14, mode = 'lines', name = 'PPO 4')
    trace5_portfolio = go.Scatter(x = time_ind, y = ppo_cumpod_15, mode = 'lines', name = 'PPO 5')
    # plot traces
    fig = go.Figure()
    fig.add_trace(trace4_portfolio)
    fig.add_trace(trace5_portfolio)

    fig.update_layout(
        legend=dict(
            x=0,
            y=1,
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=15,
                color="black"
            ),
            bgcolor="White",
            bordercolor="white",
            borderwidth=2
            
        ),
    )
    fig.update_layout(title={'y':0.85,
                             'x':0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'})
    fig.update_layout(paper_bgcolor='rgba(1,1,0,0)',
                      plot_bgcolor='rgba(1, 1, 0, 0)',
                      yaxis_title="Cumulative Return",
                      xaxis={'type': 'date', 
                        'tick0': time_ind[0], 
                        'tickmode': 'linear', 
                        'dtick': 86400000.0 *80}
    )
    fig.update_xaxes(showline=True,linecolor='black',showgrid=True, gridwidth=1, gridcolor='LightSteelBlue',mirror=True)
    fig.update_yaxes(showline=True,linecolor='black',showgrid=True, gridwidth=1, gridcolor='LightSteelBlue',mirror=True)
    fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='LightSteelBlue')
    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                    dict(count=1,
                        label="1y",
                        step="year",
                        stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    return fig

def portfolio_weights():
    ppo_4_alloc = df_ppo4_act.set_index('date')*100
    ppo_5_alloc = df_ppo5_act.set_index('date')*100
    ppo_4_alloc = pd.melt(ppo_4_alloc.reset_index(),
                            id_vars=['date'],
                            var_name='Asset',
                            value_name='Percent Allocated')
    ppo_5_alloc = pd.melt(ppo_5_alloc.reset_index(),
                          id_vars=['date'],
                          var_name='Asset',
                          value_name='Percent Allocated')
    ## ppo4
    fig_ppo4 = px.bar(ppo_4_alloc, 
                x="date", 
                color="Asset",
                y='Percent Allocated',
                title="PPO 4 assets allocated from 2020 to August 2021",
                barmode='relative',
                height=600
                )
    # Add range slider
    fig_ppo4.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                    dict(count=1,
                        label="1y",
                        step="year",
                        stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        ),
        yaxis_range=(0, 100),
        showlegend=False
    )

    ## ppo5
    fig_ppo5 = px.bar(ppo_5_alloc, 
                x="date", 
                color="Asset",
                y='Percent Allocated',
                title="PPO 5 assets allocated from 2020 to August 2021",
                barmode='relative',
                height=600
                )
    # Add range slider
    fig_ppo5.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                    dict(count=1,
                        label="1y",
                        step="year",
                        stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        ),
        yaxis_range=(0, 100),
        # legend=dict(yanchor="top", 
        #         y=.5, 
        #         xanchor="right", 
        #         x=1.19,
        #         orientation= 'v')
    )

    # get drg as a dataframe
    drg_wt = [9.5,19, 5, 9.5, 19, 9.5, 19, 9.5]
    # plotly bar chart for drg portfolio
    colors=['blue','orange','green','red','purple', 'brown','pink','grey']
    fig_drg = go.Figure(data=[go.Bar(x=df_ppo5_act.columns.drop('date'),
                                     y=drg_wt,
                                     marker_color=colors
    )])
    # fix width
    fig_drg.update_layout(title_text='Dragon Portfolio Fixed Allocation (%)',
                    width=500,
                    height=500,)

    return fig_ppo4, fig_ppo5, fig_drg

def histo_wts():
    # create stacked histograms for % allocations
    ppo_14_4_alloc = df_ppo4_act[1:].set_index('date')*100
    ppo_14_5_alloc = df_ppo5_act[1:].set_index('date')*100
    ppo_14_4_alloc = pd.melt(ppo_14_4_alloc.reset_index(),
                            id_vars=['date'],
                            var_name='Asset',
                            value_name='Percent Allocated')
    ppo_14_5_alloc = pd.melt(ppo_14_5_alloc.reset_index(),
                            id_vars=['date'],
                            var_name='Asset',
                            value_name='Percent Allocated')
    # ppo 4 
    fig_hist_ppo4 = px.histogram(ppo_14_4_alloc, 
                x="Percent Allocated", 
                color="Asset",
                title="PPO 4 histogram of asset allocations",
                barmode='relative',
                height=600,
                marginal="rug"
                )
    # layout
    fig_hist_ppo4.update_layout(xaxis_range=(5, 28),
                           yaxis_range=(0, 600),
                           showlegend=False)
    # ppo5
    fig_hist_ppo5 = px.histogram(ppo_14_5_alloc, 
                x="Percent Allocated", 
                color="Asset",
                title="PPO 5 histogram of asset allocations",
                barmode='relative',
                height=600,
                marginal="rug"
                )
    # layout
    fig_hist_ppo5.update_layout(xaxis_range=(5, 28),
                            yaxis_range=(0, 1850))

    return fig_hist_ppo4, fig_hist_ppo5
    
def returns_table():
    df_rets = pd.concat([df_ppo4_ret,
                            df_ppo5_ret.daily_return,
                            df_drg_ret.daily_return,
                            df_minv_ret.daily_return,
                            df_rand_ret.daily_return],
                        axis=1).set_index('date')[1:]*100
    df_rets.columns = ['PP0 4','PPO 5', 'Dragon', 'Min Var', 'Random']
    return df_rets    