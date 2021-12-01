# streaming
import streamlit as st
# dataframe
import pandas as pd
# plotting
import plotly.express as px
import plotly.graph_objs as go
# markdowns
from pathlib import Path
import streamlit as st


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.set_page_config(layout = "wide")

# retrieve returns for each ppo model
ppo_14_14_ret = pd.concat([pd.read_csv('./trained_models/df_actions_14_4.csv').set_index('date'),
        pd.read_csv('./trained_models/df_daily_return_14_4.csv',index_col='Unnamed: 0').set_index('date')],
                        axis=1)
ppo_14_15_ret = pd.concat([pd.read_csv('./trained_models/df_actions_14_5.csv').set_index('date'),
        pd.read_csv('./trained_models/df_daily_return_14_5.csv',index_col='Unnamed: 0').set_index('date')],
                        axis=1)

# save cumulative returns
ppo_cumpod_14 =(ppo_14_14_ret.daily_return+1).cumprod()-1
ppo_cumpod_15 =(ppo_14_15_ret.daily_return+1).cumprod()-1

# set time index
time_ind = pd.Series(ppo_14_14_ret.index)

st.header("AI investment Allocator")

page = st.sidebar.selectbox('Select page',['Model 4 vs Model 5','Markdown']) 

if page == 'Model 4 vs Model 5':
        ## plot ppo_4 vs_ppo_5
        trace3_portfolio = go.Scatter(x = time_ind, y = ppo_cumpod_14, mode = 'lines', name = 'PPO 4')
        trace4_portfolio = go.Scatter(x = time_ind, y = ppo_cumpod_15, mode = 'lines', name = 'PPO 5')
        fig = go.Figure()
        fig.add_trace(trace3_portfolio)
        fig.add_trace(trace4_portfolio)

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
    
        fig.update_layout(title={
                #'text': "Cumulative Return using FinRL",
                'y':0.85,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
        fig.update_layout(
            paper_bgcolor='rgba(1,1,0,0)',
            plot_bgcolor='rgba(1, 1, 0, 0)',
            #xaxis_title="Date",
            yaxis_title="Cumulative Return",
        xaxis={'type': 'date', 
            'tick0': time_ind[0], 
                'tickmode': 'linear', 
            'dtick': 86400000.0 *80}

        )
        fig.update_xaxes(showline=True,linecolor='black',showgrid=True, gridwidth=1, gridcolor='LightSteelBlue',mirror=True)
        fig.update_yaxes(showline=True,linecolor='black',showgrid=True, gridwidth=1, gridcolor='LightSteelBlue',mirror=True)
        fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='LightSteelBlue')

        st.plotly_chart(fig,use_container_width = True)
else:
	    ## Markdown
	
        intro_markdown = read_markdown_file("README.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)